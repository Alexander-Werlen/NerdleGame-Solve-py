
def getAllPossibleStrings(possibleCharacters, numberOfTiles):
    # Funtion creates a txt file with all possible strings written on it by line
    # Input possibleCharacters is a string with all the possible characters without any split Ex: "1234567890=+*-"

    import itertools
    import os

    if os.path.exists("possibleInputs.txt"):
        os.remove("possibleInputs.txt")

    with open("possibleInputs.txt", "a") as f:

        def foo(l):
            yield from itertools.product(*([l] * numberOfTiles))

        for x in foo(possibleCharacters):
            f.write(''.join(x) + "\n")

        pass

    return


def main():
    getAllPossibleStrings("0123456789+-*/=", 6)

    return


if __name__ == "__main__":
    main()
