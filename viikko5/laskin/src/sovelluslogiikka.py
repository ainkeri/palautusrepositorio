class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edellinen_arvo = None
    
    def tallenna_tila(self):
        self._edellinen_arvo = self._arvo

    def miinus(self, operandi):
        self.tallenna_tila()
        self._arvo -= operandi

    def plus(self, operandi):
        self.tallenna_tila()
        self._arvo += operandi

    def nollaa(self):
        self.tallenna_tila()
        self._arvo = 0
    
    def kumoa(self):
        if self._edellinen_arvo is not None:
            self._arvo = self._edellinen_arvo
            self._edellinen_arvo = None

    def aseta_arvo(self, arvo):
        self.tallenna_tila()
        self._arvo = arvo

    def arvo(self):
        return self._arvo
