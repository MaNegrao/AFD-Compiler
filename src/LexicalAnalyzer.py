class LexicalAnalyzer(object):
    __separators = []
    __symbol_table = []
    __token_source = []

    __separators_file = 'separators.in'
    __source_code_file = 'code.in'

    def __init__ (self, fa):
        self.read_separators()
        self.read_source()

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
                    #print(self.__token_source)
        except:
            print('Read Error: Source Code')
            pass
