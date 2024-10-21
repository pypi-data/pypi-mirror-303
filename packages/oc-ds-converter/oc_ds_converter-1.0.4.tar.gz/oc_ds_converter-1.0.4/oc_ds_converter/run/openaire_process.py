import functools
import os.path
import sys
from tarfile import TarInfo

import yaml
from oc_ds_converter.lib.file_manager import normalize_path
from oc_ds_converter.lib.jsonmanager import *
from oc_ds_converter.oc_idmanager.oc_data_storage.in_memory_manager import \
    InMemoryStorageManager
from oc_ds_converter.oc_idmanager.oc_data_storage.redis_manager import \
    RedisStorageManager
from oc_ds_converter.oc_idmanager.oc_data_storage.sqlite_manager import \
    SqliteStorageManager
from oc_ds_converter.openaire.openaire_processing import *
from pebble import ProcessFuture, ProcessPool
from tqdm import tqdm
from filelock import Timeout, FileLock


def preprocess(
        openaire_json_dir:str, publishers_filepath:str, orcid_doi_filepath:str, 
        csv_dir:str, wanted_doi_filepath:str=None, cache:str=None, verbose:bool=False, storage_path:str = None, 
        testing: bool = True, redis_storage_manager: bool = False, max_workers: int = 1, target=50000) -> None:

    if not testing: # NON CANCELLARE FILES MA PRENDI SOLO IN CONSIDERAZIONE
        input_dir_cont = os.listdir(openaire_json_dir)
        els_to_be_removed = []
        for el in input_dir_cont:
            if el.startswith("._"):
                els_to_be_removed.append(os.path.join(openaire_json_dir, el))
            else:
                if el.endswith(".tar"):
                    base_name = el.replace('.tar', '')
                    if [x for x in os.listdir(openaire_json_dir) if x.startswith(base_name) and x.endswith("decompr_zip_dir")]:
                        els_to_be_removed.append(os.path.join(openaire_json_dir, el))

        if els_to_be_removed: # Anziché els_to_be_removed +  os.remove(etbr), fare in modo di skippare (es. els_to_be_skipped + skip
            # in fase di lettura dell'input) questi compressi nel processo
            # nel caso in cui ci sia già un decompresso equivalente (per evitare di riprocessare inutilmente gli stessi dati)
            for etbr in els_to_be_removed:
                os.remove(etbr)



    # creare cartella di output se non esiste (dove verranno salvati i csv delle tabelle di meta)
    if not os.path.exists(csv_dir):
        os.makedirs(csv_dir)

    req_type = ".gz"

    # creare cartella _citations di output se non esiste (dove verranno salvati i csv delle citazioni)
    preprocessed_citations_dir = csv_dir + "_citations"
    if not os.path.exists(preprocessed_citations_dir):
        makedirs(preprocessed_citations_dir)
    if verbose:
        if publishers_filepath or orcid_doi_filepath or wanted_doi_filepath:
            what = list()
            if publishers_filepath:
                what.append('publishers mapping')
            if orcid_doi_filepath:
                what.append('DOI-ORCID index')
            if wanted_doi_filepath:
                what.append('wanted DOIs CSV')
            log = '[INFO: openaire_process] Processing: ' + '; '.join(what)
            print(log)

    
    if verbose:
        print(f'[INFO: openaire_process] Getting all files from {openaire_json_dir}')

    all_input_tar = os.listdir(openaire_json_dir)
    for tar in all_input_tar:
        all_files, targz_fd = get_all_files_by_type(os.path.join(openaire_json_dir, tar), req_type, cache)
        if not redis_storage_manager or max_workers == 1:
            for filename in all_files:
                get_citations_and_metadata(tar, preprocessed_citations_dir, csv_dir, filename, orcid_doi_filepath, wanted_doi_filepath, publishers_filepath, storage_path, redis_storage_manager, testing, cache, target)


        elif redis_storage_manager or max_workers > 1:
            with ProcessPool(max_workers=max_workers, max_tasks=1) as executor:
                for filename in all_files:
                    future:ProcessFuture = executor.schedule(
                        function = get_citations_and_metadata,
                        args=(tar, preprocessed_citations_dir, csv_dir, filename, orcid_doi_filepath, wanted_doi_filepath, publishers_filepath, storage_path, redis_storage_manager, testing, cache, target)
                    )


    if cache:
        if os.path.exists(cache):
            os.remove(cache)
    lock_file = cache + ".lock"
    if os.path.exists(lock_file):
        os.remove(lock_file)

    # added to avoid order-releted issues in sequential tests runs
    if testing:
        storage_manager = get_storage_manager(storage_path, redis_storage_manager, testing=testing)
        storage_manager.delete_storage()


