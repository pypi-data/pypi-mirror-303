from csrd_utils.config import _Config
from csrd_swaggerize.config import SwagConfig
from typing import List


class Config(_Config):
    _api_prefix: str = None
    _swagger: SwagConfig = None
    _cors_headers: str | List[str] | None = None
    _cors_origins: str | List[str] | None = '*'

    def __init__(self, *, swagger: SwagConfig = None, api_prefix: str = None, cors_origins: str | List[str] = None, cors_headers: str | List[str] = None):
        self._cors_origins = cors_origins or '*'
        self._cors_headers = cors_headers or '*'
        self._api_prefix = api_prefix or '/api'
        self._swagger = swagger

    def _init_swag(self):
        if self._swagger is None:
            self._swagger = SwagConfig()

    @property
    def api_prefix(self) -> str:
        return self._api_prefix

    @property
    def cors_origins(self) -> str | List[str]:
        return self._cors_origins

    @property
    def cors_headers(self) -> str | List[str]:
        return self._cors_headers

    @property
    def swagger(self) -> SwagConfig:
        self._init_swag()
        return self._swagger

    @swagger.setter
    def swagger(self, swagger):
        self._swagger = swagger

    def compile(self):
        if self._swagger is not None:
            self._init_template()
            self._template['swagger'] = self._swagger.compile()
        return self._template
