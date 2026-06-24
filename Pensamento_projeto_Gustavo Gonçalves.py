'''
um bloco de comentarios.
projeto barbearia:

>PO (Como dono do projeto: quero um sistema para agendar serviços para a barbearia) 

>QA (como cliente:quero um sistema para agendar serviços para a barbearia
 para que eu possa agendar um horario com mais facilidade)

 >tech (como programador:quero um sistema para agendar serviços para a barbearia,
 para  que eu possa desenvolver um software eficiente e funcional)

 >dev (como programador:quero um sistema para agendar serviços para a barbearia,
 para que eu possa implementaras funcionalidades necessárias para meus clientes )
 
 >UX (como designer de experiência do usuário: quero um sistema para agendar serviços para minha barbearia,
 para que eu possa criar uma interface intuitiva,
  confortável e agradável para os usuários, garantindo uma experiência de agendamento fácil.)

>IA (Como analista de dados: Quero um sistema de agendamento para minha barbearia,
 para que possa coletar e analisar os dados de agendamneto, ajudando a indentificar padroes de estilos e otimizar
 as estrategias de marketing.)

'''

# isso é um comentario de linha única.
print('olá, mundo!')

print('_' * 48 + '\n')
print('Bem vindo ao sistema de agendamento da barbearia\n')
print('1 - cadastrar serviço')
print('2 - agendar corte')
print('3 - ver trabalhos feitos')
print('4 - nossa localização')
print('5 - nosso contato')
print('6 - sobre nos')
print('7 - funcionamento')
print('8 - creditos')
print('0 - sair do sistema')
print('\n---------------------------\n')

opcao__definida = int(input('digite a opçao desejda:'))

    if opcao__definida == 1:
        print('opcao 1 - cadastrar serviço')

    elif opcao__definida == 2:
        print('opcao 2 - agendar corte')

    elif opcao__definida == 3:
        print('opcao 3 - ver trabalhos feitos')

    elif opcao__definida == 4:
        print('opcao 4 - nossa localização')

    elif opcao__definida == 5:
        print('opcao 5 - nosso contato')

    elif opcao__definida == 6:  
        print('opcao 6 - sobre nos')

    elif opcao__definida == 7: 
        print('opcao 7 _ funcionamento')

    elif opcao__definida == 8:
        print('opcao 8 - creditos')

    else:
        print('opcao invalida')

while True:
    print('-' * 48 + '\n')
    print('bem-vindo sistema de agendamento da barbearia\n')
    print('1 - cadastrar serviço')
    print('2- agendar corte')
    print('3- ver trabalhos feitos')
    print('4- nossa localização')
    print('5- nosso contato')
    print('6- sobre nós')
    print('7- funcionamento')   
    print('8- creditos')
    print('0- sair do sistema')
    print('\n---------------------------------\n')

    opcao = input('digite a opção desejada:')

    if opcao == '1':
    print('Cadastrando produtos...\n')

    # faça a lógica para cadastrar o produto aqui,
    # e somente a inserção dos dados usando input e os tipos de dados.

    if p1_nome == '':
        p1_nome = input('corte: ')
        p1_estoque = int(input('gustavo, victor, nicolas, felipe: '))
        p1_preco = float(input('30.00: '))
        p1_validade = input('7 dias: ')
        p1_descricao = input('o melhor corte da regiao: ')
        print(f'\n📦 Produto "{p1_nome}" cadastrado na vaga 1!')

    elif p2_nome == '':
        p2_nome = input('barba: ')
        p2_estoque = int(input('gustavo, victor, nicolas, felipe: '))
        p2_preco = float(input('20.00: '))
        p2_validade = input('7 dias: ')
        p2_descricao = input('a melhor barbearia da regiao: ')
        print(f'\n📦 Produto "{p2_nome}" cadastrado na vaga 2!')

    elif p3_nome == '':
        p3_nome = input('sombrancelha: ')
        p3_estoque = int(input('gustavo, victor, felipe, nicolas: '))
        p3_preco = float(input('7.00: '))
        p3_validade = input('7 dias: ')
        p3_descricao = input('o melhor estilo: ')
        print(f'\n📦 Produto "{p3_nome}" cadastrado na vaga 3!')

     elif p4_nome == '':
        p4_nome = input('luzes: ')
        p4_estoque = int(input('gustavo, victor, felipe, nicolas: '))
        p4_preco = float(input('50.00: '))
        p4_validade = input('1 mes: ')
        p4_descricao = input('o melhhor estilo: ')
        print(f'\n📦 Produto "{p3_nome}" cadastrado na vaga 3!')

    elif p5_nome == '':
        p5_nome = input('alisamento: ')
        p5_estoque = int(input('gustavo, victor, felipe, nicolas: '))
        p5_preco = float(input('50.00: '))
        p5_validade = input('1 mes: ')
        p5_descricao = input('o melhor estilo: ')
        print(f'\n📦 Produto "{p3_nome}" cadastrado na vaga 3!')

    else:
        print('❌ Sistema cheio! Limite de 3 produtos atingido.')


    elif opcao == '3':
        print('realizando venda...')
    
        if p1_nome == and p2_nome == "" and p3_nome == "":
            print(f'não há produtos cadastrados para realizar vendas.')
        else:
            nome_venda = input('digite o nome do produto que deseja vender: ')

            if nome_venda . lower() == p1_nome . lower() and p1_nome != "":
                qtd_venda = int (input(f"quantas unidades de '{p1_nome}' deseja vender "))
                if qtd_venda <= p1_estoque:
                    p1_estoque -= qtd_venda
                    total = qtd_venda * p1_preco
                    print(f'\n✅ venda realizada! Total: R$ {total:.2f}')
                    print(f'estoque atual de {p1_nome}: {p1_estoque} unidades.')
                else:
                    print(f'❌estoque insuficiente! temos apenas (p1_estouqe).')