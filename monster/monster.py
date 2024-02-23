import random
import utils

mob = [
    {
        "name": "주황버섯",
        "hp": 10,
        "mp": 0,
        "power": 3,
        "critical": 5,
    },
    {
        "name": "발록",
        "hp": 30,
        "mp": 20,
        "power": 10,
        "critical": 15,
    },
    {
        "name": "머쉬맘",
        "hp": 20,
        "mp": 10,
        "power": 6,
        "critical": 10,
    },
    {
        "name": "예티와 페페",
        "hp": 15,
        "mp": 10,
        "power": 5,
        "critical": 8,
    },
]


class Player(utils.Status):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class Monster(utils.Status):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class Game:
    def __init__(self, player: Player, monster: Monster) -> None:
        self.player = player
        self.monster = monster

    @staticmethod
    def fight_comment() -> None:
        print(f"야생의 {monster._name}을 맞닥뜨렸다! 싸움을 해야할까?")
        print(
            """
            1. 그럼그럼 잡아야지
            2. ㄴ.. 나 무서워 도망칠래!
            3. 빡종
            """
        )

    def fight(self) -> None:
        self.fight_comment()
        choice = input("어떤 선택을 하시겠습니까?")
        if choice == "1":
            result: list = self.player.attack(self.player, self.monster)
            if result[0] == "Dead":
                print("게임을 종료합니다.")
                return
            elif result[1] == "Dead":
                print("몬스터를 토벌했습니다! 축하드립니다!")
                game_cont = input("게임을 계속 진행하시겠습니까? y or n ")
                if game_cont == "y":
                    self.start_game()
                else:
                    return
        else:
            return

    def start_game(self) -> None:
        print(
            """
        1. 몬스터 찾기 2. 현재 상태 확인 3. 게임 종료
        """
        )
        position = input("어떤 행동을 취하시겠습니까?")
        if position == "1":
            self.fight()
        elif position == "2":
            self.player.show_status()
            self.start_game()
        else:
            return


random_mob = random.choice(mob)
player = Player(name="jinwoo", hp=100, mp=30, power=10, critical=15)
monster = Monster(
    name=random_mob["name"],
    hp=random_mob["hp"],
    mp=random_mob["mp"],
    power=random_mob["power"],
    critical=random_mob["critical"],
)

game = Game(player, monster)
is_gameover = False
while not is_gameover:
    cont = game.start_game()
    if player._life == "Dead":
        is_gameover = True
        print("게임이 종료됩니다.")
    if cont == None:
        is_gameover = True
        print("게임이 종료됩니다.")
