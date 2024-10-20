import unittest
import threading
from dsl.context import Context

class TestContext(unittest.TestCase):

    def setUp(self):
        self.library = "test_library"
        self.context = Context(self.library)

    def test_add_var_new_variable(self):
        self.context.add_var("test_var", 123)
        current_thread = threading.get_ident()
        self.assertTrue(self.context.symtab_stack[current_thread][-1].var_exists("test_var"))
        self.assertEqual(self.context.symtab_stack[current_thread][-1].get_var("test_var"), 123)

    def test_add_var_existing_variable(self):
        self.context.add_var("test_var", 123)
        with self.assertRaises(ValueError) as context:
            self.context.add_var("test_var", 456)
        self.assertTrue("Variable test_var already exists in the symbol table." in str(context.exception))

    def test_add_var_new_thread(self):
        def thread_function(ctx):
            ctx.add_var("thread_var", 789)
            current_thread = threading.get_ident()
            self.assertTrue(ctx.symtab_stack[current_thread][-1].var_exists("thread_var"))
            self.assertEqual(ctx.symtab_stack[current_thread][-1].get_var("thread_var"), 789)

        thread = threading.Thread(target=thread_function, args=(self.context,))
        thread.start()
        thread.join()

    def test_add_var_creates_new_symtab_stack(self):
        new_thread_id = 99999  # Simulate a new thread ID
        self.context.symtab_stack[new_thread_id] = []
        self.context.add_var("new_thread_var", 321)
        self.assertTrue(new_thread_id in self.context.symtab_stack)
        self.assertTrue(self.context.symtab_stack[new_thread_id][-1].var_exists("new_thread_var"))
        self.assertEqual(self.context.symtab_stack[new_thread_id][-1].get_var("new_thread_var"), 321)

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()