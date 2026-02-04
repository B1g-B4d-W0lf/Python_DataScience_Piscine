import sys

def whatis(number):
	if number % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")


try :
	if len(sys.argv) != 2:
		raise AssertionError("AssertionError: more than one argument is provided")
	if sys.argv[1][0] == '-' or sys.argv[1][0] == '+':
		assert (sys.argv[1][1:].isdigit()), "AssertionError: argument is not an integer"
	else:
		assert (sys.argv[1].isdigit()), "AssertionError: argument is not an integer"
except AssertionError as e:
	print(e)
	sys.exit(1)

number = int(sys.argv[1])

whatis(number)

