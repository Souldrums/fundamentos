# -*- coding: utf-8 -*-
"""Mi primer Video juego

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dIU_TRJkVFcdH-SFsJTNkLZ1B9XrvqP_
"""

class Pokemon:
    def __init__(self, especie, tipo, fortalezas, debilidades, ataque, defensa, velocidad, puntos_vida):
        self.especie = especie
        self.tipo = tipo
        self.fortalezas = fortalezas
        self.debilidades = debilidades
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.puntos_vida = puntos_vida
        self.vida_original = puntos_vida

    def calcular_dano(self, ataque_enemigo):
        efectividad = 1.0

        if self.tipo in ataque_enemigo.fortalezas:
            efectividad = 0.5
        elif self.tipo in ataque_enemigo.debilidades:
            efectividad = 2.0

        dano = (2 * self.ataque / ataque_enemigo.defensa) * efectividad
        return int(dano)

    def atacar(self, rival):
        dano_infligido = self.calcular_dano(rival)
        rival.puntos_vida -= dano_infligido

    def combate(self, rival):
        while self.puntos_vida > 0 and rival.puntos_vida > 0:
            if self.velocidad >= rival.velocidad:
                self.atacar(rival)
                if rival.puntos_vida <= 0:
                    print(f"{self.especie} ganó la batalla!")
                    break
                rival.atacar(self)
                if self.puntos_vida <= 0:
                    print(f"{rival.especie} ganó la batalla!")
            else:
                rival.atacar(self)
                if self.puntos_vida <= 0:
                    print(f"{rival.especie} ganó la batalla!")
                    break
                self.atacar(rival)
                if rival.puntos_vida <= 0:
                    print(f"{self.especie} ganó la batalla!")

    def centro_pokemon(self):
        self.puntos_vida = self.vida_original


class PokemonAgua(Pokemon):
    def __init__(self, especie, ataque, defensa, velocidad, puntos_vida):
        super().__init__(especie, "Agua", ["Fuego"], ["Planta"], ataque, defensa, velocidad, puntos_vida)


class PokemonFuego(Pokemon):
    def __init__(self, especie, ataque, defensa, velocidad, puntos_vida):
        super().__init__(especie, "Fuego", ["Planta"], ["Agua"], ataque, defensa, velocidad, puntos_vida)


class PokemonPlanta(Pokemon):
    def __init__(self, especie, ataque, defensa, velocidad, puntos_vida):
        super().__init__(especie, "Planta", ["Agua"], ["Fuego"], ataque, defensa, velocidad, puntos_vida)


class Squirtle(PokemonAgua):
    def __init__(self):
        super().__init__("Squirtle", 40, 40, 50, 250)


class Charmander(PokemonFuego):
    def __init__(self):
        super().__init__("Charmander", 45, 35, 60, 220)


class Bulbasaur(PokemonPlanta):
    def __init__(self):
        super().__init__("Bulbasaur", 35, 45, 40, 280)


# Ejemplo de uso:

if __name__ == "__main__":
    squirtle = Squirtle()
    charmander = Charmander()

    squirtle.combate(charmander)
    charmander.centro_pokemon()
    squirtle.centro_pokemon()

    bulbasaur = Bulbasaur()
    bulbasaur.combate(squirtle)

