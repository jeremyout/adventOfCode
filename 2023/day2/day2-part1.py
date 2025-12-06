input_file = open("input.txt", "r")
# input_file = open("example_input.txt", "r")

total_allowed_count = {
    "red": 12,
    "green": 13,
    "blue": 14
}


possible_games = []

def splitLineToGameIdAndResults(line):
    split_line = line.split(":")
    gameId = split_line[0].split()
    results = split_line[1].strip().split(";")
    return gameId[1], results

def checkResultsAndSavePossibleGameId(gameId, results):
    print(f"Game ID being checked: {gameId}")
    number_of_rounds = len(results)
    print(f"number of rounds in game {gameId}: {number_of_rounds}")
    current_round_valid = True
    current_round = 0
    for result in results:
        current_round += 1
        game_result_dict = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        result = result.strip().split(", ")
        
        for game_round in result:
            game_round = game_round.split(" ")
            color_count = game_round[0]
            color = game_round[1]
            game_result_dict[color] += int(color_count)
        print(f"Current round : {current_round}")
        print(f"Current round results: {game_result_dict}")
        print(f"Total allowed counts : {total_allowed_count}")
        if ((game_result_dict["red"] > total_allowed_count["red"])
            or (game_result_dict["green"] > total_allowed_count["green"])
            or (game_result_dict["blue"] > total_allowed_count["blue"])):
                current_round_valid = False
                print("====================================================================")
                print("Game not valid .... skipping to next game".upper())
                print("====================================================================")
                break
        else:
            print("Game still valid .... going to next round")
        
        if (current_round_valid and (current_round == number_of_rounds)):
            print("------------------------------------- POSSIBLE GAME LOGGED -------------------------------------")
            possible_games.append(gameId)


def sumOfPossibleGameIDs():
    sum = 0
    for entry in possible_games:
        sum += int(entry)
    return sum

for line in (input_file):
    gameId, results = splitLineToGameIdAndResults(line)
    checkResultsAndSavePossibleGameId(gameId, results)
    
print("========================")
print(f"Sum of possible game IDs: {sumOfPossibleGameIDs()}")