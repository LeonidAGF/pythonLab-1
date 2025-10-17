from src.count_rpn import count_rpn


def test_function_count_rpn():
    # проверка count_rpn на правильный подсчёт обратной польской нотации
    assert count_rpn("1 2 3 4 5 6 7 8 9 + - + - * / / +".split()) == "25"
    assert count_rpn("6 + 6 - 6 + 6".split()) == ""
    assert count_rpn("1 2 + 6 ~ *".split()) == "-18"
    assert count_rpn("2 0 ^ 1 %".split()) == "0"
    assert count_rpn("1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +".split()) == "35"
    assert count_rpn("1000000000 99999999 +".split()) == "1099999999"
    assert count_rpn("40 $ 1 + ~ ~ ~".split()) == "-41"
