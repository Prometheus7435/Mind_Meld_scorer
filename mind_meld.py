# MIND MELD, an Incomparable game show (and perhaps found elsewhere, who knows)
# Concept: A game where thinking differently will be a detriment

# RULES:
# A player picks between two topics, all of the players then create a list of
# five items of that topic. The lists are revealed and compared to each other.
# Players score points for an item on their lists that is also found on another
# player's list. If all the items in a player's list is matched, they've
# acheived a MIND MELD and score additional points.

mind_meld_bonus = 3
required_entries = 5
max_rounds = 5


def mod_points(players: dict) -> dict:
    for p in players:
        print(f"{p}")

    while True:
        user_input = input("Which player would you like to +/- points to?  ")
        try:
            point_mod = int(input("How many points?  "))
            players[user_input]["score"] += point_mod
        except:
            print("SNELL, NO FRACTIONS!")

        end_mod = input("Is that all the random points to give out? (y/n)")
        if end_mod.startswith("y"):
            break
        else:
            print("\n")

    print("The new player scores are")
    for p in players:
        print(f'{p}: {players[p]["score"]}')

    return players


def get_players() -> list:
    while True:
        entries = (
            input("Type in the players names seperated by a comma: ")
            .replace(" ", "")
            .split(",")
        )
        confirmation = input(f"Is this list of players correct?\n{entries} (y/n): ")
        if not confirmation.startswith("n"):
            break

    return {a: {"entries": [], "score": 0} for a in entries}


def scoring(player_list: list, compare_list: list, meld_requirement: int):
    round_score = 0
    meld_status = False
    for entry in player_list:
        item_score = compare_list.count(entry)
        # print(entry, compare_list)
        round_score += item_score
    if round_score == required_entries:
        round_score += mind_meld_bonus
        meld_status = True
    return round_score, meld_status


def rounds(players: dict):
    meld_requirement = required_entries
    # print(meld_requirement)

    for p in players:
        players[p]["entries"] = (
            input(f"Enter {p}'s items, seperated by a comma: ")
            .replace(" ", "")
            .lower()
            .split(",")
        )

    print(f"The scores for round  are")
    for p in players:
        compare_list = []
        for e in players:
            if e != p:
                compare_list += players[e]["entries"]
        player_round_score, meld_status = scoring(
            players[p]["entries"], compare_list, meld_requirement
        )
        print(f"{p} gained {player_round_score} points")
        if meld_status:
            print(f"     And {p} has melded the minds")
        players[p]["score"] += player_round_score

    chaos = input("are there chaos points to be given out? (y/n): ")
    if chaos.startswith("y"):
        players = mod_points(players)

    return players


def main(players: dict):
    num_round = 1
    while True:
        print(f"Round {num_round}")
        players = rounds(players)
        print(f"\nThe player scores after Round {num_round} are:")
        for p in players:
            print(f'{p} has {players[p]["score"]} points')
        print("\n")

        if num_round >= max_rounds:
            game_over = input("was that the last of the normal rounds? (y/n): ")
            if game_over.startswith("y"):
                break
        num_round += 1


if __name__ == "__main__":
    players = get_players()
    # print(players)
    main(players)
