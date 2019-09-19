class LexicalAnalyzer(object):
    __separators = []
    __symbol_table = []
    __token_source = []
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
        for token in self.__token_source:
            state = 0
            for char in token:
                state = self.make_transition(state, char)

            if state == -1 or not self.is_final(state):
                print("Lexical error! Token: {} State: {}", token, state)
            else:
                self.__symbol_table.append({state : })

    def output(self):
        print(self.__symbol_table)
        return self.__symbol_table