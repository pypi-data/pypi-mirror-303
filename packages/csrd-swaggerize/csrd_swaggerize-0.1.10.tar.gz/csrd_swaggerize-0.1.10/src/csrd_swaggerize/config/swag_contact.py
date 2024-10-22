from csrd_utils.config import _Config


class SwagContact(_Config):
    _email: str
    _name: str
    _url: str

    def __init__(self, data: dict = None, *, email: str = None, name: str = None, url: str = None):
        data = self._init_data(data)
        self._email = email or data.get("email", None)
        self._name = name or data.get("name", None)
        self._url = url or data.get("url", None)

    def compile(self):
        if self._email is not None:
            self._init_template()
            self._template["email"] = self._email
        if self._name is not None:
            self._init_template()
            self._template["name"] = self._name
        if self._url is not None:
            self._init_template()
            self._template["url"] = self._url
        return  self._template
