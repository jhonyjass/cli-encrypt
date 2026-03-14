import getpass


class EntradaCLI:

    def pedir_contraseña(self, confirmar: bool = False) -> str:
        contraseña = getpass.getpass("Contraseña: ")

        if confirmar:
            confirmacion = getpass.getpass("Confirmar contraseña: ")
            if contraseña != confirmacion:
                raise ValueError("Las contraseñas no coinciden")

        return contraseña