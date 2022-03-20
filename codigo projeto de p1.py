
import time
def mostrar(l):
    for c in range(0, len(l)):
            print(f' posição do Produto:{c} = Nome do produto:{produtos[c][0]}, Valor: R${produtos[c][1]}, Quantidade: {produtos[c][2]}')
    return 0
encomendas = []
produtos = []
deseja = ("sim")
while True:
    n = int(input(' 1-Adicionar produto\n 2-Alterar preço\n 3-Retirar produto ou quantidade\n 4-Mostrar produtos\n 5-Encomendar\n 6-Mostrar encomendas\n Opção:'))
    if n == 1:
        prod_novo = []
        produto = input(' Nome do produto:')
        valor = float(input(' Valor do produto:R$'))
        quant = int(input(' Quantidade do produto:'))
        prod_novo.append(produto)
        prod_novo.append(valor)
        prod_novo.append(quant)
        print(f'produto adicionado: Nome do produto:{prod_novo[0]}, Valor: R${prod_novo[1]}, Quantidade:{prod_novo[2]}\n'+'=='*35)
        produtos.append(prod_novo)
        time.sleep(1)
    elif n == 2:
        print('=='*35)
        mostrar(produtos)
        print('=='*35)
        escolha = int(input(' Fale a posição do produto que deseja alterar o valor:'))
        novo_pre = float(input(' Novo preço: R$'))
        del produtos[escolha][1]
        q = produtos[escolha][1]
        produtos[escolha][1]=novo_pre
        produtos[escolha].append(q)
        print(f'Novo preço adicionado = Nome do produto:{produtos[escolha][0]}, valor: R${produtos[escolha][1]}, Quantidade:{produtos[escolha][2]}\n'+'=='*35)
        time.sleep(1)
    elif n == 3:
        print('=='*35)
        mostrar(produtos)
        print('=='*35)
        p = input(' Deseja (remover) o produto ou (alterar) a quantidade?:').upper()
        if p == 'REMOVER':
            o = int(input(' Fale a posição do produto que quer remover:'))
            del produtos[o]
            mostrar(produtos)
        elif p == 'ALTERAR':
            p1 = int(input(' Fale a posição do produto que quer remover:'))
            p2 = input('Deseja (aumentar) ou (diminuir) a quantidade do produto:').upper()
            if p2 == 'AUMENTAR':
                pa = int(input('Quantidade que deseja aumentar:'))
                produtos[p1][2]+=pa
                print('=='*35)
                print(f'Quantidade aumentada = Nome do produto:{produtos[p1][0]}, valor: R${produtos[p1][1]}, Quantidade:{produtos[p1][2]}\n'+'=='*35)
                print('=='*35)
            elif p2 == 'DIMINUIR':
                pa = int(input('Quantidade que deseja diminuir:'))
                produtos[p1][2]-=pa
                if produtos[p1][2] <= 0:
                    pergunta = input('Não há unidades desse produto, deseja encomendar: sim ou não?')
                    if pergunta == "sim":
                        quant = int(input("Digite a quantidade deseja adicionar: "))
                        encomendas.append([produtos[p1][0], quant])
                else:
                    print(f'Quantidade reduzida = Nome do produto:{produtos[p1][0]}, valor: R${produtos[p1][1]}, Quantidade:{produtos[p1][2]}\n'+'=='*35)
            time.sleep(1)
    elif n == 4:
        if len(produtos) == 0:
            print(' Nenhum produto na lista...')
            print('=='*35)
        else:
            print('=='*35)
            mostrar(produtos)
            print('=='*35)
        time.sleep(1)
    elif n == 5:
        quantidade = nom = 0
        while True:
            nom = str(input("Digite o nome dos produtos que deseja encomendar: "))
            quantidade = int(input("Digite a quantidade deseja adicionar: "))
            encomendas.append([nom, quantidade])
            deseja = str(input("Deseja adicionar mais algum produto? sim ou não? ")).lower().strip()
            if deseja != 'sim':
                break
        print('')
        for i, a in enumerate (encomendas):
            print(f"Produto encomendado:{a[0]:<1}, Quantidade:{a[1]:>1}")
            print('=='*35)
    elif n == 6:
            print('=='*35)
            for i, a in enumerate (encomendas):
                print(f"Produto encomendado:{a[0]:<1}, Quantidade:{a[1]:>1}")
            print('=='*35)
            time.sleep(0.5)
    else:
        print("opção inválida, voltando ao menu...")
        time.sleep(1)
        continue
