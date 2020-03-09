import random

startsvilleTable = ["Skeletons are dangerous, but they drop more gold", "Welcome to startsville, that grass field is "
                                                                        "good for training."]


def villageSpeak(place):
    if place == "startsville":
        say = random.randint(0, (len(startsvilleTable))-1)
        print(startsvilleTable[say])
