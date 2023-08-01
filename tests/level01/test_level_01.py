from subprocess import run, PIPE
from netgarage.utils.settings import LevelSettings
from netgarage.level01 import Solver, ExecutableCache
from unittest.mock import MagicMock, patch
import pytest

LEVEL_EXECUTABLE_MOCK = 'resources/bin/level01.sh'
ECHO_EXECUTABLE = 'resources/bin/echo_input.sh'

PASSCODE_STR = 'passcode'

parameters = [
    ([1,2,3], None),
    ([1,2,123], PASSCODE_STR),
]


def _fake_run(number: int):
    if number == 123:
        return PASSCODE_STR
    return None

@pytest.mark.parametrize('inputs, expected_passcode', parameters)
def test_solve(inputs, expected_passcode):
    with patch(
            "netgarage.level01.ExecutableCache.run",
            wraps=_fake_run) as mock_bar:
        settings = LevelSettings(1)
        solver = Solver(settings)
        passcode = solver.solve(inputs)
        assert passcode == expected_passcode


def test_solve_cache():
    with patch(
            "netgarage.level01.ExecutableCache.run",
            wraps=_fake_run) as mock_bar:
        settings = LevelSettings(1)
        solver = Solver(settings)
        solver.solve([123])
        assert solver.result == PASSCODE_STR


def test_executable_cache():
    cache = ExecutableCache(LEVEL_EXECUTABLE_MOCK)
    cache.run(2)
    cache.run(4)
    assert cache.get(1) is None
    assert cache.get(2)
    assert cache.get(4)