def h1(cube):
    misplaced_count = 0

    for i, sticker_color in enumerate(cube.state):
        if sticker_color != cube.goal_state[i]:
            misplaced_count += 1

    return misplaced_count / 8


# source for documentation: https://www.reddit.com/r/algorithms/comments/wgfloz/heuristic_function_for_a_rubiks_cube/?rdt=45294


# Why is your approach not admissible? If you start one move from the solved cube.
# 12 tiles will have the wrong color. So your heuristic h(n) = 12, but in order to be admissible,
# it needs to be <= 1.And that example is also the reason why it doesn't work for you.
# If you have a different position with 10 wrong color tiles (and with a long solution),
# it will explore that node first, even though you can solve the one position with 12 wrong tiles in just one single move.
#
# It's possible to fix the heuristic, by dividing it by 12. h(n) = ceil(number_of_wrong_tile / 12).
# That heuristic will guarantee, that A* will find the shortest solution, but it will still be quite bad.
# The Rubik's Cube space is just too big.


def h2(cube):
    misplaced_count = 0

    for i, sticker_color in enumerate(cube.state):
        if sticker_color != cube.goal_state[i]:
            misplaced_count += 1

    return misplaced_count


def h3(cube, pattern_database):
    state_tuple = tuple(cube.state)
    if state_tuple in pattern_database:
        return pattern_database[state_tuple]
    else:
        # state is not in the pattern database
        return h1(cube)
