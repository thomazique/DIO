contatos = {
    "guilherme@email.com": {"nome": "Guilherme", "telefone": "1111-2222"},
    "Giovana@email.com": {"nome": "Giovana", "telefone": "2222-1111"},
    "extra@email.com": {"nome": "Giovana", "telefone": "2222-1111", "extra": {"a": 1}},

}

for chave in contatos:
    print(chave)



for chave in contatos:
    print(chave, contatos[chave])


