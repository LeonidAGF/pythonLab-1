from src.constants import BRACKETS, CLOSING_BRACKET, OPENING_BRACKET
from src.count_rpn import count_rpn


def brackets_validation(expression: str):

    """
        Функция проверяющая правтльность расстановки скобок в  выражении.
        Возвращает 1 если скобки расставлены верно, противном случае 0 .
    """

    brackets: list[str] = []
    open_bracket_pos: list[int] = []

    input_str: str = expression
    while "( (" in input_str:
        input_str = input_str.replace("( (", "((")
    while ") )" in input_str:
        input_str = input_str.replace(") )", "))")

    for i in range(0,len(input_str)):
        el: str = input_str[i]
        if el in BRACKETS:
            if el == CLOSING_BRACKET:
                if len(brackets) == 0:
                    return 0
                elif brackets[-1] == OPENING_BRACKET and count_rpn(input_str[open_bracket_pos[-1]+1:i].replace("(","").replace(")","")) != "":
                    brackets = brackets[0:len(brackets) - 1]
                    open_bracket_pos = open_bracket_pos[0:len(open_bracket_pos)-1]
                else:
                    return 0
            else:
                brackets.append(el)
                open_bracket_pos.append(i)

    if len(brackets) > 0:
        return 0

    return 1
