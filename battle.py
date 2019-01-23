import random


class Battle:

    def roll_dice(self, roll):
        result = int(0)
        i = 0
        while i < roll:
            dice = random.randint(1, 6)
            i = i + 1
            result = result + dice
        return result

    def health_check(self, hero, monster):
        print(hero.name, "has ", hero.endurance, " HP")
        print(monster.name, "has ", monster.endurance, " HP")

    def damage(self, health):
        new_health = health - 1
        return new_health

    def escape(self, agility):
        if (agility*10) <= random.randint(1, 100):
            print("Hero escaped from battle")
            return True
        else:
            print("Hero can't escape!")
            return False

    def attack(self, hero, monster):
        attack_value = 0
        agility_value = 0
        attack_value += self.roll_dice(self, hero.attack)
        agility_value += self.roll_dice(self, monster.agility)
        print(attack_value, agility_value)
        if attack_value > agility_value:
            monster.endurance = self.damage(self, monster.endurance)
            print("Hero attacked")
            hero.endurance = self.damage(self, hero.endurance)
            print("Monster attacked")
        elif agility_value > attack_value:
            hero.endurance = self.damage(self, hero.endurance)
            print("Monster attacked")
            monster.endurance = self.damage(self, monster.endurance)
            print("Hero attacked")
        else:
            print("Attacker missed")

    def fight(self, hero, monster):
        while True:
            if hero.endurance >= 0 and monster.endurance >= 0:
                print("You are battling a", monster.name, "! \n[1] Fight \n[2] Escape\n")
                choice = int(input())
                self.health_check(self, hero, monster)
                if choice == 1:
                    self.attack(self, hero, monster)
                elif choice == 2:
                    self.escape(self, hero.agility)
                else:
                    print("Invalid selection, try again")
            else:
                print("Battle ended")
                break