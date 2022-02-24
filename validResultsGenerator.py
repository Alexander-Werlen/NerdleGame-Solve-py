import re
import os


def createTXTFile(validSolutions):
    if os.path.exists("validSolutions.txt"):
        os.remove("validSolutions.txt")

    with open("validSolutions.txt", "a") as f:
        for expression in validSolutions:
            f.write(expression + "\n")

        pass


def readValidInputs():
    if os.path.exists("validInputs.txt"):
        with open("validInputs.txt", "r") as f:
            validInputs = [line[:-1] for line in f]
            pass
    else:
        raise Exception("No validInputs.txt file found")

    return validInputs


def isValidSolution(expression, avoidedPatterns):

    if avoidedPatterns.search(expression):
        return False
    else:
        return True


def main():

    validInputs = readValidInputs()

    """ 
    Cases in which the eq is not a valid solution>
    1) ^[+*/=0]
    2) [+-][+-]
    3) [=][+/*]
    4) [+*/][+/]
    5) [+/][*]
    6) [=][\d-]+[*+-/]
    7) [\D]0\d

     """
    avoidedPatterns = re.compile(
        r'(^[+*/=0]|[+-][+-]|[=][+/*]|[+*/][+/]|[+/][*]|[=][\d-]+[*+-/]|[\D]0\d)')

    possibleSolutions = [
        expression for expression in validInputs if isValidSolution(expression, avoidedPatterns)]

    createTXTFile(possibleSolutions)


if __name__ == "__main__":
    main()
