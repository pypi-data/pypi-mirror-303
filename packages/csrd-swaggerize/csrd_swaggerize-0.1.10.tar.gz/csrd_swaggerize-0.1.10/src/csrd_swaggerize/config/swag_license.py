from csrd_utils.config import _Config
from csrd_swaggerize.models import License


class SwagLicense(_Config):
    _name: str
    _url: str

    def __init__(self, data: dict = None, *, license: License = None, name: str = None, url: str = None):
        if license is not None:
            self.from_enum(license)
            return

        data = self._init_data(data)
        self._name = name or data.get("name", None)
        self._url = url or data.get("url", None)

    def from_enum(self, license: License):
        if license == License.Apache:
            self._name = "Apache 2.0"
            self._url = "http://www.apache.org/licenses/LICENSE-2.0.html"
        else:
            self._name = None
            self._url = None

    def compile(self):
        if self._name is not None:
            self._init_template()
            self._template["name"] = self._name
        if self._url is not None:
            self._init_template()
            self._template["url"] = self._url
        return  self._template