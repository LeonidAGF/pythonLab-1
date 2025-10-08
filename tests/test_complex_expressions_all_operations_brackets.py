from src.processing_rpn import processing_rpn

def test_complex_expressions_all_operations_brackets():
   #проверка на выражениях с нецелыми числами, скобками, унарнвми операциями, большими числами
   assert processing_rpn("1 (2 3 + ~- ) *") == "-5"
   assert processing_rpn("6 6 6 6 + - ~- +") == "12"
   assert processing_rpn("(1 2 -) ~- 1 + 24.5 20 - 2 * 4 // +") == "4"
   assert processing_rpn("(1 2 -) ~- ~- ~+ ~- 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 5 * ~-") == "-150"
   assert processing_rpn("(1 ~- ) ~- 1.2 + ~- ~- ~- ~- ~- ~- ~- ~- ~+ ~- ~+ ~-") == "2.2"
   assert processing_rpn("(((1)) ~- 2000000 * ~-)") == "2000000"
   assert processing_rpn("6 6 6 + + 7.77 7.00 7.23 + + + ~- ") == "-40"
