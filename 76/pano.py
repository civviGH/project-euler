#!/usr/bin/env python3

from aux import *
import sys
from copy import deepcopy

"""beispiel fuer 7

Startwert fest erzeugen
1 1 1 1 1 1 1
2 1 1 1 1 1
3 1 1 1 1
4 1 1 1
5 1 1
6 1

Starte Rekursion

R: 1
iteriere jeden wert aus vorheriger rekursion
fuer jeden wert, inkrementiere solange wert[R] bis kaputt
1 2 X
2 2 1 1 1
2 3 X
3 2 1 1
3 3 1 
3 4 X
4 2 1 
4 3 -> kein wert mehr rechts neben uns: R++

R: 2
2 2 2 1
2 2 3 X
3 2 2 -> kein wert mehr rechts neben uns: R++

R: 3
2 2 2 1

http://www.numericana.com/data/partition.htm

"""

def list_is_desc(l):
    for i in range(len(l) - 1):
        if l[i] < l[i+1]:
            return False
    return True

count = 0
_NUMBER = int(sys.argv[1])
final = []
# Startwerte festlegen
final.append([[i + 1] + [1] * (_NUMBER - i - 1) for i in range(_NUMBER - 1)])
count += len(final[0])
pointer = 1
while True:
    final.append([])
    working_copy = deepcopy(final[pointer -1])
    # falls wir im letzten schritt keine legitimen summen erzeugt haben, sind wir fertig!
    if len(working_copy) == 0:
        print(count)
        sys.exit(0)
    for cur in working_copy:
        legit = True
        while legit:
            # falls rechts neben uns nichts mehr ist, rekursion erhoehen
            try:
                tmp = cur[pointer + 1]
            except:
                break
            # rechteste element ist eine 1? aufaddieren auf pointer
            cur[pointer] += cur.pop()
            # noch legitim? wenn ja, eintragen und count erhoehen
            legit = list_is_desc(cur)
            if legit:
                count += 1
                final[pointer].append(deepcopy(cur))
            # wenn nein, naechsten wert nehmen
    pointer += 1
    print(f"starting recursion depth {pointer}")