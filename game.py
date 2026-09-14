from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Iron Dome"


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
    print("But no hero has answered the call... yet.")

    Dom =  Hero("Dom")

    print(f"{hero.name} is summoned into the arean with {hero.health} health")

    heroDamage = hero.attack

    goblin.take_damage(heroDamage)

if __name__ == "__main__":
    main()