def get_citations_and_metadata(tar: str, preprocessed_citations_dir: str, csv_dir: str, filename: str, orcid_index: str, doi_csv: str, publishers_filepath_openaire: str, storage_path: str, redis_storage_manager: bool, testing: bool, cache:str, target=50000):

    storage_manager = get_storage_manager(storage_path, redis_storage_manager, testing=testing)

    if cache:
        if not cache.endswith(".json"):
            cache = os.path.join(os.getcwd(), "cache.json")
        else:
            if not os.path.exists(os.path.abspath(os.path.join(cache, os.pardir))):
                Path(os.path.abspath(os.path.join(cache, os.pardir))).mkdir(parents=True, exist_ok=True)
    else:
        cache = os.path.join(os.getcwd(), "cache.json")

    last_part_processed = 0
    lock = FileLock(cache + ".lock")
    cache_dict = dict()
    write_new = False

    if os.path.exists(cache):
        with lock:
            with open(cache, "r", encoding="utf-8") as c:
                try:
                    cache_dict = json.load(c)
                except:
                    write_new = True
    else:
        write_new = True

    if write_new:
        with lock:
            with open(cache, "w", encoding="utf-8") as c:
                json.dump(cache_dict, c)

    # skip if in cache
    if tar in cache_dict:
        if filename in cache_dict[tar]:
            if cache_dict[tar][filename] == "completed":
                return
            else:
                last_part_processed = cache_dict[tar][filename]
        else:
            filename_alt = ''
            if '/' in filename:
                filename_alt = filename.replace('/', '\\')
            elif '\\' in filename:
                filename_alt = filename.replace('\\', '/')
            if filename_alt:
                if filename_alt in cache_dict[tar]:
                    if cache_dict[tar][filename_alt] == "completed":
                        return
                    else:
                        last_part_processed = cache_dict[tar][filename]

    openaire_csv = OpenaireProcessing(orcid_index=orcid_index, doi_csv=doi_csv, publishers_filepath_openaire=publishers_filepath_openaire, storage_manager=storage_manager, testing=testing)

    index_citations_to_csv = []
    data = []

    target = target

    skip_rows = target * last_part_processed

    f = gzip.open(filename, 'rb')
    source_data = f.readlines()
    pbar = tqdm(total=len(source_data))
    f.close()
    filename = filename.name if isinstance(filename, TarInfo) else filename
    filename_without_ext = filename.replace('.json', '').replace('.tar', '').replace('.gz', '')
    filepath_ne = os.path.join(csv_dir, f'{os.path.basename(filename_without_ext)}')
    filepath_citations_ne = os.path.join(preprocessed_citations_dir, f'{os.path.basename(filename_without_ext)}')

    filepath = os.path.join(csv_dir, f'{os.path.basename(filename_without_ext)}.csv')
    filepath_citations = os.path.join(preprocessed_citations_dir, f'{os.path.basename(filename_without_ext)}.csv')
    pathoo(filepath)

    def get_all_redis_ids_and_save_updates(sli_da):
        all_br = []
        all_ra = []
        for entity in sli_da:

            # start check: if line is processable
            if entity:
                d = json.loads(entity.decode('utf-8'))
                if d.get("relationship"):
                    if d.get("relationship").get("name") == "Cites":
                        # end check: if line is processable

                        ent_all_br, ent_all_ra = openaire_csv.extract_all_ids(json.loads(entity))
                        all_br.extend(ent_all_br)
                        all_ra.extend(ent_all_ra)

        redis_validity_values_br = openaire_csv.get_reids_validity_list(all_br, "br")
        redis_validity_values_ra = openaire_csv.get_reids_validity_list(all_ra, "ra")
        openaire_csv.update_redis_values(redis_validity_values_br, redis_validity_values_ra)

    def save_files(ent_list, citation_list, nf, is_last_sf=False):
        if ent_list:
            filename_str = filepath_ne+"_"+str(nf) + ".csv"
            with open(filename_str, 'w', newline='', encoding='utf-8') as output_file:
                dict_writer = csv.DictWriter(output_file, ent_list[0].keys(), delimiter=',', quotechar='"',
                                             quoting=csv.QUOTE_NONNUMERIC, escapechar='\\')
                dict_writer.writeheader()
                dict_writer.writerows(ent_list)
            ent_list = []

        if citation_list:
            filename_cit_str = filepath_citations_ne+"_"+str(nf) + ".csv"
            with open(filename_cit_str, 'w', newline='', encoding='utf-8') as output_file_citations:
                dict_writer = csv.DictWriter(output_file_citations, citation_list[0].keys(), delimiter=',',
                                             quotechar='"', quoting=csv.QUOTE_NONNUMERIC, escapechar='\\')
                dict_writer.writeheader()
                dict_writer.writerows(citation_list)
            citation_list = []

        openaire_csv.memory_to_storage()

        task_done(nf, is_last=is_last_sf)

        return ent_list, citation_list

    def task_done(file_part_number, is_last=False) -> None:
        try:
            if tar not in cache_dict:
                cache_dict[tar] = dict()

            if not is_last:
                cache_dict[tar][filename] = file_part_number
            else:
                cache_dict[tar][filename] = "completed"

            with lock:
                with open(cache, 'r', encoding='utf-8') as aux_file:
                    cur_cache_dict = json.load(aux_file)

                    for k,v in cur_cache_dict.items():
                        if not cache_dict.get(k) and cur_cache_dict.get(k):
                            cache_dict[k] = v
                        elif cache_dict[k] != v:
                            tar_files_processed_values_dict = cache_dict[k]
                            cur_tar_files_processed_values_dict = cur_cache_dict[k]

                            for c, w in cur_tar_files_processed_values_dict.items():
                                if tar_files_processed_values_dict.get(c) == "completed" or cur_tar_files_processed_values_dict.get(c) == "completed":
                                    cur_tar_files_processed_values_dict[c] = "completed"
                                elif isinstance(tar_files_processed_values_dict.get(c), int) and isinstance(cur_tar_files_processed_values_dict.get(c), int):
                                    cur_tar_files_processed_values_dict[c] = max([tar_files_processed_values_dict.get(c), cur_tar_files_processed_values_dict.get(c)])
                                elif isinstance(tar_files_processed_values_dict.get(c), int) or isinstance(cur_tar_files_processed_values_dict.get(c), int):
                                    cur_tar_files_processed_values_dict[c] = tar_files_processed_values_dict.get(c) if isinstance(tar_files_processed_values_dict.get(c), int) else cur_tar_files_processed_values_dict.get(c)

                            tar_files_processed_values_dict.update(cur_tar_files_processed_values_dict)
                            cache_dict[k] = tar_files_processed_values_dict

                    for k,v in cache_dict.items():
                        if k not in cur_cache_dict:
                            cur_cache_dict[k] = v

                    for k,v in cur_cache_dict.items():
                        if k not in cache_dict:
                            cache_dict[k] = v

                with open(cache, 'w', encoding='utf-8') as aux_file:
                    json.dump(cache_dict, aux_file)

        except Exception as e:
            print(e)


    start = skip_rows
    cnt = skip_rows
    end = start + target

    if len(source_data[start:]) > target:
        source_data_slice = source_data[start: end]
    else:
        source_data_slice = source_data[start:]

    get_all_redis_ids_and_save_updates(source_data_slice)

    for entity in source_data:

        # in case the current entity is the <target>nth entity
        if cnt == end:
            start = cnt
            end = start + target
            if len(source_data[start:]) > target:
                source_data_slice = source_data[start: end]
            else:
                source_data_slice = source_data[start:]

            # update redis validated id list + save citation and meta file
            get_all_redis_ids_and_save_updates(source_data_slice)
            last_part_processed += 1
            data, index_citations_to_csv = save_files(data, index_citations_to_csv, last_part_processed)

        # real entity process
        if entity:
            d = json.loads(entity.decode('utf-8'))
            if d.get("relationship"):
                if d.get("relationship").get("name") == "Cites":

                    norm_source_ids = []
                    norm_target_ids = []

                    any_source_id = ""
                    any_target_id = ""

                    source_entity = d.get("source")
                    if source_entity:
                        norm_source_ids = openaire_csv.get_norm_ids(source_entity['identifier'])
                        if norm_source_ids:
                            for e, nsi in enumerate(norm_source_ids):
                                stored_validity = openaire_csv.validated_as(nsi)
                                norm_source_ids[e]["valid"] = stored_validity


                    target_entity = d.get("target")
                    if target_entity:
                        norm_target_ids = openaire_csv.get_norm_ids(target_entity['identifier'])
                        if norm_target_ids:
                            for i, nti in enumerate(norm_target_ids):
                                stored_validity_t = openaire_csv.validated_as(nti)
                                norm_target_ids[i]["valid"] = stored_validity_t

                    # check that there is a citation we can handle (i.e.: expressed with ids we actually manage)
                    if norm_source_ids and norm_target_ids:

                        source_entity_upd_ids = {k:v for k,v in source_entity.items() if k != "identifier"}
                        source_valid_ids = [x for x in norm_source_ids if x["valid"] is True]
                        source_invalid_ids = [x for x in norm_source_ids if x["valid"] is False]
                        source_to_be_val_ids = [x for x in norm_source_ids if x["valid"] is None]
                        source_identifier = {}
                        source_identifier["valid"] = source_valid_ids
                        source_identifier["not_valid"] = source_invalid_ids
                        source_identifier["to_be_val"] = source_to_be_val_ids
                        source_entity_upd_ids["identifier"] = source_identifier
                        #source_entity_upd_ids["redis_validity_lists"] = [redis_validity_values_br, redis_validity_values_ra]

                        target_entity_upd_ids = {k:v for k,v in target_entity.items() if k != "identifier"}
                        target_valid_ids = [x for x in norm_target_ids if x["valid"] is True]
                        target_invalid_ids = [x for x in norm_target_ids if x["valid"] is False]
                        target_to_be_val_ids = [x for x in norm_target_ids if x["valid"] is None]
                        target_identifier = {}
                        target_identifier["valid"] = target_valid_ids
                        target_identifier["not_valid"] = target_invalid_ids
                        target_identifier["to_be_val"] = target_to_be_val_ids
                        target_entity_upd_ids["identifier"] = target_identifier
                        #target_entity_upd_ids["redis_validity_lists"] = [redis_validity_values_br, redis_validity_values_ra]

                        # creation of a new row in meta table because there are new ids to be validated.
                        # "any_source_id" will be chosen among the valid source entity ids, if any
                        if source_identifier["to_be_val"]:
                            source_tab_data = openaire_csv.csv_creator(source_entity_upd_ids) #valid_citation_ids_s --> evitare rivalidazione ?
                            if source_tab_data:
                                processed_source_ids = source_tab_data["id"].split(" ")
                                all_citing_valid = processed_source_ids
                                if all_citing_valid: # It meanst that there is at least one valid id for the citing entity
                                    any_source_id = all_citing_valid[0]
                                    data.append(source_tab_data) # Otherwise the row should not be included in meta tables


                        # skip creation of a new row in meta table because there is no new id to be validated
                        # "any_source_id" will be chosen among the valid source entity ids, if any
                        elif source_identifier["valid"]:
                            all_citing_valid = source_identifier["valid"]
                            any_source_id = all_citing_valid[0]["identifier"]

                        # creation of a new row in meta table because there are new ids to be validated.
                        # "any_target_id" will be chosen among the valid target entity ids, if any
                        if target_identifier["to_be_val"]:
                            target_tab_data = openaire_csv.csv_creator(target_entity_upd_ids)
                            if target_tab_data:
                                processed_target_ids = target_tab_data["id"].split(" ")
                                all_cited_valid = processed_target_ids
                                if all_cited_valid:
                                    any_target_id = all_cited_valid[0]
                                    data.append(target_tab_data) # otherwise the row should not be included in meta tables

                        # skip creation of a new row in meta table because there is no new id to be validated
                        # "any_target_id" will be chosen among the valid source entity ids, if any
                        elif target_identifier["valid"]:
                            all_cited_valid = target_identifier["valid"]
                            any_target_id = all_cited_valid[0]["identifier"]


                    if any_source_id and any_target_id:
                        citation = dict()
                        citation["citing"] = any_source_id
                        citation["referenced"] = any_target_id
                        index_citations_to_csv.append(citation)
        pbar.update()
        cnt += 1
    last_part_processed += 1
    data, index_citations_to_csv = save_files(data, index_citations_to_csv, last_part_processed, is_last_sf=True)
    pbar.close()

