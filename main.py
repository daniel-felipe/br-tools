from core.taxa import Taxa
from core.cep import Cep
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='BR Tools')
    parser.add_argument(
        '--taxas',
        '-t',
        action='store_true',
        help='Mostra as taxas de juros atuais'
    )
    parser.add_argument(
        '--cep',
        '-c',
        help='Busca informações de um CEP'
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if args.taxas:
        taxa = Taxa()
        taxa.show()

    if args.cep:
        cep = Cep(args.cep)
        cep.show()


if __name__ == '__main__':
    main()
