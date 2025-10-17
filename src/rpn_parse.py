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


def rpn_parse(tokens: list[str]):

    """
            Получает на вход инфиксное выражение в виде массива токенов и преобразует его в обратную польскую нотацию
            Возвращает обратную польскую нотацию в виде массива токенов
    """

    stack: list[str] = []
    operators: list[str] = []
    operators_before_bracket: list[str] = []

    open = 0
    openlen = 0
    last = ""

    for i in range(0,len(tokens)):
        el = tokens[i]
        if open>0:
            openlen+=1

        if el == "(":
            openlen = 1
            open = open + 1
            operators_before_bracket = operators+operators_before_bracket
            operators = []
            if last not in " +-(*/%^//~$":
                raise Exception

        elif el == ")":
            open -= 1
            if open==0:
                operators += operators_before_bracket
                stack += operators
                operators = []
                operators_before_bracket = []
            else:
                stack += operators
                operators = []

            if open < 0 or openlen==2 or last in " +-(*/%^//~$":
                raise Exception
        elif is_number(el):
            stack.append(el)
        elif el in "*/%^//":

            operators = [el] + operators

            if last not in " )" and not is_number(last) and len(tokens)-1==i:
                raise Exception
        elif el in "~$":
            operators = [el] + operators
            if last == ")" or is_number(last):
                raise Exception
        elif el in "+-":
            if "*" in operators or "/" in operators or "%" in operators or "^" in operators or "//" in operators or "~" in operators or "$" in operators:
                stack += operators
                operators = []
            operators.append(el)
            if last in " (+-(*/%^//~$" or len(tokens)-1==i:
                raise Exception
        else:
            raise Exception
        last =el

    stack += operators

    if open>0:
        raise Exception

    #print(stack)
    return stack
