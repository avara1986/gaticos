from unittest.mock import patch

import pytest
from click.testing import CliRunner

from gaticos.main import PhraseGenerator, animame, main


@pytest.mark.parametrize("input_count", [1, 2, 3, 4, 5, 6, 7, 8])
def test_main(input_count):
    runner = CliRunner()
    result = runner.invoke(main, ['--count', input_count])
    assert result.output == "Miau!\n" * input_count
    assert result.exit_code == 0


@patch.object(PhraseGenerator, "gen_random_phrase")
def test_animame(mock_gen_random_phrase):
    runner = CliRunner()
    mock_gen_random_phrase.return_value = "Mock de la función original"
    result = runner.invoke(
        main,
        [
            'animame',
        ],
    )

    assert "Mock de la función original" in result.output


def test_gen_random_phrase():
    expected_results = PhraseGenerator.list_phases
    assert PhraseGenerator.gen_random_phrase() in expected_results
