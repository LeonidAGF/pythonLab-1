from src.constants import BRACKETS, CLOSING_BRACKET, OPENING_BRACKET

def brackets_validation(expression: str):

    """
        Функция проверяющая правтльность расстановки скобок в  выражении.
        Возвращает 1 если скобки расставлены верно, противном случае 0 .
    """

    brackets: list[str] = []

    input_str = expression
    while "((" in input_str:
        input_str = input_str.replace("((", "( (")
    while "))" in input_str:
        input_str = input_str.replace("))", ") )")


    for i in range(0,len(input_str)):
        el = input_str[i]
        if el in BRACKETS:
            if el == CLOSING_BRACKET:
                if len(brackets) == 0:
                    return 0
                else:
                    if brackets[-1] == OPENING_BRACKET and input_str[i-1] not in BRACKETS:
                        brackets = brackets[0:len(brackets) - 1]
                    else:
                        return 0
            else:
                brackets.append(el)

    if len(brackets) > 0:
        return 0

    return 1
