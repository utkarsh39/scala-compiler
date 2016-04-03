#symbolTable is a dictionary of lists. Name and type
class Env:
    tablecount = 1
    def _init_(self, prev_env = None):
        self.table = {}
        self.code = []
        self.id = tablecount
        tablecount += 1
        self.parent = prev_env
        self.childlist = []

        if(prev_env != None):
            prev_env.childlist.append(self.id)

    def add_entry(self, name, type):
         if name in self.table:
            print 'Error: Entry already present - ( ' + name + ' )'
	    assert(False)
        else:
            self.table[name]= []
            self.table[name].append(name)
            self.table[name].append(type)

    def present(self, name):
        if name in self.table:
            return True
        else:
            return False

    def update_entry(self, name, key, updated_entry):
        try:
            self.table[name][key] = updated_entry
            return True
        except:
            return False

    
