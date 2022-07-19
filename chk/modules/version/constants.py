from typing import Dict


class VersionConfigNode:
    """represent the base of all kind of documents"""
    VERSION = 'version'


class VersionStrToSpecConfigMapping:
    """VersionStrToSpecConfigMapping lists all archetypes by version string"""

    data: Dict = {
        "default:http:0.7.2": "chk.modules.http.entities.HttpSpec_V072",
    }
