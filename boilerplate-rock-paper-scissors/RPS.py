# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.


# prev_play auto updates.
def player(
    prev_play,
    opponent_history=[],
    order={},  # Stores all the values ranging from "RRRR", "RRRP"... "SSSS"
):
    # The number of sequences to track. Abbey uses 2, and 5 is required to pass the tests
    n = 5

    ideal_response = {"P": "S", "R": "P", "S": "R"}

    # Append the opponent history
    if prev_play:
        opponent_history.append(prev_play)

    # First attempt
    if not prev_play:
        prev_play = "P"
        opponent_history.append(
            prev_play
        )  # Assume opponent first play R and keep track of the count of it
        return "R"

    elif len(opponent_history) < n:
        return "R"

    # Len of history at least 5
    else:
        # extract the last 5 moves
        prev5 = "".join(opponent_history[-n:])
        order[prev5] = order.get(prev5, 0) + 1

        # Find all the potential plays by first extracting the 4 previous moves
        prev4 = "".join(opponent_history[-(n - 1) :])
        potential_plays = [prev4 + "R", prev4 + "P", prev4 + "S"]

        # Find the most frequent sequence
        most_frequent = ""
        cur = -1
        for p in potential_plays:
            if order.get(p, 0) > cur:
                cur = order.get(p, 0)
                most_frequent = p

        # Extract the next move, and return the ideal response of it
        return ideal_response[most_frequent[-1]]
