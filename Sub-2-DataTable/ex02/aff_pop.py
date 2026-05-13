import matplotlib.pyplot as plt
import sys
from load_csv import load


def format_numbers(pop_val):
    """Takes a string representing a number ending with
     a symbol letter and converts it to a float"""

    if pop_val.endswith('M'):
        return float(pop_val[:-1]) * 1e6
    elif pop_val.endswith('k'):
        return float(pop_val[:-1]) * 1e3
    else:
        return float(pop_val)


def main():
    """Creates a double lined graph showing the evolution of population
     numbers over the years for France & Belgium"""

    try:
        if len(sys.argv) != 2:
            raise AssertionError("Use is: aff_pop.py [path]")
        path = sys.argv[1]
        df = load(path)
        if df is None:
            raise AssertionError(f"Data could not be loaded from {path}")
        france_data = df[df['country'] == 'France']
        belgium_data = df[df['country'] == 'Belgium']
        years = france_data.columns[1:].astype(int)
        mask = years <= 2050
        years = years[mask]
        pop_values_fr = [format_numbers(x) for x
                         in france_data.iloc[0, 1:][mask]]
        pop_values_bl = [format_numbers(x) for x
                         in belgium_data.iloc[0, 1:][mask]]

        plt.plot(years, pop_values_fr, label='France', color='blue')
        plt.plot(years, pop_values_bl, label='Belgium', color='green')

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
        plt.xlim(1790, 2060)
        plt.yticks([20000000, 40000000, 60000000, 80000000],
                   ["20M", "40M", "60M", None])
        plt.legend()
        plt.show()

    except AssertionError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
