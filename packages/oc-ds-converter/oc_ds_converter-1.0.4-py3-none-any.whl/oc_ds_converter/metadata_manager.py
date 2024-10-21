#!python
# Copyright 2022, Arianna Moretti <arianna.moretti4@unibo.it>, Arcangelo Massari <arcangelo.massari@unibo.it>
#
# Permission to use, copy, modify, and/or distribute this software for any purpose
# with or without fee is hereby granted, provided that the above copyright notice
# and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT,
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
# DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
# SOFTWARE.


import importlib
from urllib.parse import quote

from oc_ds_converter.oc_idmanager.isbn import ISBNManager
from oc_ds_converter.oc_idmanager.issn import ISSNManager
from oc_ds_converter.oc_idmanager.orcid import ORCIDManager


class MetadataManager():
    def __init__(self, metadata_provider:str, api_response:dict, orcid_doi_filepath:str):
        self.metadata_provider = metadata_provider
        self.api_response = api_response
        self.orcid_doi_filepath = orcid_doi_filepath
        self._issnm = ISSNManager()
        self._isbnm = ISBNManager()
        self._om = ORCIDManager()
        from oc_ds_converter.oc_idmanager.doi import DOIManager
        self.doi_manager = DOIManager()
        self._have_api = ['crossref', 'datacite', 'medra', 'jalc']

    def extract_metadata(self) -> None:
        metadata = {'ra': self.metadata_provider}
        if self.metadata_provider is None or self.api_response is None:
            return metadata
        if self.metadata_provider == 'unknown':
            return self.extract_from_unknown()
        elif self.metadata_provider in self._have_api:
            module = importlib.import_module(f'oc_ds_converter.{self.metadata_provider}.{self.metadata_provider}_processing')
            class_ = getattr(module, f'{self.metadata_provider.title()}Processing')
            metadata_processor = class_(orcid_index=self.orcid_doi_filepath)
            api_response = self.api_response['data'] if self.metadata_provider == 'datacite' else self.api_response
            metadata.update(getattr(metadata_processor, 'csv_creator')(api_response))                
        return metadata

    def extract_from_unknown(self) -> None:
        metadata = dict()
        api_response: dict = self.api_response[0]
        if api_response.get('status') == 'Error':
            metadata['ra'] = 'unknown'
            return metadata
        elif api_response.get('status') == 'DOI does not exist':
            metadata['ra'] = 'invalid'
            return metadata
        registration_agency = self.api_response[0]['RA'].lower()
        metadata['ra'] = registration_agency
        doi = self.api_response[0]['DOI']
        api_registration_agency = getattr(self.doi_manager, f'_api_{registration_agency}')
        if api_registration_agency:
            from oc_ds_converter.lib.file_manager import call_api
            url = api_registration_agency + quote(doi)
            r_format = 'xml' if registration_agency == 'medra' else 'json'
            extra_api_result = call_api(url=url, headers=self.doi_manager._headers, r_format=r_format)
            self.metadata_provider = registration_agency
            self.api_response = extra_api_result
            try:
                metadata.update(self.extract_metadata())
            except Exception as e:
                print(doi, registration_agency)
                print(e)
                raise(Exception)
        return metadata