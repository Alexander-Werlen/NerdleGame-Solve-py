import re


def checkValidity(eqStr, avoidedPatterns):
    """ 
    Cases in which the eq is not a valid input>
    1) ^[*/=]
    2) [=][/*]
    3) [+/][*/]
    4) [=][\d-+]+[*+-/]

     """
    try:
        split = eqStr.split("=")
        if len(split) != 2:
            return False

        if eval(split[0]) != eval(split[1]):
            return False

        if avoidedPatterns.search(eqStr):
            return False
        else:
            return True
    except Exception:
        return False


def reduceToValidExpressions():
    import os

    validExpressions = []

    avoidedPatterns = re.compile(
        r'(^[*/=]|[=][/*]|[+/][*/]|[=][\d+-]+[*+-/])')

    # Reading possibleInputs file and copying the valid expressions onto a list
    with open("possibleInputs.txt", "r") as f:
        for expression in f:

            if checkValidity(expression[:-1], avoidedPatterns):
                validExpressions.append(expression)
        pass

    # Writing the valid expressions on the list onto another file
    if os.path.exists("validInputs.txt"):
        os.remove("validInputs.txt")

    with open("validInputs.txt", "a") as f:
        for expression in validExpressions:
            f.write(expression)

        pass

    return


def main():
    reduceToValidExpressions()

    return


if __name__ == "__main__":
    main()
