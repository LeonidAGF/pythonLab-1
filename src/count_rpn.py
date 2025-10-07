from src.constants import SPELLING_ERROR, OPERATORS, UNARY_OPERAORS, UNARY_MINUS, MINUS, PLUS, MULTIPLY, DEVIDE, MODULO, \
    INTEGER_DEVIDE, EXPONENTIATION, ZERO_DIVISION_ERROR


def count_rpn(expression: str):
    """
        Считает результат обратной польской нотации.
        Возвращает строку с рузультатом если выражение написанно верно, в противном случае возвращает пустую строку.
    """

    answer = ""
    input_str = expression
    stack = input_str.split()

    if len(stack) == 0:
        print(SPELLING_ERROR)
        answer = ""
        return answer

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
                        if float(stack[pos - 1])!=0:
                            stack[pos - 2] = str(float(stack[pos - 2]) / float(stack[pos - 1]))
                        else:
                            raise ZeroDivisionError

                    elif stack[pos] == MODULO:
                        if float(stack[pos - 2])%1 == 0 or float(stack[pos - 1])%1==0:
                            stack[pos - 2] = str(float(stack[pos - 2]) % float(stack[pos - 1]))
                        elif float(stack[pos - 1]) ==0:
                            raise ZeroDivisionError
                        else:
                            raise ValueError

                    elif stack[pos] == INTEGER_DEVIDE:
                        if float(stack[pos - 2])%1 == 0 or float(stack[pos - 1])%1==0:
                            stack[pos - 2] = str(float(stack[pos - 2]) // float(stack[pos - 1]))
                        else:
                            raise ValueError

                    elif stack[pos] == EXPONENTIATION:
                        stack[pos - 2] = str(float(stack[pos - 2]) ** float(stack[pos - 1]))

                    stack = stack[0:pos - 1] + stack[pos + 1:len(stack)]
                    pos -= 2

        if float(stack[0]) % 1 == 0:
            answer = str(int(float(stack[0])))
        else:
            answer = stack[0]
    except ZeroDivisionError:
        print("\"", expression, "\"", ZERO_DIVISION_ERROR)
        answer = ""

    except Exception:
        print("\"", expression, "\"", SPELLING_ERROR)
        answer = ""
    return answer
