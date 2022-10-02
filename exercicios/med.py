a=float(input("Digite a nota do primeiro aluno:"))
b=float(input("Digite a nota do segundo aluno:"))
med=((a*3.5)+(b*7.5))/(3.5+7.5)
if(a>10 and b>10):
    print("Notas invalidas")
else:
    print(f"A média é {med:.5f}")