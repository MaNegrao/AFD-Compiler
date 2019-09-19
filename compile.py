from src.LexicalAnalyzer import LexicalAnalyzer
from src.FiniteAutomata import FiniteAutomata

# FiniteAutomata()
fa = FiniteAutomata().output()

# LexicalAnalyzer(fa)
symbol_table = LexicalAnalyzer(fa).output()

if symbol_table is None:
    print('\nAborted!')