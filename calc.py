#permet a la calculette de définir la méthode
import os
from addition import calcule_addition 
from soustraction import calcule_soustraction
from multiplication import calcule_multiplication
from division import calcule_division

a = int(input())
calcul = input()
b = int(input())

if calcul =="+" : 
    a = calcule_addition (a,b)

if calcul =="-":
    a = calcule_soustraction (a,b)

if calcul =="*":
    a = calcule_multiplication (a,b)
if calcul =="/":
    a=  calcule_division (a,b)

    






