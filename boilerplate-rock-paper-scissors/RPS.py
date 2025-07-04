# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.


# prev_play auto updates.
def player(prev_play, opponent_history=[]):

    order = {
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
    }

    ideal_response = {"P": "S", "R": "P", "S": "R"}

    # First attempt
    if not prev_play:
        prev_play = "R"
        opponent_history.append("R")
        opponent_history.append(prev_play)
        return "R"

    # when len of opponent history less than 3, return the ideal response of the previous play (Similar to Kris)
    elif len(opponent_history) < 3:
        opponent_history.append("R")
        opponent_history.append(prev_play)
        return ideal_response[prev_play]

    # Len of history at least 3
    else:
        opponent_history.append(prev_play)

        # extract the last 3 moves
        prev3 = "".join(opponent_history[-3:])
        order[prev3] += 1

        # Find all the potential plays
        potential_plays = [
            prev_play + "RR",
            prev_play + "RS",
            prev_play + "RP",
            prev_play + "PR",
            prev_play + "PP",
            prev_play + "PS",
            prev_play + "SR",
            prev_play + "SP",
            prev_play + "SS",
        ]

        # Find the most frequent sequence
        most_frequent = ""
        cur = -1
        for p in potential_plays:
            if order[p] > cur:
                cur = order[p]
                most_frequent = p

        # Extract the next move, and return the ideal response of it
        return ideal_response[most_frequent[1]]
