import threading
from .symtab import SymbolTable

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
        self.SymbolTableCls = SymbolTableCls # custom symbol table from the client
        self.lock = threading.Lock()
        self.reload()
            
    def reload(self):
        '''
        Reinitializes this object for new processing.
        '''
        self.out = []
        self.err = []
        self.dci = []
        self.globals = {}
        self.symtabs = [self.SymbolTableCls()]
        
    def get_var(self, name):
        '''
        Gets a variable from symbol stack and symbol table
        :param name:
        '''
        for s in reversed(self.symtabs):
            if s.var_exists(name):
                return s.get_var(name)
    
    def add_var(self, name, value):
        if self.var_exists(name):
            raise ValueError(f"Variable {name} already exists in the symbol table.")
        with self.lock:
            return self.symtabs[-1].add_var(name, value)

            
    def update_var(self, name, value):
        with self.lock:
            for s in reversed(self.symtabs):
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
        for s in reversed(self.symtabs):
            if s.var_exists(name):
                return True
    
    def append_local_symtab(self):
        '''
        Appends a new symbol table to the symbol table stack.
        '''
        with self.lock:
            self.symtabs.append(self.SymbolTableCls())
            return self.symtabs[-1]
    
    def pop_local_symtab(self):
        '''
        Pop a symbol table from the symbol table stack.
        '''
        with self.lock:
            self.symtabs.pop()
        
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