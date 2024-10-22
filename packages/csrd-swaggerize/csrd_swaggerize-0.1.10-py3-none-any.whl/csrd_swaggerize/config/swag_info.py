from .swag_contact import SwagContact
from .swag_license import SwagLicense, License
from csrd_utils.config import _Config

from typing import Union, Dict


class SwagInfo(_Config):
    def __init__(self, title = None, version = None, *, description=None, terms_of_service=None, termsOfService=None, contact: Union[SwagContact | Dict] = None, license: Union[SwagLicense | Dict | License] = None):
        self._title = title or 'A CSRD API'
        self._version = version or '0.0.1'
        self._description = description or 'powered by CSRD'

        self._tos = termsOfService or terms_of_service or '/tos'
        if type(contact) is dict:
            contact = SwagContact(**contact)
        self._contact = contact or SwagContact()
        if license is not None:
            if type(license) is dict:
                license = SwagLicense(**license)
            if type(license) is License:
                license = SwagLicense(license=license)
        self._license = license or SwagLicense()

    def compile(self) -> dict:
        if self._title is not None:
            self._init_template()
            self._template['title'] = self._title
        if self._version is not None:
            self._init_template()
            self._template['version'] = self._version
        if self._description is not None:
            self._init_template()
            self._template['description'] = self._description
        if self._tos is not None:
            self._init_template()
            self._template['tos'] = self._tos
        if self._contact.compile() is not None:
            self._init_template()
            self._template['contact'] = self._contact.compile()
        if self._license.compile() is not None:
            self._init_template()
            self._template['license'] = self._license.compile()
        return self._template
