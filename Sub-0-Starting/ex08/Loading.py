import time
import os


def format_time(duration):
    minutes, seconds = divmod(int(duration), 60)
    return (f"{minutes:02d}:{seconds:02d}")


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    start_time = time.time()

    ter_size = os.get_terminal_size().columns
    bar_size = ter_size - 40

    for i, value in enumerate(lst, start=1):
        percent_bar = int(i / total * bar_size)
        bar = f"{'█' * percent_bar:<{bar_size}}"
        percent = percent_bar * 100 // bar_size

        elapsed_time = time.time() - start_time
        if elapsed_time < 0.1:
            speed = 0
            expected_time = 0
        else:
            speed = i / elapsed_time
            expected_time = (total - i) / speed

        right_time = format_time(elapsed_time)
        right_exp_time = format_time(expected_time)

        res = len(str(total))

        bar_write = f"{percent:3.0f}%|{bar}| {i:>{res}}/{total}"
        extra_write = f"[{right_time}>{right_exp_time}, {speed:3.2f}it/s]"

        print("\r" + " " * ter_size, end="")
        print(f"\r{bar_write} {extra_write}", end="", flush=True)
        yield value


# def main():
#     for _ in ft_tqdm(range(0, 333)):
#         pass


# if __name__ == "__main__":
#     main()
