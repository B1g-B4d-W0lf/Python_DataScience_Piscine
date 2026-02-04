import sys
from ft_filter import ft_filter


def main():
    """Take a string and an int and filters the words superior to the int
        in the string and print a list.

       Takes: String, Int

       Return: List"""

    try:
        try:
            if len(sys.argv) != 3:
                raise AssertionError("the arguments are bad")
            text = sys.argv[1]
            n = int(sys.argv[2])

            if not isinstance(text, str) or not isinstance(n, int):
                raise AssertionError("the arguments are bad")

            filtered = \
                list(ft_filter(lambda word: len(word) > n, text.split()))

            print(filtered)

        except ValueError:
            raise AssertionError("the arguments are bad")
    except AssertionError as e:
        print("AssertionError:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
