from src.processing_rpn import processing_rpn

def main() -> None:

    """
        Точкой входа в приложение
        return: Данная функция ничего не возвращает
    """

    input1 = str(input("введите обратную польскую нотацию \n"))

    result = processing_rpn(input1)

    print(result)

if __name__ == "__main__":
    main()
