#solicita os dados do usuario
nome = input("Insira seu nome: ")
idade = int(input("insira sua idade: "))

#exibe uma saudação ao usuario
 print(f"Olá, {nome}!") 

#utilizado if,elif, else para classificar o usuario de acordo com sua idade
if idade <= 11:
     print("Vocë é uma criança, sem responsabilidades, vá se divertir, Brinque, aprenda, corra")
elif idade <= 17:
     print("Vocë é um adolescente, aproveite essa fase da vida Estude, se desenvolva, socialize")
elif idade <= 64:
     print("Vocë é um adulto, Trabalhe, tome decisoës, viaje, seja independente")
else:
     print("Vocë é um idoso, Descanse, curta o lazer, compartilhe a experiência de vida")
    




   
