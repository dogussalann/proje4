import random
import time

class Player: #Abstraction(Soyut Sınıf) oyuncu ile ilgili genel özellikleri ve metotları tanımlar. Gerçeklemesi HumanPlayer ve ComputerPlayer'dır.
    def __init__(self, name="Oyuncu ismi"):
        self.__name = name #Encapsulation(Kapsülleme) (__)
        self.__cards = []  #Encapsulation(Kapsülleme) (__)
        self.__score = 0   #Encapsulation(Kapsülleme) (__)

    def add_card(self, card):
        self.__cards.append(card)

    def select_card(self):
        raise NotImplementedError("Burada override olucak.")#Polymorphism (Çok biçimlilik)

    def add_score(self, points):
        self.__score += points

    def get_cards(self):
        return self.__cards

    def get_score(self):
        return self.__score

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"{self.__name} (Puan: {self.__score})"

class HumanPlayer(Player): #Inheritance (kalıtım)-player
    def select_card(self):
        print(f"{self.get_name()} kartları: {', '.join(str(card) for card in self.get_cards())}")
        choice = int(input("Bir kart seçin (1. 2. 3.): ")) - 1
        return self.get_cards().pop(choice)

class ComputerPlayer(Player): #Inheritance (kalıtım)-player
    def select_card(self):
        return self.get_cards().pop(random.randint(0, len(self.get_cards()) - 1))

class Pokemon:
    def __init__(self, name, damage_points):
        self.__name = name
        self.__damage_points = damage_points

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_damage_points(self):
        return self.__damage_points

    def set_damage_points(self, damage_points):
        self.__damage_points = damage_points

    def __str__(self):
        return f"{self.__name} (Saldırı: {self.__damage_points})"

class Game:
    def __init__(self, mode):
        self.deck = [
            Pokemon("Pikachu", 50), Pokemon("Charizard", 70), Pokemon("Bulbasaur", 40),
            Pokemon("Squirtle", 30), Pokemon("Jigglypuff", 20), Pokemon("Gengar", 60),
            Pokemon("Eevee", 30), Pokemon("Snorlax", 80), Pokemon("Mewtwo", 90),
            Pokemon("Dragonite", 85)
        ]
        random.shuffle(self.deck)
        self.mode = mode
        if self.mode == '1':
            self.player1 = HumanPlayer("Oyuncu")
            self.player2 = ComputerPlayer("Bilgisayar")
        elif self.mode == '2':
            self.player1 = ComputerPlayer("Bilgisayar 1")
            self.player2 = ComputerPlayer("Bilgisayar 2")

    def deal_cards(self):
        for _ in range(3):
            self.player1.add_card(self.deck.pop())
            self.player2.add_card(self.deck.pop())

    def play_round(self):
        player1_card = self.player1.select_card()
        player2_card = self.player2.select_card()
        print(f"{self.player1.get_name()} oynuyor {player1_card}")
        time.sleep(1) #turlar arası 1 saniye mola
        print(f"{self.player2.get_name()} oynuyor {player2_card}")
        time.sleep(1) #turlar arası 1 saniye mola

        if player1_card.get_damage_points() > player2_card.get_damage_points():
            self.player1.add_score(5)
            print(f"{self.player1.get_name()} turu kazandı")
            time.sleep(1) #turlar arası 1 saniye mola
        elif player2_card.get_damage_points() > player1_card.get_damage_points():
            self.player2.add_score(5)
            print(f"{self.player2.get_name()} turu kazandı!")
            time.sleep(1) #turlar arası 1 saniye mola
        else:
            print("Bu tur berabere!")

        # Draw new cards from the deck
        if self.deck:
            self.player1.add_card(self.deck.pop())
            self.player2.add_card(self.deck.pop())
        if self.mode == '2':
            time.sleep(1) #turlar arası 1 saniye mola

    def play_game(self):
        self.deal_cards()
        while self.player1.get_cards() and self.player2.get_cards():
            self.play_round()
            print("------------")
            print(self.player1)
            print(self.player2)
            print("------------")
            time.sleep(1) #turlar arası 1 saniye mola

        # Determine the winner
        if self.player1.get_score() > self.player2.get_score():
            print(f"{self.player1.get_name()} oyunu kazandı!")
        elif self.player2.get_score() > self.player1.get_score():
            print(f"{self.player2.get_name()} oyunu kazandı!")
        else:
            print("Oyun berabere!")

# Oyunu başlat
if __name__ == "__main__":
    mode = input("Oyun modu seçin: Oyuncu_vs_Bilgisayar için 1'i Bilgisayar_vs_Bilgisayar için 2'yi seçin: ")
    game = Game(mode)
    game.play_game()