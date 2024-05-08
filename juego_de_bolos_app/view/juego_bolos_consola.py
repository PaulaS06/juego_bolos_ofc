from juego_de_bolos_app.model.juego_bolos import JuegoDeBolos


class Consola:
    def __init__(self, bolos: JuegoDeBolos):
        self.bolos: JuegoDeBolos = bolos

    @staticmethod
    def mostrar_inicio():
        print("BIENVENIDO AL JUEGO DE BOLOS")

    def registrar_rolls(self):
        for i in range(10):
            print(f"Frame {i + 1}")
