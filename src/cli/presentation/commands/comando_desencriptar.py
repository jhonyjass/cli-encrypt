from core.domain.errors.errores import ErrorDominio


class ComandoDesencriptar:

    def __init__(self, servicio, entrada, salida):
        self.servicio = servicio
        self.entrada = entrada
        self.salida = salida

    def ejecutar(self, args):
        try:
            contraseña = self.entrada.pedir_contraseña()

            self.salida.mostrar_mensaje("Desencriptando archivo...")

            resultado = self.servicio.desencriptar(args.ruta, contraseña)

            self.salida.mostrar_mensaje("Archivo desencriptado correctamente")
            self.salida.mostrar_mensaje(resultado)

            return 0

        except ErrorDominio as e:
            self.salida.mostrar_error(str(e))
            return 1