def get_storage_manager(storage_path: str, redis_storage_manager: bool, testing: bool):
    if not redis_storage_manager:
        if storage_path:
            if not os.path.exists(storage_path):
            # if parent dir does not exist, it is created
                if not os.path.exists(os.path.abspath(os.path.join(storage_path, os.pardir))):
                    Path(os.path.abspath(os.path.join(storage_path, os.pardir))).mkdir(parents=True, exist_ok=True)
            if storage_path.endswith(".db"):
                storage_manager = SqliteStorageManager(storage_path)
            elif storage_path.endswith(".json"):
                storage_manager = InMemoryStorageManager(storage_path)

        if not storage_path and not redis_storage_manager:
            new_path_dir = os.path.join(os.getcwd(), "storage")
            if not os.path.exists(new_path_dir):
                os.makedirs(new_path_dir)
            storage_manager = SqliteStorageManager(os.path.join(new_path_dir, "id_valid_dict.db"))
    elif redis_storage_manager:
        if testing:
            storage_manager = RedisStorageManager(testing=True)
        else:
            storage_manager = RedisStorageManager(testing=False)
    return storage_manager


def pathoo(path:str) -> None:
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

if __name__ == '__main__':
    arg_parser = ArgumentParser('openaire_process.py', description='This script creates CSV files from Openaire JSON files, enriching them through of a DOI-ORCID index')
    arg_parser.add_argument('-c', '--config', dest='config', required=False,
                            help='Configuration file path')
    required = not any(arg in sys.argv for arg in {'--config', '-c'})
    arg_parser.add_argument('-cf', '--openaire', dest='openaire_json_dir', required=required,
                            help='Openaire json files directory')
    arg_parser.add_argument('-out', '--output', dest='csv_dir', required=required,
                            help='Directory where CSV will be stored')
    arg_parser.add_argument('-p', '--publishers', dest='publishers_filepath', required=False,
                            help='CSV file path containing information about publishers (id, name, prefix)')
    arg_parser.add_argument('-o', '--orcid', dest='orcid_doi_filepath', required=False,
                            help='DOI-ORCID index filepath, to enrich data')
    arg_parser.add_argument('-w', '--wanted', dest='wanted_doi_filepath', required=False,
                            help='A CSV filepath containing what DOI to process, not mandatory')
    arg_parser.add_argument('-ca', '--cache', dest='cache', required=False,
                        help='The cache file path. This file will be deleted at the end of the process')
    arg_parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', required=False,
                            help='Show a loading bar, elapsed time and estimated time')
    arg_parser.add_argument('-sp', '--storage_path', dest='storage_path', required=False,
                            help='path of the file where to store data concerning validated pids information.'
                                 'Pay attention to specify a ".db" file in case you chose the SqliteStorageManager'
                                 'and a ".json" file if you chose InMemoryStorageManager')
    arg_parser.add_argument('-t', '--testing', dest='testing', action='store_true', required=False,
                            help='parameter to define if the script is to be run in testing mode. Pay attention:'
                                 'by default the script is run in test modality and thus the data managed by redis, '
                                 'stored in a specific redis db, are not retrieved nor permanently saved, since an '
                                 'instance of a FakeRedis class is created and deleted by the end of the process.')
    arg_parser.add_argument('-r', '--redis_storage_manager', dest='redis_storage_manager', action='store_true', required=False,
                            help='parameter to define whether or not to use redis as storage manager. Note that by default the parameter '
                                 'value is set to false, which means that -unless it is differently stated- the storage manager used is'
                                 'derived by the storage filepath type (i.e.: .db or .json). The redis db used by the storage manager is the n.2')
    arg_parser.add_argument('-m', '--max_workers', dest='max_workers', required=False, default=1, type=int, help='Workers number')
    args = arg_parser.parse_args()
    config = args.config
    settings = None
    if config:
        with open(config, encoding='utf-8') as f:
            settings = yaml.full_load(f)
    openaire_json_dir = settings['openaire_json_dir'] if settings else args.openaire_json_dir
    openaire_json_dir = normalize_path(openaire_json_dir)
    csv_dir = settings['output'] if settings else args.csv_dir
    csv_dir = normalize_path(csv_dir)
    publishers_filepath = settings['publishers_filepath'] if settings else args.publishers_filepath
    publishers_filepath = normalize_path(publishers_filepath) if publishers_filepath else None
    orcid_doi_filepath = settings['orcid_doi_filepath'] if settings else args.orcid_doi_filepath
    orcid_doi_filepath = normalize_path(orcid_doi_filepath) if orcid_doi_filepath else None
    wanted_doi_filepath = settings['wanted_doi_filepath'] if settings else args.wanted_doi_filepath
    wanted_doi_filepath = normalize_path(wanted_doi_filepath) if wanted_doi_filepath else None
    cache = settings['cache_filepath'] if settings else args.cache
    cache = normalize_path(cache) if cache else None
    verbose = settings['verbose'] if settings else args.verbose
    storage_path = settings['storage_path'] if settings else args.storage_path
    storage_path = normalize_path(storage_path) if storage_path else None
    testing = settings['testing'] if settings else args.testing
    redis_storage_manager = settings['redis_storage_manager'] if settings else args.redis_storage_manager
    max_workers = settings['max_workers'] if settings else args.max_workers

    preprocess(openaire_json_dir=openaire_json_dir, publishers_filepath=publishers_filepath,
               orcid_doi_filepath=orcid_doi_filepath, csv_dir=csv_dir, wanted_doi_filepath=wanted_doi_filepath, 
               cache=cache, verbose=verbose, storage_path=storage_path, testing=testing, 
               redis_storage_manager=redis_storage_manager, max_workers=max_workers)
