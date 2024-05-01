soma_tot = ult_num = pen = anti_pen = num_cons = num_desc = zero = 0
num = int(input("Números: "))
while num >= 0:
    if num == 0:
        zero += 1
        if zero > 3:
            print("Só é permitido até 3 zeros consecutivos!!!")
        else:
            soma_tot -= ult_num
            num_desc += 1
            num_cons -= 1
            ult_num = pen
            pen = anti_pen
            anti_pen = 0         
    else:
        anti_pen = pen
        pen = ult_num
        ult_num = num
        soma_tot += num
        num_cons += 1
        zero = 0
    num = int(input("Números: "))
print(f"Soma = {soma_tot}")
print(f"Números Considerados = {num_cons}")
print(f"Números Desconciderados = {num_desc}")