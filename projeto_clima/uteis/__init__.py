import sys
from time import sleep


def linha(tam=40):
    print(f'_' * tam)


def saida_programa():
    print(
        'Saíndo do programa',end=''
          )

    for _ in range(3):
        print(
            '.', end='', flush=True
        )

        sleep(0.5)
    sys.exit()


if __name__ == "__main__":
    saida_programa()

