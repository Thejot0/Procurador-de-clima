import re

def digitar_local():
    local = input('Digite o local que deseja procurar e ver o clima: ')

    if re.match(r"^[A-Za-zÀ-Öà-ö\s-]+$", local):
        print('Localização encontrada')
        return local

    print('Localização incorrete')


def quantidade_dias():
    while True:
        dias = input('Digite a quantidade de dias que deseja ver a previsão (1 a 14): ')

        if dias.isalpha():
            print('Permitido apenas numeros inteiros')
            print()

        elif dias.isdigit():
            dias = int(dias)

            if dias < 1 or dias > 14:
                print('Digite os dias que estão entre 1 e 14')
                print()

            else:
                return dias


if __name__ == "__main__":
    teste = quantidade_dias()
    print(teste)