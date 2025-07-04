# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.


# prev_play auto updates.
def player(
    prev_play,
    opponent_history=[],
    order={},  # Stores all the values ranging from "RRRR", "RRRP"... "SSSS"
):

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

    elif len(opponent_history) < 4:
        return ideal_response[prev_play]

    # Len of history at least 4
    else:
        # extract the last 4 moves
        prev4 = "".join(opponent_history[-4:])
        order[prev4] = order.get(prev4, 0) + 1

        # Find all the potential plays by first extracting the 3 previous moves
        prev3 = "".join(opponent_history[-3:])
        potential_plays = [prev3 + "R", prev3 + "P", prev3 + "S"]

        # Find the most frequent sequence
        most_frequent = ""
        cur = -1
        for p in potential_plays:
            if order.get(p, 0) > cur:
                cur = order.get(p, 0)
                most_frequent = p

        # Extract the next move, and return the ideal response of it
        return ideal_response[most_frequent[-1]]
