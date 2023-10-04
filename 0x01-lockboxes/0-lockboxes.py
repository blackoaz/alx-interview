#!/usr/bin/python3
"""
function for checking keys for locked and unlocked boxes
"""
def canUnlockAll(boxes):
    if not boxes or not boxes[0]:
        return False

    num_boxes = len(boxes)
    unlocked = [False] * num_boxes

    # The first box is unlocked
    unlocked[0] = True

    # start with the keys from the first box
    keys_to_check = [0]

    while keys_to_check:
        current_box = keys_to_check.pop()

        for key in boxes[current_box]:
            if 0 <= key < num_boxes and not unlocked[key]:
                unlocked[key] = True
                keys_to_check.append(key)

    return all(unlocked)
