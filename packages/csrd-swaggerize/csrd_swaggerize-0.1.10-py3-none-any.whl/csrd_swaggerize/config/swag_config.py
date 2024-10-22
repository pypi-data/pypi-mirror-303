from typing import List, Dict, Union
from .swag_info import SwagInfo
from csrd_utils.config import _Config


class SwagConfig(_Config):
    _host: str = None
    _definitions: dict = None
    _info: SwagInfo = None
    _schemes: List[str] = ['http', 'https']
    _swagger: str = None

    def __init__(self, data: dict = None, *, host=None, definitions = None, schemes = None, info: Union[SwagInfo, Dict] = None, swagger = None):
        data = self._init_data(data)
        self._definitions = definitions or data.get("definitions", None)
        self._schemes = schemes or data.get("schemes", None)
        if type(info) is dict:
            info = SwagInfo(**info)
        self._info = info or SwagInfo(**data.get("info", {}))
        self._host = host or data.get("host", None)
        self._swagger = swagger or '2.0'
        # self._swagger = swagger or '3.0.0'

    def _init_definitions(self):
        if self._definitions is None:
            self._definitions = {}

    @property
    def definitions(self):
        self._init_definitions()
        return self._definitions

    @definitions.setter
    def definitions(self, definitions: dict):
        self._init_definitions()
        self._definitions = definitions

    def add_definitions(self, definitions: dict):
        if definitions is not None:
            self._init_definitions()
            self._definitions.update(definitions)

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, host):
        self._host = host

    def _init_info(self):
        if self._info is None:
            self._info = SwagInfo()

    @property
    def info(self):
        self._init_info()
        return self._info

    @info.setter
    def info(self, info):
        self._init_info()
        self._info = info

    @property
    def schemes(self):
        return self._schemes

    @schemes.setter
    def schemes(self, schemes):
        self._schemes = schemes


    def compile(self):
        if self._definitions is not None:
            self._init_template()
            self._template['definitions'] = self._definitions
        if self._host is not None:
            self._init_template()
            self._template['host'] = self._host
        if self._info.compile() is not None:
            self._init_template()
            self._template['info'] = self._info.compile()
        if self._schemes is not None:
            self._init_template()
            self._template['schemes'] = self._schemes
        if self._swagger is not None:
            self._init_template()
            if self._swagger == '2.0':
                self._template['swagger'] = self._swagger
                self._template['openapi'] = self._swagger
            else:
                self._template['swagger'] = self._swagger
                self._template['openapi'] = self._swagger

        return self._template
