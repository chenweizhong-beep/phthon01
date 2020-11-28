class Games():
    my_power: int = 200
    enemy_power: int = 199

    def __init__(self, my_hp, enemy_hp):
        self.my_hp = my_hp
        self.enemy_hp = enemy_hp

    def fight(self):
        while True:
            self.my_hp = self.my_hp - self.enemy_power
            print(self.my_hp)
            self.enemy_hp = self.enemy_hp - self.my_power
            print(self.enemy_hp)
            if self.my_hp <= 0:
                print("我输了")
                break
            if self.enemy_hp <= 0:
                print("我赢了")
                break


class HouYi(Games):
    def __init__(self, defense, my_hp, enemy_hp):
        self.defense = defense
        super().__init__(my_hp, enemy_hp)

    def fight(self):
        while True:
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            print(self.my_hp)
            self.enemy_hp = self.enemy_hp - self.my_power
            print(self.enemy_hp)
            if self.my_hp <= 0:
                print("我输了")
                break
            if self.enemy_hp <= 0:
                print("我赢了")
                break


if __name__ == '__main__':
    # game = Games(1000, 1300)
    # game.fight()
    houyi = HouYi(200, 1000, 10000)
    houyi.fight()
