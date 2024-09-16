from enum import StrEnum
import pytest


class TtStrEnum(StrEnum):
    AA = "aa"
    BB = "bb"


class TestTtStrEnum:

    @pytest.mark.parametrize(
        ["parameter", "expected"],
        [
            pytest.param("AA", "aa", id="AA"),
            pytest.param("BB", "bb", id="BB"),
        ],
    )
    def test_get_name_success(self, parameter, expected):
        # Given
        # When
        # Then
        assert TtStrEnum[parameter] == expected, "取得失敗"

    @pytest.mark.parametrize(
        ["parameter", "expected"],
        [
            pytest.param("aa", "aa", id="aa"),
            pytest.param("bb", "bb", id="bb"),
        ],
    )
    def test_get_value_success(self, parameter, expected):
        # Given
        # When
        # Then
        assert TtStrEnum(parameter) == expected, "取得失敗"
