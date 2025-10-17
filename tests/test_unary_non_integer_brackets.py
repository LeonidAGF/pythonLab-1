from src.processing_rpn import processing_rpn


def test_unary_non_integer_brackets():
    # проверка на выражениях с унартными операциями, нецелыми числами и скобками
    assert processing_rpn("~1.5*2 ") == "-3"
    assert processing_rpn("$1 - $2.4") == "-1.4"
    assert processing_rpn("~(1.11111 - 2.11111)") == "1"
    assert processing_rpn("~$~~(1 - 2)") == "1"
    assert processing_rpn("(~1 )+ ~1") == "-2"
    assert processing_rpn("3.33 + ~( ~ 1.11 - 1.11*2)") == "6.66"
    assert processing_rpn("~~4 ^ ~$~$0.5") == "2"
