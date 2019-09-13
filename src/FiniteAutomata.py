class FiniteAutomata(object):
    # default settings
    __initial_state = 0
    __error_state = -1
    __alphabet = []
    __fa = {}
    __next_new_state = 0
    #config folders and files
    __input_folder = 'set'
    __tokens_file = 'tokens.in'
    __gramma_file = 'gramma.in'

    def __init__(self):
        #mapping transitions
        self.map_gramma()
        self.map_tokens()
        #determinize FA
        self.determinize()
        self.show()

    def find_state(self, state=None):
        if state is None:
            state = self.__next_new_state 
        else:
            state += 1
        try:
            while self.__fa[state]['final']:
                state += 1
        except:
            pass
        return state

    def append_char(self, char):
        if not char in self.__alphabet:
            self.__alphabet.append(char)
            for state in self.__fa:
                self.__fa[state][char] = []

    def create_state(self, state, final=False, parents=[]):
        if not state in self.__fa:
            self.__fa[state] = {'final': final, 'parents': parents}
            self.__next_new_state += 1
            for char in self.__alphabet:
                self.__fa[state][char] = []

        elif not self.__fa[state]['final']:
            self.__fa[state]['final'] = final

    def create_transition(self, state, char, next_state):
        if type(self.__fa[state][char]) == list:
            if next_state not in self.__fa[state][char]:
                self.__fa[state][char].append(next_state)
    
    def map_gramma(self):
        try:
            file = open(self.__input_folder+'/'+self.__gramma_file, 'r')
            for gramma in file:
                # Removing unused characters
                gramma = gramma.replace('\n', '')
                state, productions = gramma.split('::=')
                productions = productions.split('|')
                state = int(state.replace('<', '').replace('>', ''))
                
                self.create_state(state)

                for prod in productions:
                    char = ''
                    next_state = None
                    is_char = True

                    for c in prod:
                        if c == '<' and is_char:
                            next_state = c
                            is_char = False
                        elif c == '>' and not is_char:
                            next_state += c
                            is_char = True
                        elif not is_char:
                            next_state += c
                        else:
                            char = c
                    self.append_char(char)

                    if next_state:
                        next_state = int(next_state.replace('<', '').replace('>', ''))
                        self.create_state(next_state)
                        self.create_transition(state, char, next_state)
                    else:
                        self.__fa[state]['final'] = True
        except:
            pass

    def map_tokens(self): 
        try:
            file = open(self.__input_folder+'/'+self.__tokens_file, 'r')
            for token in file:    
                token = token.replace('\n', '')
                token_len = len(token)
                state = self.__initial_state
                for i in range(token_len):
                    char = token[i]
                    self.append_char(char)
                    self.create_state(state)
                    
                    next_state = None

                    if i < token_len-1:
                        next_state = self.find_state(state)
                        self.create_state(next_state)
                    else:
                        next_state = self.find_state()
                        self.create_state(next_state, True)
                    
                    self.create_transition(state, char, next_state)
                    state = next_state
        except:
            print("deu erro ai irmão")
            pass

    def merge_states(self, state, next_state):
        if self.__fa[next_state]['final']:
            self.__fa[state]['final'] = True
        
        for char in self.__alphabet:
            states = self.__fa[next_state][char]
            if type(states) is list:
                for s in states:
                    self.create_transition(state, char, s)
            elif type(states) is int:
                self.create_transition(state, char, states)

    def find_state_by_parents(self, parents):
        for state in self.__fa:
            if self.__fa[state]['parents'] == parents:
                return state

    def determinize_state(self, state):
        for char in self.__alphabet:
            next_states = self.__fa[state][char]
            if type(next_states) == list:
                #if the transtion has only one state, keep this one
                if len(next_states) == 1:
                    self.__fa[state][char] = next_states[0]
                elif len(next_states) == 0:
                    self.__fa[state][char] = None
                else:
                    parents = []
                    for next_state in next_states:
                        if next_state not in parents:
                            parents.append(next_state)
                    new_state = self.find_state_by_parents(parents)
                    if new_state is not None:
                        self.__fa[state][char] = new_state
                    else:
                        new_state = self.find_state()
                        self.__fa[state][char] = new_state
                        self.create_state(new_state, parents=parents)
                        for next_state in next_states:
                            self.merge_states(new_state, next_state)
                        self.determinize_state(new_state)

    def determinize(self):
        fa = self.__fa.copy()
        for state in fa:
            self.determinize_state(state)

    


    def show(self):
        for state, value in self.__fa.items():
            print(state, '=>', value, '\n')
