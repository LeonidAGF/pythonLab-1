from src.count_rpn import count_rpn

def test1():
   #проверка с на простых выражениях и целых числах
   assert count_rpn("3 3 +") == "6"
   assert count_rpn("2 3 -") == "-1"
   assert count_rpn("5 5 *") == "25"
   assert count_rpn("4 2 /") == "2"
   assert count_rpn("5 3 //") == "1"
   assert count_rpn("5 3 %") == "2"
   assert count_rpn("2 2 **") == "4"

def test2():
   #проверка на простых выражениях и целых числах с добавлением скобок
   assert count_rpn("(3 3 +)") == "6"
   assert count_rpn("(2 3) -") == "-1"
   assert count_rpn("(5) (5) *") == "25"
   assert count_rpn("(4 (2)) /") == "2"
   assert count_rpn("((((((5)))))) (((3))) //") == "1"
   assert count_rpn("((5) 3) %") == "2"
   assert count_rpn("( ( ((((2))) ) ( ((((2))))) ) ) **") == "4"


def test3():
   #проверка на выражениях с несколькими операциями и скобками
   assert count_rpn("3 3 3 + +") == "9"
   assert count_rpn("1 2 3 - +") == "0"
   assert count_rpn("6 5 5 * +") == "31"
   assert count_rpn("(4 2 /) 5 *") == "10"
   assert count_rpn("(((5)) (3) //) 2 *") == "2"
   assert count_rpn("5 3 % 2 % 0 **") == "1"
   assert count_rpn("2 2 ** 0 ** 1 * 2 * 3 + 3 3 + +") == "11"

def test4():
   #проверка на выражениях с нецелыми числами и скобками
   assert count_rpn("3.5 3 3 + +") == "9.5"
   assert count_rpn("2.2 4.4 2.2 - +") == "4.4"
   assert count_rpn("6.0 5.5 2 * +") == "17"
   assert count_rpn("(3 2 /) 3 *") == "4.5"
   assert count_rpn("(((5.21)) (3) //) 2.5 * 2 *") == "5"
   assert count_rpn("5.1 3.0 % 2 % 0 **") == "1"
   assert count_rpn("2 2 ** 0 ** 1 * 2 * 3 + 3 3.3 + +") == "11.3"

def test5():
   #проверка на выражениях с унартными операциями, нецелыми числами и скобками
   assert count_rpn("1 ~-") == "-1"
   assert count_rpn("1 ~+ 2 ~+ -") == "-1"
   assert count_rpn("(1 2 -) ~-") == "1"
   assert count_rpn("(1 2 -) ~- ~- ~+ ~-") == "1"
   assert count_rpn("(1 ~- ) ~- 1 +") == "2"
   assert count_rpn("1 ~- 2 *") == "-2"
   assert count_rpn("4 ~- ~- 0.5 ~+ ~- ~+ ~- **") == "2"

def test6():
   #проверка на выражениях с нецелыми числами, скобками, унарнвми операциями, большими числами
   assert count_rpn("1 (2 3 + ~- ) *") == "-5"
   assert count_rpn("6 6 6 6 + - ~- +") == "12"
   assert count_rpn("(1 2 -) ~- 1 + 24.5 20 % 2 * 4 // +") == "4"
   assert count_rpn("(1 2 -) ~- ~- ~+ ((~-)) 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 5 * ~-") == "-150"
   assert count_rpn("(1 ~- ) ~- 1.2 + ~- ~- ~- ~- ~- ~- ~- ~- ~+ ~- ~+ ~-") == "2.2"
   assert count_rpn("(((1)) ~- 2000000 * ~-)") == "2000000"
   assert count_rpn("6 6 6 + + 7.77 7.00 7.23 + + + ~- ") == "-40"

def test7():
   #проверка на ошибочных выражениях
   count_rpn("1 2 + ()")
   count_rpn("1 2 3 ++")
   count_rpn("1 0 /")
   count_rpn("1 + 2")
   count_rpn("( 1 2 +")
   count_rpn("((( 1 2 + ))))")
   count_rpn("1 2 3 4 5 6 7 8 9 10")
