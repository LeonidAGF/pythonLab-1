from src.constants import OPENING_BRACKET, MULTIPLY, MINUS, PLUS, DEVIDE, MODULO, EXPONENTIATION, INTEGER_DEVIDE, \
    UNARY_MINUS, UNARY_PLUS, CLOSING_BRACKET


def is_number(input_str: str):
    """
            Проверка являетс ли строка поданная на вход числом
            Функция возращает 0 если строка не число и 1 если число
    """

    res = 1
    try:
        float(input_str)
    except Exception:
        res = 0
    return res


def rpn_parse(tokens: list[str]) -> list[str]:
    """
            Получает на вход инфиксное выражение в виде массива токенов и преобразует его в обратную польскую нотацию
            Возвращает обратную польскую нотацию в виде массива токенов
    """

    stack: list[str] = []
    operators: list[str] = []
    operators_before_bracket: list[str] = []

    open_brackets_count = 0
    open_bracket_in_len = 0
    last = ""

    for i in range(0, len(tokens)):
        el = tokens[i]
        if open_brackets_count > 0:
            open_bracket_in_len += 1

        if el == OPENING_BRACKET:
            open_bracket_in_len = 1
            open_brackets_count = open_brackets_count + 1
            operators_before_bracket = operators + operators_before_bracket
            operators = []
            if last not in " " + PLUS + MINUS + OPENING_BRACKET + MULTIPLY + DEVIDE + MODULO + EXPONENTIATION + INTEGER_DEVIDE + UNARY_MINUS + UNARY_PLUS:  # " +-(*/%^//~$"
                raise Exception

        elif el == CLOSING_BRACKET:
            open_brackets_count -= 1
            if open_brackets_count == 0:
                operators += operators_before_bracket
                stack += operators
                operators = []
                operators_before_bracket = []
            else:
                stack += operators
                operators = []

            if open_brackets_count < 0 or open_bracket_in_len == 2 or last in " " + PLUS + MINUS + OPENING_BRACKET + MULTIPLY + DEVIDE + MODULO + EXPONENTIATION + INTEGER_DEVIDE + UNARY_MINUS + UNARY_PLUS:  # " +-(*/%^//~$"
                raise Exception
        elif is_number(el):
            stack.append(el)
        elif el in MULTIPLY + DEVIDE + MODULO + EXPONENTIATION + INTEGER_DEVIDE:  # "*/%^//"

            if EXPONENTIATION in operators and el != EXPONENTIATION:
                stack += operators
                operators = []

            operators = [el] + operators

            if last not in " " + CLOSING_BRACKET and not is_number(last) and len(tokens) - 1 == i:
                raise Exception
        elif el in UNARY_MINUS + UNARY_PLUS:
            operators = [el] + operators
            if last == CLOSING_BRACKET or is_number(last):
                raise Exception
        elif el in PLUS + MINUS:
            if MULTIPLY in operators or DEVIDE in operators or MODULO in operators or EXPONENTIATION in operators or INTEGER_DEVIDE in operators or UNARY_MINUS in operators or UNARY_PLUS in operators:
                stack += operators
                operators = []
            operators.append(el)
            if last in " " + PLUS + MINUS + OPENING_BRACKET + MULTIPLY + DEVIDE + MODULO + EXPONENTIATION + INTEGER_DEVIDE + UNARY_MINUS + UNARY_PLUS or len(
                    tokens) - 1 == i:  # " +-(*/%^//~$"
                raise Exception
        else:
            raise Exception
        last = el
    stack += operators

    if open_brackets_count > 0:
        raise Exception

    return stack
