import csv
import re
#re = regex

def cargar_diccionario_ingredientes():
    archivo = open('ingredientes.txt', 'r', encoding='utf-8')
    ingredientes = archivo.readlines()
    total_ingredientes = len(ingredientes)

    for i in range(0,total_ingredientes):

        ingrediente = ingredientes[i].rstrip('\n')


        if re.search('Tomate', ingrediente):
            delimitador = re.search('\d', ingrediente).start()
            tomate = int(ingrediente[delimitador:])

        elif re.search('Lechuga', ingrediente):
            delimitador = re.search('\d', ingrediente).start()
            lechuga = int(ingrediente[delimitador:])

        elif re.search('Hamburguesa', ingrediente):
            delimitador = re.search('\d', ingrediente).start()
            hamburguesa = int(ingrediente[delimitador:])

        elif re.search('Carne', ingrediente):
            delimitador = re.search('\d', ingrediente).start()
            carne = int(ingrediente[delimitador:])

        elif re.search('Espárragos', ingrediente):
            delimitador = re.search('\d', ingrediente).start()
            espagarragos = int(ingrediente[delimitador:])

        elif re.search('Pan', ingrediente):
            delimitador = re.search('\d', ingrediente).start()
            pan = int(ingrediente[delimitador:])

        elif re.search('Papa', ingrediente):
            delimitador = re.search('\d', ingrediente).start()
            papa = int(ingrediente[delimitador:])

        elif re.search('Cebolla', ingrediente):
            delimitador = re.search('\d', ingrediente).start()
            cebolla = int(ingrediente[delimitador:])

    diccionario_ingredientes = {
        'tomate': tomate,
        'lechuga': lechuga,
        'hamburguesa': hamburguesa,
        'carne': carne,
        'esparragos': espagarragos,
        'pan': pan,
        'papa': papa,
        'cebolla': cebolla,
    }
    return diccionario_ingredientes



