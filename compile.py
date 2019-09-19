from src.LexicalAnalyzer import LexicalAnalyzer
from src.FiniteAutomata import FiniteAutomata

fa = FiniteAutomata()
symbol_table = LexicalAnalyzer(fa)
if symbol_table is None:
    print('\nAborted!')