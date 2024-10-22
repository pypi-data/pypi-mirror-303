import threading
from dsl.symtab import SymbolTable

class Context:
    '''
    The context for parsing and interpretation.
    '''
    def __init__(self, library, SymbolTableCls=SymbolTable):
        '''
        Initializes this object.
        '''
        self.library = library
        self.runnable = None
        self.user_id = None
        self.SymbolTableCls = SymbolTableCls # custom symbol table from the client
        self.lock = threading.Lock()
        self.reload()
            
    def reload(self):
        """

        This method resets the following attributes:
        - symtab_stack: Dictionary to store symbol tables.
        - out: List to store output messages.
        - err: List to store error messages.
        - dci: List to store data context information.
        - globals: Dictionary to store global variables.
        - ident: Thread identifier obtained from threading.get_ident().
        - symtabs: List containing a new instance of SymbolTableCls, thread-specific symbol tables.
        """
        '''
        Reinitializes this object for new processing.
        '''
        self.out = []
        self.err = []
        self.dci = []
        self.globals = {}
        self.symtab_stack = {threading.get_ident(): [self.SymbolTableCls()]} # {thread_id: [SymbolTableCls(), SymbolTableCls()]}
        
    def get_var(self, name):
        '''
        Gets a variable from symbol stack and symbol table
        :param name:
        '''
        if not self.var_exists(name):
            raise ValueError(f"Variable {name} does not exist in the symbol table.")

        current_thread = threading.get_ident()
        with self.lock:
            if current_thread in self.symtab_stack:
                for s in reversed(self.symtab_stack[current_thread]):
                    if s.var_exists(name):
                        return s.get_var(name)        
    
    def add_var(self, name, value):
        """
        Adds a variable to the symbol table.
        If the variable already exists, it updates the variable with the new value.
        If the current thread matches the main thread, it adds the variable to the last symbol table in the stack.
        If the current thread does not have a symbol table stack, it creates one and adds the variable to the new symbol table.
        Args:
            name (str): The name of the variable to add.
            value (Any): The value of the variable to add.
        Returns:
            Any: The result of adding or updating the variable in the symbol table.
        """
        if self.var_exists(name):
            raise ValueError(f"Variable {name} already exists in the symbol table.")

        # if the current thread is the main thread
        current_thread = threading.get_ident()

        with self.lock:
            if not current_thread in self.symtab_stack:
                self.symtab_stack[current_thread] = [self.SymbolTableCls()]
            return self.symtab_stack[current_thread][-1].add_var(name, value)
            
    def update_var(self, name, value):
        """
        Update the value of a variable in the symbol table.

        This method searches for the variable in the symbol tables associated with the current thread.
        If the variable is found, its value is updated. The search is performed in reverse order of the symbol tables.

        Args:
            name (str): The name of the variable to update.
            value: The new value to assign to the variable.

        Returns:
            The result of the update operation from the symbol table, if the variable is found.
            Otherwise, returns None.
        """
        if not self.var_exists(name):
            raise ValueError(f"Variable {name} does not exist in the symbol table.")

        current_thread = threading.get_ident()

        with self.lock:
            if current_thread in self.symtab_stack:
                for s in reversed(self.symtab_stack[current_thread]):
                    if s.var_exists(name):
                        return s.update_var(name, value)
    
    def add_or_update_var(self, name, value):
        if self.var_exists(name):
            return self.update_var(name, value)
        else:
            return self.add_var(name, value)
                                
    def var_exists(self, name):
        '''
        Checks if a variable exists in any of the symbol tables.
        :param name: variable name
        '''
        current_thread = threading.get_ident()
        if current_thread in self.symtab_stack:
            for s in reversed(self.symtab_stack[current_thread]):
                if s.var_exists(name):
                    return True
    
    def append_local_symtab(self):
        '''
        Appends a new symbol table to the symbol table stack.
        '''
        with self.lock:
            current_thread = threading.get_ident()
            if current_thread in self.symtab_stack: # if current thread exists in the symbol table stack, append a new symbol table at the end
                self.symtab_stack[current_thread].append(self.SymbolTableCls())
            else: # otherwise, create a new symbol table stack
                self.symtab_stack[current_thread] = [self.SymbolTableCls()]
            return self.symtab_stack[current_thread][len(self.symtab_stack[current_thread]) - 1]
    
    def pop_local_symtab(self):
        '''
        Pop a symbol table from the symbol table stack.
        '''
        with self.lock:
            current_thread = threading.get_ident()
            if current_thread in self.symtab_stack:
                if self.symtab_stack[current_thread]:
                    self.symtab_stack[current_thread].pop()
                    if not self.symtab_stack[current_thread]: # no symbol table, remove the entry
                        del self.symtab_stack[current_thread]
        
    @property
    def library(self):
        return self.__library
    
    @library.setter
    def library(self, lib):
        self.__library = lib
        
    @property
    def runnable(self):
        return self.__runnable
    
    @runnable.setter
    def runnable(self, runnable):
        self.__runnable = runnable
                      
    def iequal(self, str1, str2):
        '''
        Compares two strings for case insensitive equality.
        :param str1:
        :param str2:
        '''
        if str1 == None:
            return str2 == None
        if str2 == None:
            return str1 == None
        return str1.lower() == str2.lower()
    
    def write(self, *args):
        '''
        Writes a line of strings in out context.
        '''
        self.out.append("{0}".format(', '.join(map(str, args))))
    
    def error(self, *args):
        '''
        Writes a line of strings in err context.
        '''
        self.err.append("{0}".format(', '.join(map(str, args))))

    def append_dci(self, server, user, password):
        self.dci.append([server, user, password])
    
    def pop_dci(self):
        if self.dci:
            return self.dci.pop()
    
    def get_activedci(self):
        if not self.dci:
            return [None, None, None]
        return self.dci[-1]