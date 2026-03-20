disciplinas = ["rad\n", "poo\n", "disp moveis\n"]

with open("disciplinas.txt", "w") as arquivo:
    arquivo.write("minhas disciplinas + top \n")
    for i, d in enumerate(disciplinas,1):
            arquivo.write(f'{i}. {d}\n')
            
    arquivo.writelines(disciplinas)
    
    with open("disciplinas.txt", "r") as arquivo:
        print(arquivo.read())