import glob
import json
import os
import os.path
from os import listdir, makedirs
from os.path import exists, join

from oc_ds_converter.preprocessing.base import Preprocessing
from tqdm import tqdm


class DatacitePreProcessing(Preprocessing):
    """This class aims at pre-processing DataCite dumps.
    In particular, DatacitePreProcessing splits the original nldJSON in many JSON files, each one containing the number of entities specified in input by the user. Further, the class discards those entities that do not provide useful information for meta"""

    def __init__(self, input_dir, output_dir, interval, filter=None, low_memo=True):
        self._req_type = ".json"
        self._input_dir = input_dir
        self._output_dir = output_dir
        self._needed_info = ["relationType", "relatedIdentifierType", "relatedIdentifier"]
        if not exists(self._output_dir):
            makedirs(self._output_dir)
        self._interval = interval
        if low_memo:
            self._low_memo = low_memo
        else:
            self._low_memo = True
        if filter:
            self._filter = filter
        else:
            self._filter = ["references", "isreferencedby", "cites", "iscitedby"]
        super(DatacitePreProcessing, self).__init__()

    def split_input(self):
        # restart from the last processed line, in case of previous process interruption
        out_dir = listdir(self._output_dir)
        # Checking if the list is empty or not
        if len(out_dir) != 0:
            list_of_files = glob.glob(join(self._output_dir, '*.json'))  # * means all if need specific format then *.csv
            latest_file = max(list_of_files, key=os.path.getctime)
            with open(latest_file, encoding="utf8") as f:
                recover_dict = json.load(f)
                data_list = recover_dict["data"]
                last_processed_dict = data_list[-1]
                last_dict_id = last_processed_dict["id"]
                f.close()
        else:
            last_processed_dict = None

        all_files, targz_fd = self.get_all_files(self._input_dir, self._req_type)
        len_all_files = len(all_files)
        data = []
        #pre_count = 0
        count = 0

        for file_idx, file in enumerate(all_files, 1):
            if not self._low_memo:
                f = self.load_json(file, targz_fd, file_idx, len_all_files)
            else:
                f = open(file, encoding="utf8")
            #verificare corretto funzionamento con opzione LOW MEMO = False !!! OPZIONE LOW MEMO FALSE NON VA LETTA COME STRINGA
            for line in tqdm(f):
                if self._low_memo:
                    if last_processed_dict is not None:
                        if not line.startswith('{"id":"' + last_dict_id+'",') :
                            #pre_count += 1
                            continue
                        else:
                            last_processed_dict = None
                            # pre_count += 1
                            # count = pre_count
                            continue
                    else:
                        pass
                else:
                    if last_processed_dict is not None:
                        if line.get("id") != last_dict_id:
                            #pre_count += 1
                            continue
                        else:
                            last_processed_dict = None
                            # pre_count += 1
                            # count = pre_count
                            continue
                    else:
                        pass

                # count += 1
                # to be logged: print("Processing entity n.:", n_lines)
                if self._low_memo:
                    try:
                        linedict = json.loads(line)
                    except:
                        print(ValueError, line)
                        continue
                else:
                    linedict = line
                if 'id' not in linedict or 'type' not in linedict:
                    continue
                if linedict['type'] != "dois":
                    continue
                attributes = linedict["attributes"]
                rel_ids = attributes.get("relatedIdentifiers")

                if rel_ids:
                    for ref in rel_ids:
                        if all(elem in ref for elem in self._needed_info):
                            relatedIdentifierType = (str(ref["relatedIdentifierType"])).lower()
                            relationType = str(ref["relationType"]).lower()
                            if relatedIdentifierType == "doi":
                                if relationType in self._filter:
                                    data.append(linedict)
                                    count += 1
                                    break


                data = self.splitted_to_file(
                    count, self._interval, self._output_dir, data
                )
            f.close()

        if len(data) > 0:
            count = count + (self._interval - (int(count) % int(self._interval)))
            data = self.splitted_to_file(count, self._interval, self._output_dir, data)


    def splitted_to_file(self, cur_n, target_n, out_dir, data, headers=None):
        if not exists(out_dir):
            makedirs(out_dir)
        dict_to_json = dict()
        if int(cur_n) != 0 and int(cur_n) % int(target_n) == 0:
            # to be logged: print("Processed lines:", cur_n, ". Reduced csv nr.", cur_n // target_n)
            filename = "jSonFile_" + str(cur_n // target_n) + self._req_type
            with (
                    open(os.path.join(out_dir, filename), "w", encoding="utf8")
            ) as json_file:
                dict_to_json["data"] = data
                json.dump(dict_to_json, json_file)
                empt_list = []
            return empt_list
        else:
            return data


