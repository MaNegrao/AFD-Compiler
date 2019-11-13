class LexicalAnalyzer(object):
    __separators = []
    __symbol_table = []
    __token_source = []
    __source_code = None
    __out = []
    __fa = {}

    __separators_file = 'separators.in'
    __source_code_file = 'code.in'
    __fa_file = 'fa.in'

    def __init__ (self, fa):
        self.__fa = fa

        self.read_separators()
        self.read_source()
        self.analyze()

    def is_final(self, state):
        try:
            final = self.__fa[state]['final']
        except KeyError:
            final = False
        return final

    def read_separators(self):
        try:
            file = open('set/'+self.__separators_file, 'r')
            for separator in file:
                separator = separator.replace('\n', '')
                self.__separators.append(separator)
            file.close()
        except:
            print('Read Error: Separators!')
            pass

    def read_source(self):
        try:
            file = open('src/'+self.__source_code_file, 'r')
            lines = file.read().splitlines()
            self.__source_code = lines
            lines = list(filter(lambda a: a != '', lines))
            file.close()
            for token in lines: 
                for char in token:
                    if char in self.__separators:
                        token = token.replace(char, ' '+char+' ')
                token = token.strip().split(' ')
                for char in token:
                    if char != '':
                        self.__token_source.append(char)
        except:
            print('Read Error: Source Code')
            pass

    def make_transition(self,state, char):
        try:
            return self.__fa[state][char]
        except KeyError:
            return -1 

    def analyze(self):
        initial_state = 0
        error_state = -1
        line_count = 0
        token = ''
        state = initial_state
        
        for line in self.__source_code:
            if '\n' not in line:
                line += '\n'
            line_count += 1
            identate = True
            identation = 0
            # Reading chars
            for i in range(len(line)):
                char = line[i]
                # Getting identation
                if identate:
                    if char != '\t':
                        identate = False
                    elif identate:
                        identation += 1
                # Making the transition if the char is not a separator
                if char not in self.__separators:
                    token += char
                    state = self.make_transition(state, char)
                # Handling the readed token
                elif token != '':
                    # Changing to error state if the token state is not final
                    if not self.is_final(state):
                        state = error_state
                    # Appending token to the output tape if it is recognized
                    else:
                        self.__out += token
                    # Appending token to the symbol table
                    self.__symbol_table.append({
                        'line': line_count,
                        'column': i,
                        'identation': identation,
                        'state': state,
                        'tag': token
                    })
                    # Showing error message if necessary
                    if state == error_state:
                        print('Lexical IsFinalerror: "%s" in line %d:%d' %(token, line_count, i))
                    # Reseting token and state
                    token = ''
                    state = initial_state
        
        for token in self.__token_source:
            state = 0
            for char in token:
                state = self.make_transition(state, char)

            if state == -1 or not self.is_final(state):
                print("Lexical error! Token: {} State: {}", token, state)
            else:
                self.__symbol_table.append({state : None})

    def output(self):
        print(self.__out)
        return self.__symbol_table