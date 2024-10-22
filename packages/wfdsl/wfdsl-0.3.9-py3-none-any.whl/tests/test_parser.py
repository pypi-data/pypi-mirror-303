import unittest
from unittest.mock import patch, mock_open
from pyparsing import ParseException
from dsl.parser import WorkflowParser, WorkflowGrammar

class TestWorkflowParser(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='print(2+3)')
    @patch('dsl.parser.WorkflowGrammar')
    def test_parse_file_success(self, MockGrammar, mock_file):
        mock_grammar_instance = MockGrammar.return_value
        mock_grammar_instance.program.ignore.return_value.parseFile.return_value = 'parsed_tokens'
        
        parser = WorkflowParser()
        result = parser.parse_file('dummy_file.py')
        
        self.assertEqual(result, 'parsed_tokens')
        mock_grammar_instance.program.ignore.return_value.parseFile.assert_called_once_with('dummy_file.py', parseAll=True)

    @patch('builtins.open', new_callable=mock_open, read_data='print(2+3)')
    @patch('dsl.parser.WorkflowGrammar')
    @patch('sys.exit')
    def test_parse_file_parse_exception(self, mock_exit, MockGrammar, mock_file):
        mock_grammar_instance = MockGrammar.return_value
        mock_grammar_instance.program.ignore.return_value.parseFile.side_effect = ParseException('error')
        
        parser = WorkflowParser()
        
        with patch('builtins.print') as mock_print:
            parser.parse_file('dummy_file.py')
            mock_print.assert_called_once_with(ParseException('error'))
            mock_exit.assert_called_once_with(3)

    @patch('builtins.open', new_callable=mock_open, read_data='print(2+3)')
    @patch('dsl.parser.WorkflowGrammar')
    def test_parse_file_general_exception(self, MockGrammar, mock_file):
        mock_grammar_instance = MockGrammar.return_value
        mock_grammar_instance.program.ignore.return_value.parseFile.side_effect = Exception('general error')
        
        parser = WorkflowParser()
        
        with patch('builtins.print') as mock_print:
            parser.parse_file('dummy_file.py')
            mock_print.assert_called_once_with(Exception('general error'))
            self.assertIn('general error', parser.err)

if __name__ == '__main__':
    unittest.main()