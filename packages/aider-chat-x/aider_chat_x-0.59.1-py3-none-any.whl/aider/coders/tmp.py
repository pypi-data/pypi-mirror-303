from cedarscript_editor import CEDARScriptEditor
from cedarscript_ast_parser import CEDARScriptASTParser
import os


cedarscript_script1 = """
-- Import the logging module:
UPDATE FUNCTION
FROM FILE "tmp.txt"
WHERE NAME = "function_name" OFFSET 1
   REPLACE SEGMENT
   STARTING AFTER LINE "print(\\"avg: \\" + avg_value)" OFFSET 2
   ENDING AT LINE "return"
   WITH CONTENT '''
@0:print("OR avg_value > 3")
@-1:return
''';
"""

xx ="""

  -- 2. Update the copied function to remove references to `self`                                                                                                         
 UPDATE FILE "refactor-benchmark/analyzer_cli_DebugAnalyzer__make_source_table/analyzer_cli.py"                                                                          
   REPLACE LINE "def _make_source_table(self, source_list, is_tf_py_library):"                                                                                           
   WITH CONTENT '''                                                                                                                                                      
 @0:def _make_source_table(source_list, is_tf_py_library):                                                                                                               
 ''';

-- 3. Update call sites of the method `_make_source_table` to call the new top-level function with the same name                                                        
 UPDATE FILE "refactor-benchmark/analyzer_cli_DebugAnalyzer__make_source_table/analyzer_cli.py"                                                                          
   REPLACE SEGMENT                                                                                                                                                       
     STARTING AFTER LINE "def list_source(self, args, screen_info=None):"                                                                                                
     ENDING BEFORE LINE "output.extend(self._make_source_table("                                                                                                         
   WITH CONTENT '''                                                                                                                                                      
 @0:output.extend(_make_source_table(                                                                                                                                    
 ''';
"""
aaa="""
 UPDATE FUNCTION
 FROM FILE "tmp.benchmarks/2024-10-04-22-59-58--CEDARScript-Gemini-small/bowling/bowling.py"
 WHERE NAME = "__init__"
INSERT BEFORE FUNCTION "inner"
 WITH CONTENT '''
 @0:print("INSERT BEFORE FUNCTION inner")
 ''';
 UPDATE FILE "tmp.benchmarks/2024-10-04-22-59-58--CEDARScript-Gemini-small/bowling/bowling.py"
 INSERT INSIDE FUNCTION "__init__" BOTTOM
 WITH CONTENT '''
 @0:print("INSIDE FUNCTION init... BOTTOM")
 ''';
 UPDATE FUNCTION
 FROM FILE "tmp.benchmarks/2024-10-04-22-59-58--CEDARScript-Gemini-small/bowling/bowling.py"
 WHERE NAME = "__init__"
 REPLACE SEGMENT
    STARTING AFTER LINE "def __init__(self):"
    ENDING AFTER LINE "def __init__(self):"
 WITH CONTENT '''
 @1:print("Line via segment")
 ''';
 UPDATE FUNCTION
 FROM FILE "tmp.benchmarks/2024-10-04-22-59-58--CEDARScript-Gemini-small/bowling/bowling.py"
 WHERE NAME = "__init__"
 REPLACE SEGMENT
    STARTING AFTER LINE "def __init__(self):"
    ENDING AFTER LINE "def __init__(self):"
 WITH CONTENT '''
 @0:print("This line will be inserted at the top 2")
 ''';
-- Update call sites to call the top-level function:
UPDATE FUNCTION
  FROM FILE "text.py"
  WHERE NAME = "fit_transform"
REPLACE LINE "X, self.stop_words_ = self._limit_features("
WITH CONTENT '''
@0:        X, self.stop_words_ = _limit_features(
''';
"""

