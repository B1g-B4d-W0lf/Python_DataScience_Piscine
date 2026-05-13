import matplotlib.pyplot as plt
import sys
from load_csv import load


def main():
    """Creates a dot graph showing the link between life expectancy
     and gross national product"""

    try:
        df_product = load("../income_per_person_gdppercapita_\
                          ppp_inflation_adjusted.csv")
        df_life = load("../life_expectancy_years.csv")
        if df_life is None or df_product is None:
            raise AssertionError("Data could not be loaded")
        year_data_life = df_life['1900']
        year_data_product = df_product['1900']

        plt.scatter(year_data_product, year_data_life)

        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.xscale('log')
        plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
        plt.yticks(range(15, 56, 5), range(15, 56, 5))
        plt.legend()
        plt.show()

    except AssertionError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
