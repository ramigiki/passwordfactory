from app.api.utilities import get_characters, generate_password


def test_get_character_output_type():
    """
    Test get_characters method output type: always be a list

    """
    arguments = {}
    output = get_characters(**arguments)
    assert type(output) == list


def test_get_character_numbers():
    """
    Test the numbers should be from 0-9
    Test that numbers exists in the list
    """
    arguments = {"numbers": 1}
    output = get_characters(**arguments)
    assert len(output) == 10
    assert '0' in output
    assert '9' in output


def test_get_characters_lowercase():
    """
    Test the lowercase characters in the list
    Test that lowercase characters should be 26
    Test that some lowercase characters exist
    """
    arguments = {"lowercase": 1}
    output = get_characters(**arguments)
    assert len(output) == 26
    assert "a" in output
    assert "r" in output
    assert "z" in output


def test_get_characters_uppercase():
    """
    Test the uppercase characters in the list
    Test that uppercase characters should be 26
    Test that some uppercase characters exist
    """
    arguments = {"uppercase": 1}
    output = get_characters(**arguments)
    assert len(output) == 26
    assert "A" in output
    assert "R" in output
    assert "Z" in output


def test_get_characters_symbols():
    """
    Test the symbols in the list
    Test that some symbols exist in the list
    """
    arguments = {"symbols": 1}
    output = get_characters(**arguments)
    assert "@" in output
    assert "!" in output
    assert "#" in output


def test_get_characters_all():
    """
    Collective test to test all the returned chars at once
    """
    arguments = {"numbers": 1, "lowercase": 1, "uppercase": 1, "symbols": 1}
    output = get_characters(**arguments)
    assert "S" in output
    assert "o" in output
    assert "4" in output
    assert "#" in output


def test_generate_password_numbers():
    """
    Test number password generation
    """
    arguments = {"length": 10, "numbers": 1}
    output = generate_password(**arguments)
    assert len(output) == 10
    assert "a" not in output
    assert "B" not in output
    assert "$" not in output


def test_generate_password_lowercase():
    arguments = {"length": 100, "lowercase": 1}
    output = generate_password(**arguments)
    assert len(output) == 100
    assert "4" not in output
    assert "B" not in output
    assert "$" not in output


def test_generate_password_uppercase():
    arguments = {"length": 200, "uppercase": 1}
    output = generate_password(**arguments)
    assert len(output) == 200
    assert "2" not in output
    assert "b" not in output
    assert "$" not in output


def test_generate_password_symbols():
    arguments = {"length": 5, "symbols": 1}
    output = generate_password(**arguments)
    assert len(output) == 5
    assert "4" not in output
    assert "a" not in output
    assert "B" not in output
