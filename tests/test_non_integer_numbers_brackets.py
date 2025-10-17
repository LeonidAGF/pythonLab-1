from src.processing_rpn import processing_rpn


def test_non_integer_numbers_brackets():
    # проверка на выражениях с нецелыми числами и скобками
    assert processing_rpn("3.5+(3.5+(2.5))") == "9.5"
    assert processing_rpn("(2.2) + (4.4) - (2.2)") == "4.4"
    assert processing_rpn("(6.0 + 5.5 * 2)") == "17"
    assert processing_rpn("(3 / 2) * 3") == "4.5"
    assert processing_rpn("(((5)) // (3))* 2.5 * 2") == "5"
    assert processing_rpn("(5.1 - 3.0 / 2) ^ 0") == "1"
    assert processing_rpn("2 ^ 2 ^ 0 * 1 * 2 + 3 + 3  +(3.3)") == "11.3"
