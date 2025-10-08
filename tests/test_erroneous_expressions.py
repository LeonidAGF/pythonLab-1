from src.processing_rpn import processing_rpn

def test_erroneous_expressions():
   #проверка на ошибочных выражениях
   assert processing_rpn("(1 2) +")==""
   assert processing_rpn("1 2 3 ++")==""
   assert processing_rpn("1 0 /")==""
   assert processing_rpn("1 + 2")==""
   assert processing_rpn("( 1 2 +")==""
   assert processing_rpn("((( 1 2 + ))))")==""
   assert processing_rpn("1 2 3 4 5 6 7 8 9 10")==""
