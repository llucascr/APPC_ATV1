import os

#define as variaveis iniciais
soma = 0
ult = 0
pen = 0
ant = 0
zero = 1
cons = 0
desc = 0

os.system('cls') #limpa tela

print("Bem Vindo ao Zero Cancela")

while True: #abre o laço de repetição

    digit = input("Número: ") #define o num primeiro como string
    if digit.lstrip('-').isdigit(): #verifica se é um digito permitindo números negativos
        num = int(digit) #define num com o valor de digit só em int 
        
        if num < 0:
            break #fecha o laço de repetição
        
        #inicia processos realizados caso o número seja positivo
        if num > 0:
            if pen == 0: #define o penultimo numero 
                pen = ult
            elif ant == 0 and pen > 0: #define o penultimo e o antepenultimo numero 
                ant = pen
                pen = ult
            ult = num
            soma += num
            cons += 1
            zero = 1
        elif num == 0 and soma>0:  #quando digita zero
            if zero>3:
                print("Só é permitido até 3 zeros consecutivos ")
            elif zero<=3: 
                soma=soma-ult #subtrai a soma pelo ultimo número
                ult = pen #define o penultimo numero como o ultimo
                pen = ant #define o antepenultimo numero como o penultimo 
                ant = 0 #reseta o antepenultimo
                zero += 1
                desc += 1
                cons = cons-1
        elif num == 0 and soma==0: #verifica se num e soma são iguais à 0
            print("Nenhum número para desconciderar")
        #termina processos realizados caso o número seja positivo

    else:
        print("Ta errado")  # Mensagem  de digit inválido
        input("Aperte Enter para voltar")
        
os.system('cls') #limpa tela
print("Zero Cancela Finalizado")
print("soma = ", soma)
print("numeros considerados = ", cons)
print("numeros desconsiderados = ", desc)
print("ult =", ult, "pen =", pen, "ant =", ant)