cedarscript_script = """
UPDATE
--FUNCTION FROM
FILE "tmp.benchmarks/2024-10-04-22-59-58--CEDARScript-Gemini-small/bowling/bowling.py"
-- WHERE NAME = "inner"
-- UPDATE FILE "tmp.benchmarks/2024-10-04-22-59-58--CEDARScript-Gemini-small/bowling/bowling.py"
--DELETE LINE "pass"
--DELETE FUNCTION "inner"
--DELETE SEGMENT
--  STARTING AFTER LINE "def inner(a: int):"
--  ENDING AT LINE "pass #"
INSERT INSIDE FUNCTION "__init__" TOP
WITH FUNCTION "roll" RELATIVE INDENTATION 0
--WITH CONTENT '''@0:print("INSERT INSIDE FUNCTION inner @@")''';


UPDATE FUNCTION "_make_source_table"                                                                                                                                    
FROM FILE "refactor-benchmark/analyzer_cli_DebugAnalyzer__make_source_table/analyzer_cli.py"                                                                          
REPLACE LINE "    if is_tf_py_library:" WITH CONTENT '''                                                                                                                
@0:  if is_tf_py_library:                                                                                                                                               
''';                                                                                                                                                                    
UPDATE FUNCTION "list_source"                                                                                                                                           
FROM FILE "refactor-benchmark/analyzer_cli_DebugAnalyzer__make_source_table/analyzer_cli.py"                                                                          
REPLACE LINE "    output.extend(self._make_source_table(" WITH CONTENT '''                                                                                              
@0:    output.extend(_make_source_table(                                                                                                                                
''';                                                                                                                                                                    
UPDATE FUNCTION "_make_source_table"                                                                                                                                    
FROM FILE "refactor-benchmark/analyzer_cli_DebugAnalyzer__make_source_table/analyzer_cli.py"                                                                          
MOVE WHOLE                                                                                                                                                              
INSERT BEFORE LINE "class DebugAnalyzer(object):"                                                                                                                       
RELATIVE INDENTATION 0;                                                                                                                                               
"""

cedarscript_script="""
 -- 1. Move the `parse_output` method from the `PylintWidget` class, placing it at the top level, just before the line where its class starts                            
 UPDATE FUNCTION "parse_output"                                                                                                                                          
 FROM FILE "main_widget_PylintWidget_parse_output/main_widget.py"                                                                                                                                              
 MOVE WHOLE                                                                                                                                                              
 INSERT BEFORE LINE "class PylintWidget(PluginMainWidget):"                                                                                                              
 RELATIVE INDENTATION 0;                                                                                                                                                 
 """

basedir="/Users/elifarley.callado/Documents/GitHub/refactor-benchmark/refactor-benchmark/galaxy_GalaxyCLI_execute_list_collection"
basedir="/Users/elifarley.callado/Documents/GitHub/aider/tmp.benchmarks/2024-10-03-01-09-32--CEDARScript-test-4/pig-latin"
basedir="/Users/elifarley.callado/Documents/GitHub/refactor-benchmark/refactor-benchmark/grad_scaler_GradScaler__unscale_grads_"
basedir="/Users/elifarley.callado/Documents/GitHub/refactor-benchmark/refactor-benchmark/text_CountVectorizer__limit_features"
basedir="/Users/elifarley.callado/Documents/GitHub/aider"
basedir="/Users/elifarley.callado/Documents/GitHub/refactor-benchmark/refactor-benchmark"

# file = "refactor-benchmark/analyzer_cli_DebugAnalyzer__make_source_table/analyzer_cli.py"
os.chdir(basedir)
cedarscript_parser = CEDARScriptASTParser()
cedarscript_editor = CEDARScriptEditor(basedir)
parsed_commands, parse_errors = cedarscript_parser.parse_script(cedarscript_script)

for e in parse_errors:
    print(f"### {e}")
if parse_errors:
    exit(1)

for cmd in parsed_commands:
    print(cmd)
print(f'> { str(cedarscript_editor.apply_commands(parsed_commands)) }')
