from cli.adapters.input.entrada_cli import EntradaCLI
from cli.adapters.output.salida_cli import SalidaCLI
from cli.presentation.cli_app import AplicacionCLI
from cli.presentation.commands.comando_desencriptar import ComandoDesencriptar
from cli.presentation.commands.comando_encriptar import ComandoEncriptar
from cli.presentation.parser.parser import crear_parser
from core.infrastructure.dependencies.dependencias import (
    encriptador,
    desencriptador
)


def main():
    parser = crear_parser()

    entrada = EntradaCLI()
    salida = SalidaCLI()

    comandos = {
        "encrypt": ComandoEncriptar(encriptador, entrada, salida),
        "decrypt": ComandoDesencriptar(desencriptador, entrada, salida),
    }

    app = AplicacionCLI(parser, comandos)

    exit_code = app.ejecutar()
    exit(exit_code)






if __name__ == "__main__":
    main()