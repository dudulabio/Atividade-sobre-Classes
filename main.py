from cultura import Cultura
from safra import Safra
from talhao import Talhao
from fazenda import Fazenda
from plantio import Plantio
from trator import Trator

if __name__ == "__main__":

    cultura1 = Cultura("Milho")
    print(cultura1)
    print('-------------------------------------------------------')

    safra1 = Safra("Safra de Verão", 2024, 2025, cultura1)
    print(safra1)
    print('\n')
    print('-------------------------------------------------------')

    talhao1 = Talhao(1, 100)
    talhao2 = Talhao(2, 150)
    print(talhao1)
    print(talhao2)

    fazenda1 = Fazenda("Fazenda A")

    print('\n')
    print('----------------------------')
    fazenda1.adicionar_talhao(talhao1)
    fazenda1.adicionar_talhao(talhao2)

    print("Talhões da fazenda:")
    for talhao in fazenda1.talhoes:
        print(talhao)

    print('\n')
    print('---------------------------')
    maior_area = fazenda1.encontrar_talhao_maior_area()
    menor_area = fazenda1.encontrar_talhao_menor_area()

    print("Talhão com maior área:", maior_area.numero, "- Área:", maior_area.area, "hectares")
    print("Talhão com menor área:", menor_area.numero, "- Área:", menor_area.area, "hectares")

    plantio1 = Plantio("2024-03-25", 80, talhao1, safra1)
    print(plantio1)

    print('\n')
    print('----------------------------')
    print('Lista de tratores: ')
    trator1 = Trator('Masey Fergunson', 'Trator de Arado', 'Vermelho', '9000')
    trator2 = Trator('New Holland','Trator de Plantação', 'Azul', '7500')
    trator3 = Trator( 'John Deere','Trator de Corte', 'Verde', '8000')

    print(trator1)
    print(trator2)
    print(trator3)
    print('---------------------------')