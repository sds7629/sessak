import random
from typing import overload, Optional
import schedule


class Status:

    def __init__(
        self,
        name: str,
        hp: int,
        power: int,
        critical: int,
        mp: Optional[int] = None,
    ) -> None:
        self._life = "Live"
        self._name = name or None
        self._hp = hp
        self._mp = mp or 0
        self._power = [p for p in range(power - 4, power + 1)]
        self._critical = critical
        self._magicnum = 2

    def show_status(self) -> None:
        print(
            f"""
            나의 상태: {self._life}
            닉네임: {self._name}
            HP: {self._hp}
            MP: {self._mp}
            Damage: {random.choice(self._power)}
            크리티컬 확률: {self._critical}%
              """
        )

    @staticmethod
    def basic_attack(base: object, target: object) -> Optional[str]:
        critical_percent = random.randint(1, 100)
        if critical_percent <= base._critical:
            print("크리티컬 데미지!!!!")
            random_damage = random.choice(base._power) * 2
        else:
            random_damage = random.choice(base._power)
        target._hp -= random_damage
        print(
            f"{base._name}님의 기본 공격으로 인해 {target._name}이 {random_damage}의 피해를 입었습니다."
        )
        if target._hp <= 0:
            target._life = "Dead"
            print(f"{base._name}님의 공격으로 {target._name}이 사망헸습니다.")
        else:
            print(
                f"{base._name}님의 공격으로 {target._name}의 HP가 {target._hp}남았습니다."
            )
        return target._life

    @staticmethod
    def magic_attack(base: object, target: object) -> Optional[str]:

        if base._mp <= 0:
            print("마법 공격을 하기 위한 마나가 부족합니다.")
            return
        base._mp -= 10
        base._magicnum -= 1

        if base._magicnum <= 0:
            print("사용할 수 있는 마법 공격의 횟수를 초과했습니다.")
            return

        magic_damage = round(random.choice(base._power) * 1.5)
        target._hp -= magic_damage
        print(
            f"{base._name}님의 마법 공격으로 인해 {target._name}이 {magic_damage}의 피해를 입었습니다."
        )
        if target._hp <= 0:
            target._life = "Dead"
            print(f"{base._name}의 공격으로 {target._name}이 사망했습니다.")
        else:
            print(
                f"{base._name}의 공격으로 {target._name}의 HP가 {target._hp} 남았습니다."
            )
        return target._life


class Player(Status):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class Monster(Status):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class Game:
    def __init__(self, player: Player, monster: Monster) -> None:
        self.player = player
        self.monster = monster

    def fight(self) -> None:
        print(f"야생의 {monster._name}을 맞닥뜨렸다! 싸움을 해야할까?")
        print(
            """
              1. 그럼그럼 잡아야지
              2. ㄴ.. 나 무서워 도망칠래!
              3. 빡종
              """
        )
        choice = input("당신의 행동을 선택해주세요!")
        if choice == "1":
            print(
                """
                  1. 기본 공격
                  2. 마법 공격
                  """
            )
            attack_choice = input("어떤 종류의 공격을 하시겠습니까!")
            if attack_choice == "1":
                monster_life = self.player.basic_attack(self.player, self.monster)
            else:
                monster_life = self.player.magic_attack(self.player, self.monster)
            if monster_life == "Dead":
                print(f"{self.monster._name}을 토벌했습니다! 축하드립니다")
                self.start_game()
            else:
                random_attack = [self.monster.basic_attack, self.monster.magic_attack]
                monster_attack = random.choice(random_attack)
                player_life = monster_attack(self.monster, self.player)
                if player_life == "Dead":
                    print("game over")
                    return
                else:
                    print("행동을 선택해 주세요!")
                    print(
                        """
                          1. 곧 죽어도 다시 공격이지~
                          2. 저 자식 너무 쎈데..? 도망쳐야겠어
                          """
                    )
                    attack_choice2 = input("어떤 행동을 하시겠습니까!?")
                    if attack_choice2 == "1":
                        self.fight()
                    else:
                        print("당신 도망자야!?")
                        return
        elif choice == "2":
            print("당신 도망자야?")
            self.start_game()
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


player = Player(name="jinwoo", hp=100, mp=30, power=10, critical=15)
monster = Monster(
    name=random.choice(["주황버섯", "머쉬맘", "발록", "예티와 페페"]),
    hp=15,
    mp=30,
    power=20,
    critical=10,
)

game = Game(player, monster)
is_gameover = False
while not is_gameover:
    # print(f"야생의 {monster._name}을 맞닥뜨렸다! 싸움을 해야할까?")
    # print(
    #     """
    #           1. 그럼그럼 잡아야지
    #           2. ㄴ.. 나 무서워 도망칠래!
    #           3. 빡종
    #           """
    # )
    cont = game.start_game()
    if cont == None:
        is_gameover = True
        print("게임이 종료됩니다.")
