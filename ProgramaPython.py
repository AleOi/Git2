# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

class animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __add__(self, animal2):
        self.idade = animal2.idade
C1 = animal("Poodle", 12) 
C2 = animal("Rusky", 22) 
C1 + C2
print(C1.idade)
