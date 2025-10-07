from src.count_rpn import count_rpn

def main() -> None:

    """
        Точкой входа в приложение
        return: Данная функция ничего не возвращает
    """

    input1 = str(input("введите обратную польскую нотацию \n"))

    result = count_rpn(input1)

    print(result)

if __name__ == "__main__":
    main()
