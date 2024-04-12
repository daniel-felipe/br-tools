from core.taxa import Taxa
import argparse

def main():
    parser = argparse.ArgumentParser(description='BR Tools')
    parser.add_argument('--taxas', '-t', action='store_true', help='Mostra as taxas de juros atuais'),
    args = parser.parse_args()

    if args.taxas:
        taxa = Taxa()
        taxa.show()

if __name__ == '__main__':
    main()

