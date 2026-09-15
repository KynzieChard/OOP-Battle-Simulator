from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Iron Dome"

def battle(hero:Hero, enemy:Goblin):
    while hero.is_alive() and enemy.is_alive():
        heroDamage = hero.attack()
        enemy.take_damage(heroDamage)
        if enemy.is_alive:
            enemyDamage = enemy.attack()
            hero.take_damage(enemyDamage)

        if hero.is_alive():
            print(f"{hero.name} wins!")
        else:
            print(f"{enemy.name} wins!")


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Garry")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print("But no hero has answered the call... yet.")

    goblin2 = Goblin("Barry")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")


    Dannel = Hero("Dannel")

    print(f"{Dannel.name} the hero {Dannel.role} is summoned into the arean with {Dannel.health} health")

    heroDamage = Dannel.attack()

    goblin.take_damage(heroDamage)

if __name__ == "__main__":
    main()
    battle("Dannel","goblin")