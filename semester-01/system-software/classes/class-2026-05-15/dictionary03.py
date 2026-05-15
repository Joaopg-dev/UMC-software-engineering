# Exercício 03: Crie um dicionário com dados de um aluno e exiba suas informações.

dic_cadastro = {"Nome" : "Joao",
                "Idade" : 20,
                "Curso" : "Engenharia de Software",
                "Status" : "matriculado"
}

print("\n" + "-" * 30)
print(f"FICHA DO ALUNO : {dic_cadastro['Nome']}".upper())
print("-" * 30)
print(f"Curso: {dic_cadastro['Curso']}")
print(f"Idade: {dic_cadastro['Idade']} anos")
print(f"Status: {dic_cadastro['Status']}")
print("-" * 30)
