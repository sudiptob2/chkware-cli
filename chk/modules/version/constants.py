from chk.console.app_container import app
from typing import Dict


class BaseDocElements:
    """represent the base of all kind of documents"""
    VERSION = 'version'


class VersionStrToSpecConfigMapping:
    """VersionStrToSpecConfigMapping lists all archetypes by version string"""

    data: Dict = {
        "default:http:0.7.2": "chk.modules.http.entities.HttpConfigV072",
    }

    @classmethod
    def find_by_version(cls, key: str) -> str:
        """find config by version str"""
        if not isinstance(key, str): raise SystemExit(app.messages.exception.fatal.V0004)

        class_map = cls.data.get(key)
        if not isinstance(class_map, str): raise SystemExit(app.messages.exception.fatal.V0004)
        elif len(class_map) == 0: raise SystemExit(app.messages.exception.fatal.V0004)

        return class_map
