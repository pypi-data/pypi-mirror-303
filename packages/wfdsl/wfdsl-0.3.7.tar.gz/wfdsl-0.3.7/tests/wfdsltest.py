import os
import sys

# Get the path to the parent's directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the parent directory to sys.path
sys.path.insert(0, parent_dir)

from src.dsl.wftimer import Timer
from src.dsl.parser import WorkflowParser
from src.dsl.grammar import PythonGrammar
from src.dsl.interpreter import Interpreter
from src.dsl.context import Context
from src.dsl.library import LibraryBase
from src.dsl.filemgr import FileManager

if __name__ == "__main__":
    with Timer() as t:
        p = WorkflowParser(PythonGrammar())
        if len(sys.argv) > 1:
            tokens = p.parse_file(os.path.abspath(sys.argv[1]))
        else:
            #test_program_example = 'SamtoBam(2+3)'
            test_program_example = 'print(2+3)'
            tokens = p.parse(test_program_example)
        #tokens = p.grammar.assignstmt.ignore(pythonStyleComment).parseString(test_program_example)
            
        print(tokens)
        print(tokens.asXML())
        integrator = Interpreter(Context(LibraryBase(FileManager())))
       # integrator = PhenoWLCodeGenerator()
        
        #integrator.context.load_library("libraries")
        integrator.run(tokens)
    
    print(integrator.context.library)
    print(integrator.context.out)
    print(integrator.context.err)
    #print(integrator.code)


