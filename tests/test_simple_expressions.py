from src.processing_rpn import processing_rpn

def test_simple_expressions():
   #проверка на простых выражениях и целых числах
   assert processing_rpn("3 + 3") == "6"
   assert processing_rpn("2 - 3") == "-1"
   assert processing_rpn("5 * 5") == "25"
   assert processing_rpn("4 / 2") == "2"
   assert processing_rpn("5 // 3") == "1"
   assert processing_rpn("5 % 3") == "2"
   assert processing_rpn("2 ^ 2 ") == "4"
