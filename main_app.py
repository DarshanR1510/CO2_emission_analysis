import matplotlib.pyplot as plt

def extract_data(country):
    list_len = len(country)
    for length in range(0, list_len):
        if list_len > 3:
            print("ERR: Sorry, at most 3 countries can be entered.")
            return False
        """
        Checking for availability for country in keys
        """
        if country[length] not in emission_dict.keys():
            print(f"ERR: Sorry “{country[length]}” is not a valid country", end="\n\n")
            return False
    else:
        write_line_csv = list(emission_dict.keys())[0].title() + "," + ",".join(list(emission_dict.values())[0]) + "\n"
        for num in range(0, len(country)):
            write_line_csv += country[num].title() + "," + ",".join(
                emission_dict[country[num]]) + "\n"

        with open('Emissions_subset.csv', 'w') as new_file:
            new_file.writelines(write_line_csv)
        print(f"Data successfully extracted for countries " + ", ".join(
            country).title() + " saved into file Emissions_subset.csv", end="\n\n")
    return True


print("A Simple Data Analysis Program")
print()

"""
Step 1: Using the TRY:EXPECT to Handle the Exception in program
"""

try:
    emission_dict = {}
    """
    Reading the countries in lower case.
    """
    with open('Emissions.csv', 'r') as file:
        for data in file.read().split('\n'):
            emission_dict.update({data.split(',')[0].lower(): data.split(',')[1:]})
    print("All data from Emissions.csv has been read into a dictionary.", end="\n\n")
    """
    looping until user don't enter expected input
    """
    while True:
        input_year = input("Select a year to find statistics (1997 to 2010): ")
        if not input_year.isdigit() or not 1997 <= int(input_year) <= 2010:
            print("Sorry that is not a valid year.")
            continue
        else:
            break

    index_of = int()
    lines = []

    for item in emission_dict.values():
        if input_year in item:
            index_of = (item.index(input_year))

    total = 0
    i = 0
    emissions_in_year = []

    for value in emission_dict.values():
        if i != 0:
            total += float(value[index_of])
            emissions_in_year.append(list(emission_dict.values())[i][index_of])
        i += 1

    max_country_index = int(emissions_in_year.index(str(max(float(str_value) for str_value in emissions_in_year))))
    min_country_index = int(emissions_in_year.index(str(min(float(str_value) for str_value in emissions_in_year))))
    average_emissions = total / 195

    max_emission = list(emission_dict.keys())[max_country_index + 1]
    min_emission = list(emission_dict.keys())[min_country_index + 1]

    print(f'In {input_year}, countries with minimum and maximum CO2 emission levels were: [{min_emission}] '
          f'and [{max_emission}] respectively.')
    print(f'Average CO2 emissions in {input_year} were {"%.6f" % round(average_emissions, 6)}')
    print()
    """
    Making it case insensitive and checking for availability for country in keys
    """
    while True:
        visualize_country = input("Select the country to visualize: ").lower()
        if visualize_country in emission_dict.keys():
            number = list(emission_dict.keys()).index(visualize_country)
            plt.plot(list(map(float, list(emission_dict.values())[0])), list(map(float, list(emission_dict.values())[number])))
            plt.title("Year vs Emissions in Capita")
            plt.xlabel("Year")
            plt.ylabel("Emissions in" + visualize_country.title())
            plt.show()
            print()
            break
        else:
            print("Sorry that is not a valid Country.")
            continue
    """
    Making it case insensitive and checking for availability for country in keys - Using power of python to get data into two country variable
    """
    while True:
        try:
            country1, country2 = input("Write two comma-separated countries for which you want to visualize data: ").lower().split(", ")
        except ValueError:
            print("Please write up to two comma-separated countries for which you want to visualize data...")
            continue
        if country1 not in emission_dict.keys() or country2 not in emission_dict.keys():
            print("Sorry that is not a valid Country.")
            continue
        else:
            number1 = list(emission_dict.keys()).index(country1)
            number2 = list(emission_dict.keys()).index(country2)
            plt.plot(list(map(float, list(emission_dict.values())[0])),
                     list(map(float, list(emission_dict.values())[number1])), label=country1)
            plt.plot(list(map(float, list(emission_dict.values())[0])),
                     list(map(float, list(emission_dict.values())[number2])), label=country2)
            plt.title("Year vs Emissions in Capita")
            plt.xlabel("Year")
            plt.ylabel("Emissions in ")
            plt.legend()
            plt.show()
            print()
            break
    """
    Making it case insensitive
    """
    while True:
        input_string = input("Write up to three comma-separated countries for which you want to extract data: ").lower()
        input_country = input_string.split(", ")
        # Looping until user don't enter expected input
        if not extract_data(input_country):
            continue
        else:
            break

except FileNotFoundError:
    print("File not found....")
except IOError:
    print("Output file can’t be saved")