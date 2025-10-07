import sys
from src.brackets_validation import brackets_validation
from src.constants import SPELLING_ERROR, OPERATORS, UNARY_OPERAORS, UNARY_MINUS, MINUS, PLUS, MULTIPLY, DEVIDE, MODULO, \
    INTEGER_DEVIDE, EXPONENTIATION, BRACKETS_ERROR, OPENING_BRACKET, CLOSING_BRACKET

def count_rpn(expression: str):

    """
        Считает результат обратной польской нотации.
        Возвращает строку с рузультатом если выражение написанно верно, в противном случае возвращает пустую строку.
    """

    answer = ""
    input_str = expression
    if brackets_validation(input_str)==0:
        print("\"",expression,"\"",BRACKETS_ERROR)
        return ""

    input_str = input_str.replace(OPENING_BRACKET, "")
    input_str = input_str.replace(CLOSING_BRACKET, "")

    while "  " in input_str:
        input_str = input_str.replace("  ", " ")

    stack = input_str.split()

    if len(stack) == 0:
        print(SPELLING_ERROR)
        sys.exit()

    pos = 0

    try:
        while len(stack) > 1:
            pos += 1
            if stack[pos] in OPERATORS:
                if stack[pos] in UNARY_OPERAORS:
                    if stack[pos] == UNARY_MINUS:
                        stack[pos - 1] = str(-float(stack[pos - 1]))
                    stack = stack[0:pos] + stack[pos + 1:len(stack)]
                    pos -= 1
                else:

                    if stack[pos] == PLUS:
                        stack[pos - 2] = str(float(stack[pos - 2]) + float(stack[pos - 1]))

                    elif stack[pos] == MINUS:
                        stack[pos - 2] = str(float(stack[pos - 2]) - float(stack[pos - 1]))

                    elif stack[pos] == MULTIPLY:
                        stack[pos - 2] = str(float(stack[pos - 2]) * float(stack[pos - 1]))

                    elif stack[pos] == DEVIDE:
                        stack[pos - 2] = str(float(stack[pos - 2]) / float(stack[pos - 1]))

                    elif stack[pos] == MODULO:
                        stack[pos - 2] = str(float(stack[pos - 2]) % float(stack[pos - 1]))

                    elif stack[pos] == INTEGER_DEVIDE:
                        stack[pos - 2] = str(float(stack[pos - 2]) // float(stack[pos - 1]))

                    elif stack[pos] == EXPONENTIATION:
                        stack[pos - 2] = str(float(stack[pos - 2]) ** float(stack[pos - 1]))

                    stack = stack[0:pos - 1] + stack[pos + 1:len(stack)]
                    pos -= 2

        if float(stack[0]) % 1 == 0:
            answer = str(int(float(stack[0])))
        else:
            answer = stack[0]

    except Exception:
        print("\"",expression,"\"", SPELLING_ERROR)
        answer = ""
    return answer
