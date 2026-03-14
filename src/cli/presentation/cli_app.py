class AplicacionCLI:

    def __init__(self, parser, comandos: dict):
        self.parser = parser
        self.comandos = comandos

    def ejecutar(self):
        try:
            args = self.parser.parse_args()
        except ValueError as e:
            print("Comando no válido")
            return 1

        if args.comando is None:
            self.parser.print_help()
            return 1

        comando = self.comandos.get(args.comando)

        if comando is None:
            print("Comando desconocido")
            return 1

        return comando.ejecutar(args)