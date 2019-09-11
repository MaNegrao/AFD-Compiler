class FiniteAutomata(object):
    # default settings
    __initial_state = 0
    __error_state = -1
    __alphabet = []
    __FA = {}
    __next_state = 0

    __input_folder = 'set'

    __tokens_file = 'tokens.csv'
    __gramma_file = 'gramma.in'

    def __init__(self):
        self.mapGramma()
        self.mapTokens()

    def create_state(self, state, final=False, parents=[]):
        if not state in self.__FA:
            self.__FA[state] = {'final': final, 'parents': parents}
            self.__next_state += 1
            for char in self.__alphabet:
                self.__fa[state][char] = []
        elif not self.__fa[state]['final']:
            self.__fa[state]['final'] = final


    
    def map_gramma(self):
        try:
            file = open(self.__input_folder+'/'+self.__gramma_file, 'r')
            for gramma in file:
                # Removing unused characters
                gramma = gramma.replace('\n', '')
                state, productions = gramma.split('::=')
                productions = productions.split('|')
                state = int(state.replace('<', '').replace('>', ''))
        except:
            pass



    def map_tokens(file): 
        try:
            file = open(self.__input_folder+'/'+self.__tokens_file, 'r')
        except:

    def show(self):
        for state, value in self.__fa.items():
            print(state, '=>', value, '\n')
