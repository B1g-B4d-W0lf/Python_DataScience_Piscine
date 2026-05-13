import matplotlib.pyplot as plt
import sys
from load_csv import load


def main():
    """Creates a graph about life expectancy in France"""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("Use is: aff_life.py [path]")
        path = sys.argv[1]
        df = load(path)
        if df is None:
            raise AssertionError(f"Data could not be loaded from {path}")
        france_data = df[df['country'] == 'France']
        years = france_data.columns[1:]
        life_expect = france_data.iloc[0, 1:]

        plt.plot(years, life_expect, label='France')
        plt.title("France Life expectancy projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.xticks(years[::40])
        plt.yticks(range(30, 100, 10))
        plt.show()

    except AssertionError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
