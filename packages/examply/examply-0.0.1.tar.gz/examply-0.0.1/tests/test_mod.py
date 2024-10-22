"""Unit Tests for the mod module, written for pytest
"""

from examply import mod


class TestMod:
    """Test group"""

    def test_mod(self):
        """Test mod"""
        assert mod.add(1, 2) == 3
