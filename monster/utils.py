from typing import Optional
import random


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
        self._magicnum = mp // 10

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
    def basic_attack(base: object, target: object) -> Optional[list[str]]:
        critical_percent = random.randint(1, 100)
        if critical_percent <= base._critical:
            print(f"{base._name}의 크리티컬 데미지!!!!")
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

        if base._magicnum <= 0:
            print("사용할 수 있는 마법 공격의 횟수를 초과했습니다.")
            print("기본 공격으로 전환합니다.")
            return base.basic_attack(base, target)

        if base._mp <= 0:
            print("마법 공격을 하기 위한 마나가 부족합니다.")
            print("기본 공격으로 전환합니다")
            return base.basic_attack(base, target)

        base._mp -= 10
        base._magicnum -= 1

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

    @staticmethod
    def attack(player: object, monster: object) -> Optional[list[str]]:
        print(
            f"""
            어떤 종류의 공격을 하시겠어요!?
            1. 기본 공격
            2. 마법 공격 ({player._magicnum})회 가능
            """
        )
        attack_type = input("어떤 타입의 공격을 진행하시겠습니까?!")
        if attack_type == "1":
            monster_life = player.basic_attack(player, monster)
            player_life = monster.basic_attack(monster, player)
        else:
            monster_life = player.magic_attack(player, monster)
            player_life = monster.magic_attack(monster, player)

        return [player_life, monster_life]
