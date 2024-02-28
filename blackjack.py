logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
from typing import List

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


class User:
    def __init__(self, name: str):
        self._name = name
        self._user_card = list()

    @staticmethod
    def random_card():
        random_choice = random.choice(deck)
        return random_choice

    def choice_card(self) -> List:
        for _ in range(2):
            self._user_card.append(self.random_card())
        return self._user_card

    def calculate_card(self) -> int:
        if sum(self._user_card) == 21 and len(self._user_card) == 2:
            return 0

        if 11 in self._user_card and sum(self._user_card) >= 21:
            self._user_card.remove(11)
            self._user_card.append(1)

        return sum(self._user_card)

    def new_card(self) -> None:
        self._user_card.append(self.random_card())


player1 = User("jinoo")
dealer_com = User("딜러")


class BlackJackGame(User):
    def __init__(self, user: User, dealer: User) -> None:
        self.player1 = user
        self.dealer = dealer
        self.is_gameover = False

    def game_settings(self):
        self.player1.choice_card()
        self.dealer.choice_card()

    @staticmethod
    def compare(player: int, dealer: int) -> str:
        if player == dealer:
            return "Draw 🙃"
        elif dealer == 0:
            return "Blackjack 😱"
        elif player == 0:
            return "Win Blackjack 😎"
        elif player > 21:
            return "21을 초과 했어요 당신은 졌습니다."
        elif dealer > 21:
            return "딜러가 21점을 초과 했어요 플레이어가 이겼습니다."
        elif player > dealer:
            return "플레이어가 이겼습니다.😃"
        else:
            return "딜러가 이겼습니다. 😤"

    def game_start(self):
        print(logo)
        sure = input("게임을 시작하시겠습니까? y or n")
        if sure == "y":
            self.game_settings()
            player_score = self.player1.calculate_card()
            dealer_score = self.dealer.calculate_card()
            print(f"나의 덱 {self.player1._user_card}")
            while not self.is_gameover:
                if player_score == 0 or dealer_score == 0 or player_score >= 21:
                    self.is_gameover = True
                else:
                    your_choice = input("카드를 한장 더 뽑으시겠습니까? y or n ")
                    if your_choice == "y":
                        self.player1.new_card()
                        player_score = self.player1.calculate_card()
                        print(f"나의 덱 {self.player1._user_card}")
                    else:
                        self.is_gameover = True
            while dealer_score != 0 and dealer_score < 17:
                self.dealer.new_card()
                dealer_score = self.dealer.calculate_card()

            print(
                f"""
            {self.player1._name}님의 카드는 {self.player1._user_card}, 딜러의 카드는 {self.dealer._user_card}
            {self.player1._name}님의 점수는 {player_score} 딜러의 점수는 {dealer_score}
            결과는 {self.compare(player_score, dealer_score)}
                """
            )
        else:
            exit()


if __name__ == "__main__":
    game = BlackJackGame(player1, dealer_com)
    print(game.game_start())
