import sys


def count_char(string):
    """ Makes a count of the different char in a string and prints results

        Takes : String

        Return : Success(0) or Failure(1) """

    total = len(string)
    UC = sum(1 for char in string if char.isupper())
    LC = sum(1 for char in string if char.islower())
    dgt = sum(1 for char in string if char.isdigit())
    spc = sum(1 for char in string if char.isspace())
    punc_char = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    punc = sum(1 for char in string if char in punc_char)

    print(f"The text contains {total} characters:")
    print(f"{UC} upper letters")
    print(f"{LC} lower letters")
    print(f"{punc} punctuation marks")
    print(f"{spc} spaces")
    print(f"{dgt} digits")


def main():

    try:
        if len(sys.argv) > 2:
            raise AssertionError("Use is : >$ python building.py [arg]")
        if (len(sys.argv) == 1 or len(sys.argv[1]) == 0):
            string = input("What is the text to count?\n")
            string += "\n"
        if (len(sys.argv) == 2 and len(sys.argv[1]) > 0):
            string = sys.argv[1]
    except AssertionError as e:
        print(e)
        sys.exit(1)

    count_char(string)


if __name__ == "__main__":
    main()
