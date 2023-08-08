import time
import numpy as np
import sys

# Delay print function


def print_delayed(string):
    # uma letra de cada vez... sofrimnto
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for caracter in string:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(0.05)


# class


class pokemon:
    def __init__(self, name, types, moves, EVs, Health="===================="):
        # Savar variaveis como os atributos
        self.name = name
        self.types = types
        self.moves = moves
        self.Ataque = EVs['ATAQUE']
        self.Defesa = EVs['DEFESA']
        self.SPAtaque = EVs['SPATAQUE']
        self.SPDefesa = EVs['SPDEFESA']
        self.Velocidade = EVs['VELOCIDADE']
        self.Health = Health
        self.bars = 20  # Amount of health bars

    def Luta(self, pokemon2):
        # Porada de dois pokemons lets goooo
        # Mostrando os atributos

        print("-----POKEMONE BATTLE-----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATAQUE/", self.Ataque)
        print("DEFESA/", self.Defesa)
        print("SPATAQUE", self.SPAtaque)
        print("SPDEFESA", self.SPDefesa)
        print("LVL/", 3*(1+np.mean([
          self.Ataque,
          self.Defesa,
          self.SPAtaque,
          self.SPDefesa
          ])))
        print("\nVS")
        print(f"\n{pokemon2.name}")
        print("TYPE/", pokemon2.types)
        print("ATAQUE/", pokemon2.Ataque)
        print("DEFESA/", pokemon2.Defesa)
        print("SPATAQUE", pokemon2.SPAtaque)
        print("SPDEFESA", pokemon2.SPDefesa)
        print("LVL/", 3*(1+np.mean([
          pokemon2.Ataque,
          pokemon2.Defesa,
          pokemon2.SPAtaque,
          pokemon2.SPDefesa
          ])))
        time.sleep(2)

        # Vantagem de tipo
        # (vamos considerar as 3 primeiras so pra não escalar tanto)
        Vantagem = ["Fogo", "Agua", "Planta"]
        for i, k in enumerate(Vantagem):
            if self.types == k:
                # Both are same type
                if pokemon2.types == k:
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...'

                # Pokemon2 is STRONG
                if pokemon2.types == Vantagem[(i+1) % 3]:
                    pokemon2.Ataque *= 2
                    pokemon2.SPAtaque *= 2
                    pokemon2.Defesa *= 2
                    pokemon2.SPDefesa *= 2
                    self.Ataque /= 2
                    self.Defesa /= 2
                    self.SPAtaque /= 2
                    self.SPDefesa /= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!'

                # Pokemon2 is WEAK
                if pokemon2.types == Vantagem[(i+2) % 3]:
                    self.Ataque *= 2
                    self.Defesa *= 2
                    self.SPAtaque *= 2
                    self.SPDefesa *= 2
                    pokemon2.Ataque /= 2
                    pokemon2.Defesa /= 2
                    pokemon2.SPAtaque /= 2
                    pokemon2.SPDefesa /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...'

        # regras protas e hora do pau
        # loop que deve continuar ate a batalha acabar
        while (self.bars > 0) and (pokemon2.bars > 0):
            # Print the health of each pokemon
            print(f"\n{self.name}\t\tHLTH\t{self.Health}")
            print(f"{pokemon2.name}\t\tHLTH\t{pokemon2.Health}\n")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            print_delayed(f"\n{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            print_delayed(string_1_attack)

            # Determine damage
            # pensar em um if que checa se o ataque e fisico ou special
            pokemon2.bars -= self.Ataque
            pokemon2.Health = ""

            # Add back bars plus defense boost
            for j in range(int(pokemon2.bars+.1*pokemon2.Defesa)):
                pokemon2.Health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.Health}")
            print(f"{pokemon2.name}\t\tHLTH\t{pokemon2.Health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if pokemon2.bars <= 0:
                print_delayed("\n..." + pokemon2.name + ' fainted.')
                break

            # Pokemon2s turn

            print(f"Go {pokemon2.name}!")
            for i, x in enumerate(pokemon2.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            print_delayed(f"\n{pokemon2.name} used {pokemon2.moves[index-1]}!")
            time.sleep(1)
            print_delayed(string_2_attack)

            # Determine damage
            self.bars -= pokemon2.Ataque
            self.Health = ""

            # Add back bars plus defense boost
            for j in range(int(self.bars+.1*self.Defesa)):
                self.Health += "="

            time.sleep(1)
            print(f"{self.name}\t\tHLTH\t{self.Health}")
            print(f"{pokemon2.name}\t\tHLTH\t{pokemon2.Health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if self.bars <= 0:
                print_delayed("\n..." + self.name + ' fainted.')
                break

        money = np.random.choice(5000)
        print_delayed(f"\nOpponent paid you ${money}.\n")


if __name__ == '__main__':
    # Create Pokemon
    Charizard = pokemon('Charizard',
                        'Fogo',
                        ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'],
                        {'ATAQUE': 12,
                         'DEFESA': 8,
                         'SPATAQUE': 10,
                         'SPDEFESA': 12,
                         'VELOCIDADE': 10
                         })
    Blastoise = pokemon('Blastoise',
                        'Agua',
                        ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],
                        {'ATAQUE': 12,
                         'DEFESA': 8,
                         'SPATAQUE': 10,
                         'SPDEFESA': 12,
                         'VELOCIDADE': 10
                         })
    Venusaur = pokemon('Venusaur',
                       'Planta',
                       ['Vine Wip', 'Razor Leaf', 'Earthquake',
                        'Frenzy Plant'],
                       {'ATAQUE': 12,
                        'DEFESA': 8,
                        'SPATAQUE': 10,
                        'SPDEFESA': 12,
                        'VELOCIDADE': 10
                        })

    Charmander = pokemon('Charmander',
                         'Fogo',
                         ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],
                         {'ATAQUE': 12,
                          'DEFESA': 8,
                          'SPATAQUE': 10,
                          'SPDEFESA': 12,
                          'VELOCIDADE': 10
                          })
    Squirtle = pokemon('Squirtle',
                       'Agua',
                       ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'],
                       {'ATAQUE': 12,
                        'DEFESA': 8,
                        'SPATAQUE': 10,
                        'SPDEFESA': 12,
                        'VELOCIDADE': 10
                        })
    Bulbasaur = pokemon('Bulbasaur',
                        'Planta',
                        ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],
                        {'ATAQUE': 12,
                         'DEFESA': 8,
                         'SPATAQUE': 10,
                         'SPDEFESA': 12,
                         'VELOCIDADE': 10
                         })

    Charmeleon = pokemon('Charmeleon',
                         'Fogo',
                         ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],
                         {'ATAQUE': 12,
                          'DEFESA': 8,
                          'SPATAQUE': 10,
                          'SPDEFESA': 12,
                          'VELOCIDADE': 10
                          })
    Wartortle = pokemon('Wartortle',
                        'Agua',
                        ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],
                        {'ATAQUE': 12,
                         'DEFESA': 8,
                         'SPATAQUE': 10,
                         'SPDEFESA': 12,
                         'VELOCIDADE': 10
                         })
    Ivysaur = pokemon('Ivysaur',
                      'Planta',
                      ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],
                      {'ATAQUE': 12,
                       'DEFESA': 8,
                       'SPATAQUE': 10,
                       'SPDEFESA': 12,
                       'VELOCIDADE': 10
                       })


Charizard.Luta(Blastoise)
# Get them to fight
