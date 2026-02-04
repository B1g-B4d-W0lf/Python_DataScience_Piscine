import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
	try:
		if not isinstance(start, int) or not isinstance(end, int) \
			or not isinstance(family, list):
			raise AssertionError("Invalid format in arguments")
		arr = np.array(family)
		print(f"My shape is : {arr.shape}")
		arr = arr[start:end]
		print(f"My new shape is : {arr.shape}")
		# print(arr)
		return (arr)
	except AssertionError as e:
		print(e)
	except ValueError as e:
		print("Value Error caught, please check arguments")