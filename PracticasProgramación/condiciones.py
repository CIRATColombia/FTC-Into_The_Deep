import math
p1=float(input("Escriba el puntaje del participante uno"))
p2=float(input("Escriba el puntaje del participante dos"))
p3=float(input("Escriba el puntaje del participante tres"))

if p1>p2 and p1>p3:
    print("el ganador es el participante uno")
elif p2>p3 and p2>p1:
    print("el ganador es el participante dos")
elif p3>p2 and p3>p1:
    print("el ganador es el participante tres")
else:
    print("EMPATEEEEE")
