import mobTables

print("You are in the town of startsville,")

running = True
inStartsville = True

while running:
    if inStartsville:
        choice = input("you can input TALK to talk to the villagers, or input TRAIN to head to the nearby grass field: ")
        if choice.lower() == "train":
            mobTables.grassField()
        elif choice.lower() == "talk":
            print("This feature is in development")
#TODO // implement villager talk