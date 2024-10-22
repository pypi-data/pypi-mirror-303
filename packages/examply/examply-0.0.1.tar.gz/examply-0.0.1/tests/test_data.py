"""Unit Tests for the data module, written for pytest
"""

from examply import data


class TestData:
    """Test group"""

    def test_load_config(self):
        """Test mod"""
        assert data.load_config("sample1") == {"key": "value"}
