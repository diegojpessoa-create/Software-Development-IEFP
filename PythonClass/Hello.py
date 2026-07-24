nome = input("Qual é seu nome?")
idade = int(input("Qual é sua idade?"))
morada= input ("Qual é sua morada")
print("O seu nome é", nome, "sua idade é", idade, "é a sua morada é", morada)
if idade >=0 and idade <= 4:
       print("Voce é um bebe")
elif idade >= 5 and idade <= 13:
       print("Voce é um criança")
elif idade >= 14 and idade <= 18:
       print("Voce é um adolecente") 
elif idade >=19 and idade <= 65:
       print("Voce é um adulto")
elif idade >= 66 and idade <= 100:
       print("Voce é um idoso")
elif idade >= 101:
       print("voce é um durao")       
else:
       print("erro inesperado")      

              


