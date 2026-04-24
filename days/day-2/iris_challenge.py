log_acessos = [
    (101, "Financeiro"),
    (102, "RH"),
    (101, "Financeiro"),  # Duplicado
    (103, "TI"),
    (102, "RH"),          # Duplicado
    (101, "Suporte")      # Novo sistema para o mesmo user
]

#unicidade

log_acessos_sem_duplicacoes =  set(log_acessos)
print(log_acessos_sem_duplicacoes)

#mapeamento

dicionario_de_acesso = {};

for tuple in log_acessos_sem_duplicacoes:
    if tuple[0] in dicionario_de_acesso:
        fake_list = []
        for item in dicionario_de_acesso[tuple[0]]:
            fake_list.append(item)
        fake_list.append(tuple[1])
        dicionario_de_acesso[tuple[0]] = fake_list
    else:
        dicionario_de_acesso[tuple[0]] = [tuple[1]]

print(f"Dicionário: {dicionario_de_acesso}")

#tupla imutavell
SISTEMAS_CRITICOS =  ("Financeiro", "RH")

usuarios_com_sistemas_criticos = [];

for acesso in log_acessos_sem_duplicacoes:
    if acesso[1] in SISTEMAS_CRITICOS:
        usuarios_com_sistemas_criticos.append(acesso)


print(usuarios_com_sistemas_criticos)