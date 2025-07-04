# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.


# prev_play auto updates.
def player(
    prev_play,
    opponent_history=[],
    order={
        "RRR": 0,
        "RRP": 0,
        "RRS": 0,
        "RPR": 0,
        "RPP": 0,
        "RPS": 0,
        "RSR": 0,
        "RSP": 0,
        "RSS": 0,
        "PRR": 0,
        "PRP": 0,
        "PRS": 0,
        "PPR": 0,
        "PPP": 0,
        "PPS": 0,
        "PSR": 0,
        "PSP": 0,
        "PSS": 0,
        "SRR": 0,
        "SRP": 0,
        "SRS": 0,
        "SPR": 0,
        "SPP": 0,
        "SPS": 0,
        "SSR": 0,
        "SSP": 0,
        "SSS": 0,
    },
    order2={
        "RR": 0,
        "RP": 0,
        "RS": 0,
        "PR": 0,
        "PP": 0,
        "PS": 0,
        "SR": 0,
        "SP": 0,
        "SS": 0,
    },
):

    ideal_response = {"P": "S", "R": "P", "S": "R"}

    # Append the opponent history
    if prev_play:
        opponent_history.append(prev_play)

    # First attempt
    if not prev_play:
        prev_play = "R"
        opponent_history.append(
            "R"
        )  # Assume opponent first play R and keep track of the count of it
        return "P"

    # Len of history at least 3
    else:
        # extract the last 3 moves
        prev3 = "".join(opponent_history[-3:])
        order[prev3] += 1

        # Find all the potential plays by first extracting the 2 previous moves
        prev2 = "".join(opponent_history[-2:])
        potential_plays = [prev2 + "R", prev2 + "P", prev2 + "S"]

        # Find the most frequent sequence
        most_frequent = ""
        cur = -1
        for p in potential_plays:
            if order[p] > cur:
                cur = order[p]
                most_frequent = p

        # Extract the next move, and return the ideal response of it
        return ideal_response[most_frequent[-1]]
