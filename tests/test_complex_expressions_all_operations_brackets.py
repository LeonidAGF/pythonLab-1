from src.processing_rpn import processing_rpn


def test_complex_expressions_all_operations_brackets():
    # проверка на выражениях с нецелыми числами, скобками, унарнвми операциями, большими числами
    assert processing_rpn("1 * ~(2 + 3) + 5") == "0"
    assert processing_rpn("6 + 6 - 6 + 6 - 6 - 6 + 6 - 6") == "0"
    assert processing_rpn("~(1000-2)*2-999%1+1996") == "0"
    assert processing_rpn("(~1500000+1)^2") == "2249997000001"
    assert processing_rpn("1+1+1+1+1+1+1+1+1+1+1+1-2-2-2-2-(2-~(2))-2-2-(2-2)-2-2-2+10") == "0"
    assert processing_rpn("2000000.0*(~1^0)*((~10000)^0)-2000000") == "0"
    assert processing_rpn("$~~(((~8+7))+40)-(~(~39.0))") == "0"
