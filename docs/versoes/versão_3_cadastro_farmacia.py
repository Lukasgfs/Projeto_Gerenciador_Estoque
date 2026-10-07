

te = 'Controle de estoque'
print(te.center(20))
linha = '=' * 67
linha2 = '=' * 67 + '\n'
tex = 'Cadastro do medicamento'


print(linha)
print(te.center(70))
print(linha2)

medicamentos = []

medicamento = {
    'nome': 'Dipirona 500mg',
    'preço': 8.90,
    'quantidade': 5,
    'fabricante': 'Medley',
    'p_ativo': 'Dipirona',
}
medicamentos.append(medicamento)

medicamento = {
    'nome': 'Paracetamol 750mg',
    'preço': 6.25,
    'quantidade': 50,
    'fabricante': 'Medley',
    'p_ativo':'Paracetamol',
}
medicamentos.append(medicamento)


def cadastro_med():
        while True:
            print('\n Abrindo cadastro de produto')
            print(linha)
            print(tex.center(60))
            print(linha2)
            print(' Para voltar ao menu principal, digite: 000.\n')
            sair = False
            while True:
                nome = input('Digite o nome do medicamento: ')
                if nome == '000':
                    sair = True
                    break
                if nome.strip() == '':
                    print('Nome inválido! Por favor, digite um nome válido.')
                else:
                    break
            if sair:
                break
            
            sair = False
            while True:
                preço = input('Digite o preço: ')
                if preço == '000':
                    sair = True
                    break
                try:
                    preço = float(preço)
                    if preço <= 0:
                        print('Valor inválido! Digite um valor maior que zero.')
                    else:
                        break
                except ValueError:
                    print('Valor inválido! Por favor, digite um número positivo.')
            if sair:
                    break
            
            sair = False
            while True:
                quantidade = input('Digite a quantidade em ml ou unidades: ')
                if quantidade == '000':
                    sair = True
                    break
                try:
                    quantidade = int(quantidade)
                    if quantidade <= 0:
                        print('Quantidade inválida! Digite um valor maior que zero.')
                    else:
                        break
                except ValueError:
                    print('Quantidade inválida! Por favor, digite um número positivo.')
            if sair:
                break

            sair = False
            while True:
                fabricante = input('Digite o nome do Fabricante: ')
                if fabricante == '000':
                    sair = True
                    break
                if fabricante.strip() == '':
                    print('Fabricante inválido! Por favor, digite um nome válido.')
                else:
                    break
            if sair:
                break

            sair = False
            while True:
                p_ativo = input('Digite o princípio ativo: ')
                if p_ativo == '000':
                    sair = True
                    break
                if p_ativo.strip() == '':
                    print('Princípio ativo inválido! Por favor, digite um nome válido.')
                else:
                    break
            if sair:
                break

            print('Nome:',nome) 
            print(f'Preço: R$ {preço:.2f}') 
            print('Quantidade:', quantidade) 
            print('Fabricante:',fabricante)
            print('Princípio ativo:',p_ativo)
            novo_item = {
                'nome': nome,
                'preço': preço,
                'quantidade': quantidade,
                'fabricante': fabricante,
                'p_ativo': p_ativo
            }
            medicamentos.append(novo_item)

def listagem():
      for medica in medicamentos:
       consulta(medica)

def consulta(medica):
    print('Nome: ',medica['nome'])
    print(f"Preço: R$ {medica['preço']:.2f}")
    print('Quantidade: ',medica['quantidade'])
    print('Fabricante: ',medica['fabricante'])
    print('Princípio ativo: ',medica['p_ativo'])
    print(linha2)

def senhas():
        tenta = 0
        while tenta < 3:
            senha = input('Digite a senha de acesso: ')
            if senha == '123':
                acesso_adm()
                break
            else:
                tenta += 1
                print(f'Senha incorreta!\nTentativas máximas: 3\nVocê tentou {tenta}')
        if tenta == 3:
            print('Número máximo de tentativas atingido. Acesso negado.')

def acesso_adm():
    print('\nAcessando dados internos\n')
    total_estoques_produtos()
  
def total_item(medica):
    valor_estoque = medica['preço'] * medica['quantidade']
    print(f"Medicamento: {medica['nome']}")
    print(f"Valor em estoque: R$ {valor_estoque:.2f}")
    print(linha2)
    return valor_estoque

def total_estoques_produtos():
    total_estoque = 0
    for medica in medicamentos:
        total_estoque += total_item(medica)
    print(f'O valor total em estoque é: R${total_estoque:.2f}')
    print(linha2)

op = ''
while op != '4':
    try:
        print(' 1 - Cadastrar produto')
        print(' 2 - Lista cadastrada')
        print(' 3 - Acesso administrador')
        print(' 4 - Sair')
        op = input('Escolha uma função: ')
        if op == '1':
            cadastro_med()
            print()
        elif op == '2':
            print('\nAbrindo lista de produtos cadastrados\n')
            listagem()
        elif op == '3':
            senhas()
        elif op == '4':
            print('\n Saindo do sistema')
        else:
            print('\n Opção inválida')

    except Exception as erro:
        print('\nOcorreu um erro inesperado.')
        print(f'Erro: {erro}')
        print('Voltando ao menu principal...')







