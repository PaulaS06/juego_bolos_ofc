class JuegoDeBolos:
    def __init__(self):
        self.frames: list = []
        self.actual_frame: int = 0
        pass

    def tirar_bola(self, pins: int):
        if self.actual_frame < 10:
            pass


def puntaje():
    pass


class Frame:
    def __init__(self):
        self.rolls: list = []

    def registrar_roll(self, pins: int):
        self.rolls.append(pins)

    def es_open_frame(self):
        return sum(self.rolls) < 10

    def es_spare(self):
        return

    def es_strike(self):
        return self.rolls[0] == 10


class FitBall(Frame):
    def __init__(self):
        super.__init__()
