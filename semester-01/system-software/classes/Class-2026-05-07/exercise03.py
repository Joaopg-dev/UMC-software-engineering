nomes = []

print("\nDigite os nomes que desejar!")
print("Para sair, digite: 'sair' \n")

while True:
            nome = input(f"Digite um nome: ")
            
            if nome.lower() == "sair":
                break

            nomes.append(nome)

print(f"{nomes}")