from core.domain.errors.errores import ErrorDominio


class ComandoEncriptar:

    def __init__(self, servicio, entrada, salida):
        self.servicio = servicio
        self.entrada = entrada
        self.salida = salida

    def ejecutar(self, args):
        try:
            contraseña = self.entrada.pedir_contraseña(confirmar=True)

            self.salida.mostrar_mensaje("Encriptando archivo...")

            resultado = self.servicio.encriptar(args.ruta, contraseña)

            self.salida.mostrar_mensaje("Archivo encriptado correctamente")
            self.salida.mostrar_mensaje(resultado)

            return 0

        except (ErrorDominio, ValueError) as e:
            self.salida.mostrar_error(str(e))
            return 1