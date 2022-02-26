import pytest
import tests
from chk.archetypes.defaults.http_config import HttpV072
from chk.support.loader import ChkFileLoader


class TestHttpV072:
    """Test chk.archetypes.defaults.http_config.HttpV072"""

    def test_validate_schema(self):
        """when version string not given"""
        config = {
            'version': 'default:http:0.7.2',
            'request': {
                'url': 'https://example.com',
                'method': 'GET'
            }
        }

        ver = HttpV072()
        assert ver.validate_config(config) is True

    def test_validate_fail_if_url_empty(self):
        """when version string not given"""
        config = {
            'version': 'default:http:0.7.2',
            'request': {
                'url': None,
                'method': 'GET'
            }
        }

        ver = HttpV072()

        with pytest.raises(SystemExit) as ex:
            assert ver.validate_config(config) is True

        print(str(ex.value))
