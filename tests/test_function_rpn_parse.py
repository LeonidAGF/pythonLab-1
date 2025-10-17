from src.rpn_parse import rpn_parse


def test_function_rpn_parse():
    # проверка rpn_parse на правильное преобразование инфиксного выражения в rpn
    assert rpn_parse("1 + 2".split()) == "1 2 +".split()
    assert rpn_parse("6 + 6 + ~ 6 + 6".split()) == "6 6 6 ~ + + 6 +".split()
    assert rpn_parse("1 + 2 + 6 * 3".split()) == "1 2 6 3 * + +".split()
    assert rpn_parse("2 ^ 0 * 3".split()) == "2 0 ^ 3 *".split()
    assert rpn_parse("".split()) == "".split()
    assert rpn_parse("1000000000 + 99999999".split()) == "1000000000 99999999 +".split()
    assert rpn_parse("~ ~ ~ ( 1 ) + 2".split()) == "1 ~ ~ ~ 2 +".split()
