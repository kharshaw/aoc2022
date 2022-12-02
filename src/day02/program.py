from functools import reduce


def decodeChoiceDay2(play):

    opponent = play[0]
    outcome = play[1]
    # A: rock. B: paper, C: scissor
    chooser = {
        #         lose      draw       win
        "A": {"X": "C", "Y": "A", "Z": "B"},
        "B": {"X": "A", "Y": "B", "Z": "C"},
        "C": {"X": "B", "Y": "C", "Z": "A"},
    }

    return chooser[opponent][outcome]

def decodeChoiceDay1(play):
    choice = play[1]
    chooser = {
        "X": "A",
        "Y": "B",
        "Z": "C"
    }

    return chooser[choice]

def scoreGame(opponent, self):

    scores = {
        "AA": 3, # rock v rock => draw
        "AB": 6, # rock v paper => win
        "AC": 0, # rock v rock => lose
        "BA": 0, # paper v rock => lose
        "BB": 3, # paper v paper => draw
        "BC": 6, # paper v scissors => win
        "CA": 6, # scissors v rock => win
        "CB": 0, # scissors v paper => lose
        "CC": 3, # scissors v scissors => draw
    }

    lookup = opponent + self

    return scores[lookup]

def scoreChoice(choice):
    scoreCard = {
        "A": 1,
        "B": 2,
        "C": 3
    }

    return scoreCard[choice]

def scoreDayWithDayDecodeStrategy(play, decoder):
    opponent = play[0]
    myChoice = decoder(play)
    return scoreGame(opponent, myChoice) + scoreChoice(myChoice)

rounds = []

with open("./data.txt", "r") as f:

    for line in f:
        data = line.split(" ")
        rounds.append((data[0], data[1].strip()))

f.close()


print("part 1 your score: {score}".format(score = reduce(lambda acc, play: acc + scoreDayWithDayDecodeStrategy(play, decodeChoiceDay1), rounds, 0)))

print("part 2 your score: {score}".format(score = reduce(lambda acc, play: acc + scoreDayWithDayDecodeStrategy(play, decodeChoiceDay2), rounds, 0)))
