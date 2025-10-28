import os

names75 = ['(A-12)', '(A-13a)', '(A-13b)', '(A-14)', '(A-18)', '(A-1a)', '(A-1b)', '(A-20a)', '(A-21b)', '(A-21c)', '(A-21e)', '(A-24)', '(A-25)', '(A-2a)', '(A-2b)', '(A-30a)', '(A-30b)', '(A-32a)', '(A-32b)', '(A-33a)', '(A-33b)', '(A-35)', '(A-36)', '(A-37)', '(A-3a)', '(A-46)', '(A-4b)', '(A-5a)', '(A-5b)', '(A-7a)', '(A-7b)', '(MA)', '(MP-1)', '(MP-2)', '(MP-3)', '(R-1)', '(R-12)', '(R-15)', '(R-19)100km', '(R-19)10km', '(R-19)110km', '(R-19)120km', '(R-19)20km', '(R-19)30km', '(R-19)40km', '(R-19)50km', '(R-19)60km', '(R-19)70km', '(R-19)80km', '(R-19)90km', '(R-2)', '(R-24a)', '(R-24b)', '(R-25a)', '(R-25b)', '(R-25c)', '(R-25d)', '(R-26)', '(R-27)', '(R-28)', '(R-29)', '(R-3)', '(R-32)', '(R-33)', '(R-34)', '(R-4a)', '(R-4b)', '(R-5a)', '(R-5b)', '(R-6a)', '(R-6b)', '(R-6c)', '(R-7)', '(R-8a)', '(R-9)']
names68 = ['(A-10b)', '(A-11b)', '(A-12)', '(A-13a)', '(A-13b)', '(A-14)', '(A-15)', '(A-18)', '(A-1a)', '(A-1b)', '(A-20a)', '(A-20b)', '(A-21c)', '(A-21d)', '(A-21e)', '(A-22)', '(A-24)', '(A-27)', '(A-28)', '(A-2a)', '(A-2b)', '(A-31)', '(A-32a)', '(A-32b)', '(A-33a)', '(A-33b)', '(A-3a)', '(A-3b)', '(A-42a)', '(A-42b)', '(A-4a)', '(A-4b)', '(A-52)', '(A-5a)', '(A-5b)', '(A-6)', '(A-7a)', '(A-7b)', '(A-8)', '(Del)', '(E-5)', '(ESP-20)', '(I-4)', '(LOC-6)', '(MO)', '(MP)', '(R-1)', '(R-15)', '(R-19)', '(R-2)', '(R-24a)', '(R-24b)', '(R-26)', '(R-27)', '(R-28)', '(R-33)', '(R-43)', '(R-4a)', '(R-4b)', '(R-5a)', '(R-6a)', '(R-6b)', '(R-6c)', '(R-7)', '(RQ)', '(S-14)', '(TUR-4)', '(de)']
names118 = ['(A-12)', '(A-18)', '(A-1a)', '(A-1b)', '(A-24)', '(A-2a)', '(A-2b)', '(A-30a)', '(A-30b)', '(A-32a)', '(A-32b)', '(A-33a)', '(A-33b)', '(A-36)', '(A-3a)', '(A-5b)', '(MA)', '(MP-1)', '(MP-2)', '(MP-3)', '(R-1)', '(R-12)', '(R-15)', '(R-19)100km', '(R-19)10km', '(R-19)110km', '(R-19)120km', '(R-19)20km', '(R-19)30km', '(R-19)40km', '(R-19)50km', '(R-19)60km', '(R-19)70km', '(R-19)80km', '(R-19)90km', '(R-2)', '(R-24a)', '(R-24b)', '(R-25a)', '(R-25b)', '(R-25c)', '(R-25d)', '(R-26)', '(R-27)', '(R-28)', '(R-29)', '(R-3)', '(R-33)', '(R-34)', '(R-4a)', '(R-4b)', '(R-5a)', '(R-5b)', '(R-6a)', '(R-6b)', '(R-6c)', '(R-7)', '(R-8a)', '(R-9)', '(A-12)', '(A-18)', '(A-1a)', '(A-1b)', '(A-24)', '(A-2a)', '(A-2b)', '(A-30a)', '(A-30b)', '(A-32a)', '(A-32b)', '(A-33a)', '(A-33b)', '(A-36)', '(A-3a)', '(A-5b)', '(MA)', '(MP-1)', '(MP-2)', '(MP-3)', '(R-1)', '(R-12)', '(R-15)', '(R-19)100km', '(R-19)10km', '(R-19)110km', '(R-19)120km', '(R-19)20km', '(R-19)30km', '(R-19)40km', '(R-19)50km', '(R-19)60km', '(R-19)70km', '(R-19)80km', '(R-19)90km', '(R-2)', '(R-24a)', '(R-24b)', '(R-25a)', '(R-25b)', '(R-25c)', '(R-25d)', '(R-26)', '(R-27)', '(R-28)', '(R-29)', '(R-3)', '(R-33)', '(R-34)', '(R-4a)', '(R-4b)', '(R-5a)', '(R-5b)', '(R-6a)', '(R-6b)', '(R-6c)', '(R-7)', '(R-8a)', '(R-9)']

