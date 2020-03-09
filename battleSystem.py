availableCommand = "attack"
import random


def physical_attack(monster):
    crit = random.randint(1, 10)
    fail = random.randint(1, 20)
    if crit == 10:
        monster.health -= 8
        print("Crit! 8 damage!")
    elif fail == 20:
        print("Failed... no damage")
        pass
    else:
        print("Success, 4 damage.")
        monster.health -= 4
    print("\n")


def battle(monster):
    enemyStatus = True
    while enemyStatus:
        print("The %s is on %d hp" % (monster.name, monster.health))
        command = input("What do you do?: ")
        if command == "attack":
            physical_attack(monster)
        else:
            print("not valid, available commands are " + availableCommand)
            print("\n")
        if monster.health <= 0:
            enemyStatus = False
    print("You killed the enemy!")
