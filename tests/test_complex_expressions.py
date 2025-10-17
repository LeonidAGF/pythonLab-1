from src.processing_rpn import processing_rpn


def test_complex_expressions():
    # проверка на выражениях с несколькими операциями и скобками
    assert processing_rpn("3+3+3") == "9"
    assert processing_rpn("2-3+1") == "0"
    assert processing_rpn("5*5+6") == "31"
    assert processing_rpn("(4 / 2) * 5") == "10"
    assert processing_rpn("(((5)) // (3) ) * 2 ") == "2"
    assert processing_rpn("5 % 3 % 2 ^ 2 ") == "2"
    assert processing_rpn("2 ^ 2 ^ 0 * 1 * 2 + 3 + 3 + 3") == "11"
