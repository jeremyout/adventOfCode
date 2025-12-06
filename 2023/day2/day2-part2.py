input_file = open("input.txt", "r")
# input_file = open("example_input.txt", "r")

power_per_game = []

def splitLineToGameIdAndResults(line):
    split_line = line.split(":")
    results = split_line[1].strip().split(";")
    return results

def getMinimumCountsPerColor(results):
    min_count_needed = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for result in results:
        result = result.strip().split(", ")
        
        for game_round in result:
            game_round = game_round.split(" ")
            color_count = game_round[0]
            color = game_round[1]
            if (int(color_count) > min_count_needed[color]):
                min_count_needed[color] = int(color_count)
        print(f"Current round results: {min_count_needed}")
    return min_count_needed



def calcualtePowerOfCubesPerGame(min_counts):
    return min_counts["red"] * min_counts["green"] * min_counts["blue"]

def sumOfGamePowers():
    sum = 0
    for entry in power_per_game:
        sum += entry
    return sum

for line in (input_file):
    gameId = line.split(':')
    gameId = gameId[0].split()
    results = splitLineToGameIdAndResults(line)
    print(f"Game ID being checked: {gameId[1]}")
    min_count_per_color = getMinimumCountsPerColor(results)
    print(f"Minimum count required per color: {min_count_per_color}")
    print(f"Power calculated for Game {gameId[1]}: {calcualtePowerOfCubesPerGame(min_count_per_color)}")
    power_per_game.append(calcualtePowerOfCubesPerGame(min_count_per_color))
    
print("========================")
print(f"Total Power of minimum cube quantities: {sumOfGamePowers()}")