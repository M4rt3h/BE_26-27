import subprocess
import sys

# Installe la bibliothèque SymPy
subprocess.check_call([sys.executable, "-m", "pip", "install", "sympy"])

# Vous pouvez maintenant l'importer
import sympy as sp

#Lib de calcul algébrique


l1, l3, l4, l6 = 375, 400, 450, 70
c1 = sp.Symbol("c1")
c2 = sp.Symbol("c2")
c3 = sp.Symbol("c3")
c4 = sp.Symbol("c4")
c5 = sp.Symbol("c5")
c6 = sp.Symbol("c6")
print("hello")
print(c1)