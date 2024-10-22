from flasgger import Swagger
from .config import SwagConfig
from ._utils import init_responses, init_params
from csrd_models import Entity
from flask import Flask
import inspect
from typing import List


class Swaggerize:
    def __init__(self, app: Flask, config: SwagConfig = None):
        self.config = config or SwagConfig()
        self._swagger = Swagger(app, template=self.config.compile())

    @staticmethod
    def build_docs(func, *, tags=None, error_response: Entity, request_model: Entity = None, response_model: Entity = None):
        docs = {}

        parameters = Swaggerize.build_parameters(func=func, request_model=request_model)
        responses = Swaggerize.build_responses(response_model=response_model, error_response=error_response)

        if tags is not None:
            docs['tags'] = tags

        if responses is not None:
            docs['responses'] = responses

        if parameters is not None:
            docs['parameters'] = parameters

        return docs

    @staticmethod
    def build_parameters(func, *, request_model: Entity = None) -> List:
        parameters = None

        if inspect.get_annotations(func):
            parameters = init_params(parameters)
            for key in inspect.get_annotations(func):
                parameters.append({
                    'in': 'path',
                    'name': key,
                    'description': 'baz bar foo',
                    'type': 'string',
                    'required': True,
                })

        if request_model and hasattr(request_model, 'schema'):
            parameters = init_params(parameters)
            parameters.append({
                'in': 'body',
                'name': 'body',
                'description': 'foo bar baz',
                'required': True,
                'schema': {
                    '$ref': f'#/definitions/{request_model.__name__}'
                }
            })

        return parameters

    @staticmethod
    def build_responses(response_model: Entity, error_response: Entity) -> dict:
        responses = {'200': {}}
        if response_model and hasattr(response_model, 'schema'):
            responses = init_responses(responses)
            responses['200'] = {
                "schema": {
                    "$ref": f'#/definitions/{response_model.__name__}'
                }
            }

        if error_response and hasattr(error_response, 'schema'):
            responses = init_responses(responses)
            responses['500'] = {
                "schema": {
                    "$ref": f'#/definitions/{error_response.__name__}'
                }
            }

        return responses
