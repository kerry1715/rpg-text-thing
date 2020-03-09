import mobTables
import villageTalk
import gold

print("You are in the town of startsville,")

running = True
inStartsville = True

while running:
    if inStartsville:
        choice = input(
            "you can input TALK to talk to the villagers, input TRAIN to head to the nearby grass field, input GOLD "
            "to check your purse: ")
        if choice.lower() == "train":
            mobTables.grassField()
        elif choice.lower() == "talk":
            villageTalk.villageSpeak("startsville")
        elif choice.lower() == "gold":
            print("you have %d gold." % gold.goldValue)
