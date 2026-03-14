import argparse


class ParserPersonalizado(argparse.ArgumentParser):
    def error(self, message):
        raise ValueError(message)


def crear_parser():
    parser = ParserPersonalizado(
        description="CLI de Encriptación de Archivos"
    )

    subparsers = parser.add_subparsers(
        dest="comando",
        parser_class=ParserPersonalizado
    )

    encriptar = subparsers.add_parser("encrypt")
    encriptar.add_argument("ruta")

    desencriptar = subparsers.add_parser("decrypt")
    desencriptar.add_argument("ruta")

    return parser