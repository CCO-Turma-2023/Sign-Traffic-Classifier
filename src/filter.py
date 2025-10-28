import os
import shutil

modo = "valid"

diretorios = ["./Dataset1/", "./Dataset2/", "./Dataset3/"]


dest_labels = "DatasetCompleto/" + modo + "/labels"
dest_images = "DatasetCompleto/" + modo + "/images"

os.makedirs(dest_labels, exist_ok=True)
os.makedirs(dest_images, exist_ok=True)

names75 = ['(A-12)', '(A-13a)', '(A-13b)', '(A-14)', '(A-18)', '(A-1a)', '(A-1b)', '(A-20a)', '(A-21b)', '(A-21c)', '(A-21e)', '(A-24)', '(A-25)', '(A-2a)', '(A-2b)', '(A-30a)', '(A-30b)', '(A-32a)', '(A-32b)', '(A-33a)', '(A-33b)', '(A-35)', '(A-36)', '(A-37)', '(A-3a)', '(A-46)', '(A-4b)', '(A-5a)', '(A-5b)', '(A-7a)', '(A-7b)', '(MA)', '(MP-1)', '(MP-2)', '(MP-3)', '(R-1)', '(R-12)', '(R-15)', '(R-19)100km', '(R-19)10km', '(R-19)110km', '(R-19)120km', '(R-19)20km', '(R-19)30km', '(R-19)40km', '(R-19)50km', '(R-19)60km', '(R-19)70km', '(R-19)80km', '(R-19)90km', '(R-2)', '(R-24a)', '(R-24b)', '(R-25a)', '(R-25b)', '(R-25c)', '(R-25d)', '(R-26)', '(R-27)', '(R-28)', '(R-29)', '(R-3)', '(R-32)', '(R-33)', '(R-34)', '(R-4a)', '(R-4b)', '(R-5a)', '(R-5b)', '(R-6a)', '(R-6b)', '(R-6c)', '(R-7)', '(R-8a)', '(R-9)']
names68 = ['(A-10b)', '(A-11b)', '(A-12)', '(A-13a)', '(A-13b)', '(A-14)', '(A-15)', '(A-18)', '(A-1a)', '(A-1b)', '(A-20a)', '(A-20b)', '(A-21c)', '(A-21d)', '(A-21e)', '(A-22)', '(A-24)', '(A-27)', '(A-28)', '(A-2a)', '(A-2b)', '(A-31)', '(A-32a)', '(A-32b)', '(A-33a)', '(A-33b)', '(A-3a)', '(A-3b)', '(A-42a)', '(A-42b)', '(A-4a)', '(A-4b)', '(A-52)', '(A-5a)', '(A-5b)', '(A-6)', '(A-7a)', '(A-7b)', '(A-8)', '(Del)', '(E-5)', '(ESP-20)', '(I-4)', '(LOC-6)', '(MO)', '(MP)', '(R-1)', '(R-15)', '(R-19)', '(R-2)', '(R-24a)', '(R-24b)', '(R-26)', '(R-27)', '(R-28)', '(R-33)', '(R-43)', '(R-4a)', '(R-4b)', '(R-5a)', '(R-6a)', '(R-6b)', '(R-6c)', '(R-7)', '(RQ)', '(S-14)', '(TUR-4)', '(de)']
names118 = ['(A-12)', '(A-18)', '(A-1a)', '(A-1b)', '(A-24)', '(A-2a)', '(A-2b)', '(A-30a)', '(A-30b)', '(A-32a)', '(A-32b)', '(A-33a)', '(A-33b)', '(A-36)', '(A-3a)', '(A-5b)', '(MA)', '(MP-1)', '(MP-2)', '(MP-3)', '(R-1)', '(R-12)', '(R-15)', '(R-19)100km', '(R-19)10km', '(R-19)110km', '(R-19)120km', '(R-19)20km', '(R-19)30km', '(R-19)40km', '(R-19)50km', '(R-19)60km', '(R-19)70km', '(R-19)80km', '(R-19)90km', '(R-2)', '(R-24a)', '(R-24b)', '(R-25a)', '(R-25b)', '(R-25c)', '(R-25d)', '(R-26)', '(R-27)', '(R-28)', '(R-29)', '(R-3)', '(R-33)', '(R-34)', '(R-4a)', '(R-4b)', '(R-5a)', '(R-5b)', '(R-6a)', '(R-6b)', '(R-6c)', '(R-7)', '(R-8a)', '(R-9)', '(A-12)', '(A-18)', '(A-1a)', '(A-1b)', '(A-24)', '(A-2a)', '(A-2b)', '(A-30a)', '(A-30b)', '(A-32a)', '(A-32b)', '(A-33a)', '(A-33b)', '(A-36)', '(A-3a)', '(A-5b)', '(MA)', '(MP-1)', '(MP-2)', '(MP-3)', '(R-1)', '(R-12)', '(R-15)', '(R-19)100km', '(R-19)10km', '(R-19)110km', '(R-19)120km', '(R-19)20km', '(R-19)30km', '(R-19)40km', '(R-19)50km', '(R-19)60km', '(R-19)70km', '(R-19)80km', '(R-19)90km', '(R-2)', '(R-24a)', '(R-24b)', '(R-25a)', '(R-25b)', '(R-25c)', '(R-25d)', '(R-26)', '(R-27)', '(R-28)', '(R-29)', '(R-3)', '(R-33)', '(R-34)', '(R-4a)', '(R-4b)', '(R-5a)', '(R-5b)', '(R-6a)', '(R-6b)', '(R-6c)', '(R-7)', '(R-8a)', '(R-9)']

