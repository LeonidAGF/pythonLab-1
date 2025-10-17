from src.processing_rpn import processing_rpn

def test_unary_non_integer_brackets():
   #проверка на выражениях с унартными операциями, нецелыми числами и скобками
   assert processing_rpn("~1 ") == "-1"
   assert processing_rpn("$1 - $2") == "-1"
   assert processing_rpn("~(1 - 2)") == "1"
   assert processing_rpn("~$~~(1 - 2)") == "1"
   assert processing_rpn("(~1 )+ ~1") == "-2"
   assert processing_rpn("~1 * 2") == "-2"
   assert processing_rpn("~~4 ^ ~$~$0.5") == "2"
