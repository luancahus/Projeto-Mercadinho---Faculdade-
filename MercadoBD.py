from datetime import datetime
#from time import sleep

# projeto caixa registradora
# Loja de Bebidas

# Função
def loja():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~ MERCADINHO PYTHON ~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f'Produto                     Preço     Quantidade    Preço Total')
    n = 0
    for i in itens:

        print(f'{n+1}. {produtos[i]["nome"]: <25} R${produtos[i]["preço"]: <10}   {quantidade[n]: <6}     R$ {produtos[i]["preço"] * quantidade[n]:.2f}')
        n+= 1
        
    print(f"Total da compra:                                       R${total:.2f}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



quantidade = []
itens = []


total=0
produtos = [{},
            {"nome":"agua","codigo":1, "preço": 1.50},
            {"nome":"Coca cola 1L","codigo":2, "preço": 5},
            {"nome":"Coca cola 2,5L", "codigo":3, "preço": 8},
            {"nome": "Guaraná Antártica 1L", "codigo": 4, "preço": 4},
            {"nome": "Guaraná Antártica 2,5L", "codigo": 5, "preço": 7.50},
            {"nome": "Brahma lata", "codigo": 6, "preço": 2.50},
            {"nome": "Brahma long neck", "codigo": 7, "preço": 3.50},
            {"nome": "Skol lata", "codigo": 8, "preço": 2.19},
            {"nome": "Skol long neck", "codigo": 9, "preço": 4},
            {"nome": "Merlot", "codigo": 10, "preço": 45},
            {"nome": "Smirnoff 1L", "codigo": 11, "preço": 30},
            {"nome": "Skol beats 303mL", "codigo": 12, "preço": 5.69},
            {"nome": "Pitú", "codigo": 13, "preço": 4.49},
            {"nome": "Licor Amarula", "codigo": 14, "preço": 75},
            {"nome": "Vinho chileno branco", "codigo": 15, "preço": 32},
            {"nome": "Johnny Walker", "codigo": 16, "preço": 112},
            {"nome": "Sprite 2,5L", "codigo": 17, "preço": 8},
            {"nome": "Gin Flowers", "codigo": 18, "preço": 45},
            {"nome": "cerveja Skol 600ML 12UND", "codigo": 19, "preço":  73},
            {"nome": "Heineken Barril 5L", "codigo": 20, "preço": 149},
            {"nome": "Vodka Absolut 1L", "codigo": 21, "preço": 79.90},
            {"nome": "Batata Elma Chips 156g", "codigo": 22, "preço": 15.90},
            {"nome": "Batata pringles 114g", "codigo": 23, "preço": 12.90},
            {"nome": "Cast.Caju 100g", "codigo": 24, "preço": 7.99},
            {"nome": "Queijo Coalho 1Kg", "codigo": 25, "preço": 19.90},
            {"nome": "Salame 100g", "codigo": 26, "preço": 7.90},
            {"nome": "Presunto Aurora 150g", "codigo": 27, "preço": 4.99},
            {"nome": "Choc.Lacta", "codigo": 28, "preço": 3.99},
            {"nome": "Pao forma", "codigo": 29, "preço": 2.99},
            {"nome": "Leite Elege 1L Und", "codigo": 30, "preço": 2.99},
            {"nome": "Cafe 3coraçoes", "codigo": 31, "preço": 4.99},
            {"nome": "Bisc Treloso", "codigo": 32, "preço": 0.99},
            {"nome": "Arroz branco", "codigo": 33, "preço": 2.69},
            {"nome": "Macarrao parafuso", "codigo": 34, "preço": 2.99},
            {"nome": "Flocao", "codigo": 35, "preço": 1.35},
            {"nome": "Acuc Crital 1Kg", "codigo": 36, "preço": 2.09},
            {"nome": "Ling Calab.Sadia", "codigo": 37, "preço": 11.99},
            {"nome": "Pimentao 1Kg", "codigo": 38, "preço": 4.59},
            {"nome": "Batata 1Kg", "codigo": 39, "preço": 5.99},
            {"nome": "Cenoura 1Kg", "codigo": 40, "preço": 3.59},
            {"nome": "Tomate 1Kg", "codigo": 41, "preço": 6.49},
            {"nome": "Chuchu 1Kg", "codigo": 42, "preço": 1.99},
            {"nome": "Cebola 1Kg", "codigo": 43, "preço": 5.99},
            {"nome": "batata doce ", "codigo": 44, "preço": 2.39},
            {"nome": "Banana prata 1kg", "codigo": 45, "preço": 2.49},
            {"nome": "Maça 1Kg", "codigo": 46, "preço": 6.99},
            {"nome": "Laranja 1Kg", "codigo": 47, "preço": 4.99},
            {"nome": "Manga rosa 1Kg", "codigo": 48, "preço": 5.99},
            {"nome": "Melancia 1Kg", "codigo": 49, "preço": 1.39},
            {"nome": "Maracuja 1Kg", "codigo": 50, "preço": 6.99},
            {"nome": "Goiaba 1kg", "codigo": 51, "preço": 4.90},
            {"nome": "Acerola 1Kg ", "codigo": 52, "preço": 2.50},
            {"nome": "Abacaxi  1Und", "codigo": 54, "preço": 1.99},
            {"nome": "Desodorante aerosol 1und", "codigo": 55, "preço": 9.99},
            {"nome": "Sabonete protex 1Und", "codigo": 56, "preço": 2.00},
            {"nome": "Pasta de dente Und", "codigo": 57, "preço": 1.99},
            {"nome": "Agua Sanit 1L", "codigo": 58, "preço": 0.99 },
            {"nome": "Alcool 70%", "codigo": 59, "preço": 8.99},
            {"nome": "Papel Hig. Und", "codigo": 60, "preço": 4.99}
            ]
while True:
    codigo = int(input('Digite o código do produto: '))
    if codigo == 0:
        break
    elif codigo < 0:
        codigo = (codigo * (-1)) - 1
        c = itens[codigo]
        
        total -= produtos[c]['preço'] * quantidade[codigo]
        
        itens.pop(codigo)
        quantidade.pop(codigo)
        
        
    else:
        itens.append(codigo)
        print(produtos[codigo]['nome'])
        qnt = float(input('informe a quantidade: '))
        quantidade.append(qnt)
        preço = produtos[codigo]['preço'] * qnt
        total+= preço
    loja()


def nota(arquivo):

    data_hora = datetime.now()
    data = data_hora.strftime("%d/%m/%y")
    hora = data_hora.strftime("%X")

    
    

    loja = f'\n~~~~~~~~~~~~~~~~~~~~~~~~ MERCADINHO PYTHON ~~~~~~~~~~~~~~~~~~~~~~~~\n'
    painel = f'Produto                     	Preço      Quantidade    Preço Total\n'
    linha = '\n'
    final = '~'*70, '\n'
    meio = '-'*70, '\n'
    mostrar_total = f"Total da compra: \t\t\t\t\t R$ {total:.2f}"
    
    
    arquivo.writelines(loja)
    arquivo.writelines(f'Data: {data}\t\t\t\t\t\tHora: {hora}\n')
    arquivo.writelines(meio)
    arquivo.writelines(painel)

    n=0

    for i in itens:

        nome = f'{n+1}. {produtos[i]["nome"]: <25}     '
        preco = f'R${produtos[i]["preço"]: <6}     '
        quant = f'{quantidade[n]:<7}    '
        totals = f'R$ {produtos[i]["preço"] * quantidade[n]:>5}'

        n+= 1

        arquivo.writelines(linha)
        arquivo.writelines(nome)
        arquivo.writelines(preco)

        arquivo.writelines(quant)
        arquivo.writelines(totals)
        
    arquivo.writelines(linha)
    arquivo.writelines(meio)
    arquivo.writelines(mostrar_total)
    arquivo.writelines(linha)
    arquivo.writelines(final)
        
    arquivo.close()

def notaFiscal():
    notaFiscal = open('notaFiscal.txt', 'w')
    nota(notaFiscal)

def relatorio():
    linha = '\n'
    relatorio = open('Relatorio.txt', 'a')
    relatorio.writelines(linha*3)
    nota(relatorio)
        

notaFiscal()

relatorio()
