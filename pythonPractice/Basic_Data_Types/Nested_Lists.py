if __name__ == '__main__':
    grades = []
    minimum = 1000
    secondMinimum = 1000
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append([name,score])
        if score < minimum:
            secondMinimum = minimum
            minimum = score
        elif score < secondMinimum and score != minimum:
            secondMinimum = score 

    lowestScores = [x[0] for x in grades if x[1] == secondMinimum]
    for name in sorted(lowestScores):
        print(name)
