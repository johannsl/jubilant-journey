
def play_bowling(rolls):
    # print(rolls)
    score = 0
    roll = 0
    for frame in range(10):
        # print("frame {}, roll {}, score {}".format(frame, rolls[roll], score))
        if rolls[roll] == 10:
            score += 10
            score += rolls[roll + 1] + rolls[roll + 2]
            roll += 1
        elif rolls[roll] + rolls[roll + 1] == 10:
            score += 10
            score += rolls[roll + 2]
            roll += 2
        else:
            score += rolls[roll] + rolls[roll + 1]
            roll += 2
    return score