nAll = [names75, names68, names118]

names = list(set(names75 + names68 + names118))

diretorios = ["./Dataset1/", "./Dataset2/", "./Dataset3/"]

dicionarioTreino = {name: 0 for name in names}
dicionarioTeste = {name: 0 for name in names}
dicionarioValidacao = {name: 0 for name in names}

count = 0

for diretorio in diretorios:

    diretorio += "train/labels"
    
    namesAux = nAll[count]
    count += 1

    for arquivo in os.listdir(diretorio):
        caminho = os.path.join(diretorio, arquivo)

        # Garante que é um arquivo (não uma pasta)
        if os.path.isfile(caminho):
            with open(caminho, "r") as f:
                for linha in f:
                    partes = linha.strip().split()

                    if not partes:
                        continue 

                    # Pega o primeiro valor (índice)
                    try:
                        indice = int(partes[0])
                        dicionarioTreino[namesAux[indice]] += 1
                    except (ValueError, IndexError):
                        print("Índice não encontrado")
                        pass

count = 0

for diretorio in diretorios:

    diretorio += "test/labels"

    namesAux = nAll[count]
    count += 1
    
    for arquivo in os.listdir(diretorio):
        caminho = os.path.join(diretorio, arquivo)

        # Garante que é um arquivo (não uma pasta)
        if os.path.isfile(caminho):
            with open(caminho, "r") as f:
                for linha in f:
                    partes = linha.strip().split()

                    if not partes:
                        continue 

                    # Pega o primeiro valor (índice)
                    try:
                        indice = int(partes[0])
                        dicionarioTeste[namesAux[indice]] += 1
                    except (ValueError, IndexError):
                        print("Índice não encontrado")
                        pass

count = 0

for diretorio in diretorios:

    diretorio += "valid/labels"

    namesAux = nAll[count]
    count += 1
    
    for arquivo in os.listdir(diretorio):
        caminho = os.path.join(diretorio, arquivo)

        # Garante que é um arquivo (não uma pasta)
        if os.path.isfile(caminho):
            with open(caminho, "r") as f:
                for linha in f:
                    partes = linha.strip().split()

                    if not partes:
                        continue 

                    # Pega o primeiro valor (índice)
                    try:
                        indice = int(partes[0])
                        dicionarioValidacao[namesAux[indice]] += 1
                    except (ValueError, IndexError):
                        print("Índice não encontrado")
                        pass

print("Treino:")
for nome, contagem in dicionarioTreino.items():
    if contagem > 100:
        print(f"{nome:<20} -> {contagem}")

print("Teste:")
for nome, contagem in dicionarioTeste.items():
    if contagem > 100:
        print(f"{nome:<20} -> {contagem}")

print("Validação:")
for nome, contagem in dicionarioValidacao.items():
    if contagem > 100:
        print(f"{nome:<20} -> {contagem}")


chaves = [nome for nome, contagem in dicionarioTreino.items() if contagem > 100]

with open("classes.txt", "w") as f:
    f.write("classes_acima_100 = " + str(chaves))
