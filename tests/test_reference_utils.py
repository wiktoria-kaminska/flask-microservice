from api.reference_utils import validate_ref

def test_alphabetic_reference_valid():
    assert validate_ref('ABCDEFGHJI')

def test_numeric_reference_valid():
    assert validate_ref('1234567890')

def test_mixed_reference_valid():
    assert validate_ref('ABCDE12345')


def test_special_characters_invalid():
    assert not validate_ref('%$ABCDERTF')


def test_short_reference_invalid():
    assert not validate_ref('283746')

def test_long_reference_invalid():
    assert not validate_ref('9348572893434') 