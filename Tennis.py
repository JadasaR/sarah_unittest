# -*- coding: utf-8 -*-


class Tennis():

    def score(self, p1, p2):
        if p1 < 40 and p2 < 40:
            return 'Jugador 1 ' + str(p1) + ' Jugador 2 ' + str(p2)
        elif p1 == p2:
            return 'Deuce'
        elif p1 > p2 and p1 > 40:
            return 'Advantage Jugador 1'
        elif p2 > p1 and p2 > 40:
            return 'Advantage Jugador 2'

    def anoto(self, p1, p2):
        t = Tennis()
        return t.score(p1, p2)
