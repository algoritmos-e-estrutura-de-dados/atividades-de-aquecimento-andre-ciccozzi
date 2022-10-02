a=float(input("Digite a nota do primeiro aluno:"))
b=float(input("Digite a nota do segundo aluno:"))
c=float(input("Digite a nota do terceiro aluno:"))
med=((a*2)+(b*3)+(c*5))/(2+3+5)
if(a>10 and b>10 and c>10):
    print("Notas invalidas")
else:
    print(f"A média é {med:.1f}")