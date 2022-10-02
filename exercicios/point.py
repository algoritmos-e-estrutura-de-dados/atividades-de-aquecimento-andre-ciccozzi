import math
x1=float(input("Escreva o x1: "))
y1=float(input("Escreva o y1: "))

x2=float(input("Escreva o x2: "))
y2=float(input("Escreva o y2: "))

p1=(x2-x1)**2
p2=(y2-y1)**2

rq=math.sqrt(p1+p2)

print(f"{rq:.4f}")