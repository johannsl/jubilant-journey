
def play_bowling(rolls):
    frame_list = _build_frame_list(rolls)
    score = _calculate_score(frame_list)
    return score


# rolls is a list of rolls [1, 1, 5, 5, 10, 10, ...]
def _build_frame_list(rolls):
    frame_list = [[]]
    for i in range(len(rolls)):
        last_index = frame_list[len(frame_list) - 1]
        if sum(last_index) == 10 or len(last_index) == 2:
            frame_list.append([rolls[i]])
        else:
            last_index.append(rolls[i])
    return frame_list


# frame_list is a list of frames [[1, 1], [5, 5], [10], [10], ...]
def _calculate_score(frame_list):
    score = 0
    # print(frame_list)
    frames_or_max_10 = len(frame_list[:10])
    for i in range(frames_or_max_10):
        score += sum(frame_list[i])
        # print(score)
        if len(frame_list[i]) == 1:
            score += _strike_points(i, frame_list)
        elif sum(frame_list[i]) == 10:
            score += _spare_points(i, frame_list)
        # print(score)
    return score


def _strike_points(i, frame_list):
    score = 0
    if i + 1 < len(frame_list):
        score += frame_list[i + 1][0]
        if len(frame_list[i + 1]) == 2:
            score += frame_list[i + 1][1]
        elif i + 2 < len(frame_list):
            score += frame_list[i + 2][0]
    return score


def _spare_points(i, frame_list):
    score = 0
    if i + 1 < len(frame_list):
        score += frame_list[i + 1][0]
    return score