nAll = [names75, names68, names118]
count = 0

classes_acima_100 = ['(R-24a)', '(R-19)40km', '(I-4)', '(R-19)80km', '(A-2a)', '(A-32b)', '(A-2b)', '(R-15)', '(A-36)', '(A-1b)', '(R-19)70km', '(R-19)120km', '(R-5b)', '(R-2)', '(R-1)', '(R-4a)', '(A-12)', '(A-18)', '(R-6a)', '(R-5a)', '(R-4b)', '(MP-3)', '(R-6b)', '(A-32a)', '(R-3)', '(R-9)', '(MP-2)', '(MA)', '(R-19)50km', '(MP-1)', '(R-19)30km', '(A-24)', '(R-19)90km', '(R-34)', '(R-24b)', '(R-19)60km', '(Del)', '(R-6c)', '(R-7)']

qntImagem = 0

for diretorio in diretorios:

    names = nAll[count]
    count += 1

    dir_labels = diretorio + modo + "/labels"
    dir_images = diretorio + modo + "/images"

    for arquivo_label in os.listdir(dir_labels):
        caminho_label = os.path.join(dir_labels, arquivo_label)
        if not os.path.isfile(caminho_label):
            continue

        with open(caminho_label, "r") as f:
            linhas = f.readlines()

        novas_linhas = []

        for linha in linhas:
            partes = linha.strip().split()
            if not partes:
                continue

            try:
                indice_original = int(partes[0])
                nome_classe = names[indice_original]

                if nome_classe in classes_acima_100:
                    # Novo índice é a posição da classe no vetor classes_acima_100
                    novo_indice = classes_acima_100.index(nome_classe)
                    # Substitui o índice na linha
                    partes[0] = str(novo_indice)
                    novas_linhas.append(" ".join(partes) + "\n")
            except (ValueError, IndexError):
                continue

        # Se houver pelo menos uma linha válida, move e escreve o label
        if novas_linhas:
            # Caminho de destino
            destino_label = os.path.join(dest_labels, arquivo_label)
            with open(destino_label, "w") as f:
                f.writelines(novas_linhas)

            # Move a imagem correspondente
            nome_base = os.path.splitext(arquivo_label)[0]
            movida = False
            for ext in [".jpg", ".jpeg", ".png"]:
                caminho_img = os.path.join(dir_images, nome_base + ext)
                if os.path.exists(caminho_img):
                    destino_img = os.path.join(dest_images, nome_base + ext)
                    shutil.copy(caminho_img, destino_img)
                    movida = True
                    break

            if movida:
                print(f"Processado e movido: {arquivo_label} + imagem")
                qntImagem += 1
            else:
                print(f"Processado e movido: {arquivo_label} (imagem não encontrada)")
                exit(1)


print("Processo Encerrado")

print ("Imagens Movidas: " + str(qntImagem))