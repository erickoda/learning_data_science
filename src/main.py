from fetch_data import fetch_housing_data
from load_data import load_housing_data

def main():
    fetch_housing_data()
    housing = load_housing_data()

    print(housing.head())
    print()
    
    print(housing.info())
    print()

    return

# Execute the main function when the script is run
if __name__ == "__main__":
    main()


    