import sys


def encode(string):
    """Encode an alphanumeric string in morse

       Takes: String

       Returns: List """

    NESTED_MORSE = {'A': '.-',
                    'B': '-...',
                    'C': '-.-.',
                    'D': '-..',
                    'E': '.',
                    'F': '..-.',
                    'G': '--.',
                    'H': '....',
                    'I': '..',
                    'J': '.---',
                    'K': '-.-',
                    'L': '.-..',
                    'M': '--',
                    'N': '-.',
                    'O': '---',
                    'P': '.--.',
                    'Q': '--.-',
                    'R': '.-.',
                    'S': '...',
                    'T': '-',
                    'U': '..-',
                    'V': '...-',
                    'W': '.--',
                    'X': '-..-',
                    'Y': '-.--',
                    'Z': '--..',
                    '0': '-----',
                    '1': '.----',
                    '2': '..---',
                    '3': '...--',
                    '4': '....-',
                    '5': '.....',
                    '6': '-....',
                    '7': '--...',
                    '8': '---..',
                    '9': '----.',
                    ' ': '/'}

    morse_res = []
    for char in string.upper():
        if char in NESTED_MORSE:
            morse_res.append(NESTED_MORSE[char])
        else:
            raise AssertionError(f"unsupported character '{char}'")
    return (morse_res)


def main():
    try:
        if len(sys.argv) != 2 or len(sys.argv[1]) == 0 \
                or not isinstance(sys.argv[1], str):
            raise AssertionError("the arguments are bad")
        arg = sys.argv[1]
        result = encode(arg)
        print(' '.join(result))

    except AssertionError as e:
        print("AssertionError:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