def cargar_diccionario_recetas():

    with open('recetas.csv', newline="", encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if str(row[0]) == 'HamburguesaCasera':
                row.pop(0)
                hamburguesacasera = row
            elif str(row[0]) == 'PastelDeCarne':
                row.pop(0)
                pasteldecarne = row
            elif str(row[0]) == 'EnsaladaEspecial':
                row.pop(0)
                ensaladaespecial = row


    diccionario_recetas = {
        'HamburguesaCasera' : hamburguesacasera,
        'PastelDeCarne' : pasteldecarne,
        'EnsaladaEspecial' : ensaladaespecial
    }
    return  diccionario_recetas



def printStocks():
    for ingrediente in diccionario_ingredientes:
        print(ingrediente, diccionario_ingredientes[ingrediente])



def reponerIngredientes(lista_ingredientes):

    input_tomate = int(lista_ingredientes.count('tomate'))
    stock_tomate = int(diccionario_ingredientes['tomate'])
    suma_tomate = stock_tomate + input_tomate
    diccionario_ingredientes.update({'tomate': suma_tomate})

    input_lechuga = int(lista_ingredientes.count('lechuga'))
    stock_lechuga = int(diccionario_ingredientes['lechuga'])
    suma_lechuga = input_lechuga + stock_lechuga
    diccionario_ingredientes.update({'lechuga': suma_lechuga})

    input_hamburguesa = int(lista_ingredientes.count('hamburguesa'))
    stock_hamburguesa = int(diccionario_ingredientes['hamburguesa'])
    suma_hamburguesa = input_hamburguesa + stock_hamburguesa
    diccionario_ingredientes.update({'hamburguesa': suma_hamburguesa})

    input_carne = int(lista_ingredientes.count('carne'))
    stock_carne = int(diccionario_ingredientes['carne'])
    suma_carne = input_carne + stock_carne
    diccionario_ingredientes.update({'carne': suma_carne})

    input_esparragos = int(lista_ingredientes.count('esparragos'))
    stock_esparragos = int(diccionario_ingredientes['esparragos'])
    suma_esparragos = input_esparragos + stock_esparragos
    diccionario_ingredientes.update({'esparragos': suma_esparragos})

    input_pan = int(lista_ingredientes.count('pan'))
    stock_pan = int(diccionario_ingredientes['pan'])
    suma_pan = input_pan + stock_pan
    diccionario_ingredientes.update({'pan': suma_pan})

    input_papa = int(lista_ingredientes.count('papa'))
    stock_papa = int(diccionario_ingredientes['papa'])
    suma_papa = input_papa + stock_papa
    diccionario_ingredientes.update({'papa': suma_papa})

    input_cebolla = int(lista_ingredientes.count('cebolla'))
    stock_cebolla = int(diccionario_ingredientes['cebolla'])
    suma_cebolla = input_cebolla + stock_cebolla
    diccionario_ingredientes.update({'cebolla': suma_cebolla})


def prepararReceta(receta):
    if re.search('HamburguesaCasera', receta):
        if int(diccionario_ingredientes['hamburguesa']) >0 and int(diccionario_ingredientes['tomate']) > 0 and int(diccionario_ingredientes['pan']>0):
            stock_hamburguesa = int(diccionario_ingredientes['hamburguesa'])
            diccionario_ingredientes.update({'hamburguesa': stock_hamburguesa - 1})

            stock_tomate = int(diccionario_ingredientes['tomate'])
            diccionario_ingredientes.update({'tomate': stock_tomate - 1})

            stock_pan = int(diccionario_ingredientes['pan'])
            diccionario_ingredientes.update({'pan': stock_pan - 1})
        else:
            if int(diccionario_ingredientes['hamburguesa']) <= 0:
                print('***No se puede hacer HamburguesaCasera porque falta Hamburguesa***')
            elif int(diccionario_ingredientes['tomate']) <=0:
                print('***No se puede hacer HamburguesaCasera porque falta Tomate***')
            elif int(diccionario_ingredientes['pan']) <=0:
                print('***No se puede hacer HamburguesaCasera porque falta Pan***')


    elif re.search('PastelDeCarne', receta):
        if int(diccionario_ingredientes['carne'])>0 and int(diccionario_ingredientes['papa'])>0 and int(diccionario_ingredientes['cebolla'])>0:
            stock_carne = int(diccionario_ingredientes['carne'])
            diccionario_ingredientes.update({'carne': stock_carne - 1})

            stock_papa = int(diccionario_ingredientes['papa'])
            diccionario_ingredientes.update({'papa': stock_papa - 1})

            stock_cebolla = int(diccionario_ingredientes['cebolla'])
            diccionario_ingredientes.update({'cebolla': stock_cebolla - 1})
        else:
            if int(diccionario_ingredientes['carne'])<=0:
                print('***No se puede hacer PastelDeCarne porque falta Carne***')
            elif int(diccionario_ingredientes['papa'])<=0 :
                print('***No se puede hacer PastelDeCarne porque falta Papa***')
            elif int(diccionario_ingredientes['cebolla'])<=0:
                print('***No se puede hacer PastelDeCarne porque falta Cebolla***')


    elif re.search('EnsaladaEspecial', receta):
        if int(diccionario_ingredientes['lechuga']) > 0 and int(diccionario_ingredientes['esparragos']) > 0 and int(diccionario_ingredientes['tomate']) > 0:
            stock_lechuga = int(diccionario_ingredientes['lechuga'])
            diccionario_ingredientes.update({'lechuga': stock_lechuga - 1})

            stock_esparragos = int(diccionario_ingredientes['esparragos'])
            diccionario_ingredientes.update({'esparragos': stock_esparragos - 1})

            stock_tomate = int(diccionario_ingredientes['tomate'])
            diccionario_ingredientes.update({'tomate': stock_tomate - 1})
        else:
            if int(diccionario_ingredientes['lechuga']) <= 0 :
                print('***No se puede hacer EnsaladaEspecial porque falta Lechuga***')
            elif int(diccionario_ingredientes['esparragos']) <= 0 :
                print('***No se puede hacer EnsaladaEspecial porque falta Esparragos***')
            elif int(diccionario_ingredientes['tomate']) <= 0 :
                print('***No se puede hacer EnsaladaEspecial porque falta Tomate***')
    else:

        receta = receta[9:]
        print('*** Lo sentimos pero no preparamos '+receta+' ***')




cargar_diccionario_recetas()
cargar_diccionario_ingredientes()

diccionario_ingredientes = cargar_diccionario_ingredientes()
diccionario_recetas = cargar_diccionario_recetas()


while True:
    print('Ingresa la receta que quieres o REPONER: ')
    comando = input()


    if re.search('REPONER', comando) or re.search('reponer', comando):
        lista_ingredientes = comando
        reponerIngredientes(lista_ingredientes)
        print('Stock actual de ingredientes disponibles')
        printStocks()
    elif re.search('PREPARAR', comando) or re.search('preparar', comando):
        receta = comando
        prepararReceta(receta)
        print('Stock actual de ingredientes disponibles')
        printStocks()
    elif re.search('STOP', comando) or re.search('stop', comando):
        quit()
    else:
        print('***Comando invalido***')
        print('*** Los comandos validos son los siguentes: REPONER, PREPARAR, STOP')

    print(len(diccionario_recetas['HamburguesaCasera']))
    print(diccionario_recetas['HamburguesaCasera'][0])






















