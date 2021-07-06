import matplotlib.pyplot as plt
import pandas as pd

data_dict = {}

with open('./Emissions.csv', mode='r') as csv_data:
    for data in csv_data.read().split('\n'):
        data_dict.update({data.split(',')[0] : data.split(',')[1:]})

#extracting year list
year_list = (list(data_dict.values()))[0]
year_list = list(map(int, year_list))

#extracting country names
country_list = (list(data_dict.keys()))[1:]

#getting year input
def input_year_fun():
    global input_year
    input_year = int(input("Select a year to find statistics (1997 to 2010): "))
    return input_year
     
try:
    input_year_fun() 
    while input_year not in year_list:
        print("Please enter year from 1998 to 2010 only")
        input_year_fun()

except ValueError as error:
    print(error)
    print("Please enter year from 1998 to 2010 only")
    
        
#extracting the index of the year
year_index = year_list.index(input_year)


#Creating list of emission in individual year
single_year_ems = []
each_year_ems = (list(data_dict.values()))[1:]

for i in each_year_ems:
    single_year_ems.append(float(i[year_index]))


#Analysis functions
def find_country(ems_value):
    ems_index = single_year_ems.index(ems_value)
    ems_country = country_list[ems_index]
    return ems_country

#finding minimum and maximum emission in specific year and it's country name
min_ems_country = find_country(min(single_year_ems))
max_ems_country = find_country(max(single_year_ems))

#finding avarage of emission in specific year
avarage_ems = sum(single_year_ems)/len(single_year_ems)

#Final output:
print()
print(f'In {input_year}, countries with minimum and maximum CO2 emission levels were: [{min_ems_country}] and [{max_ems_country}] respectively.')
print(f'Avarage CO2 emissions in {input_year} were {avarage_ems}')
print()


#getting multiple country input
multi_input_country = None

def input_country_fun():
    global multi_input_country
    input_country = input("Select the countries to compare and visualize data [separate with comma ', ']: ")
    multi_input_country = list(input_country.split(', '))               #spliting input
    return multi_input_country    

input_country_fun() 

x_values = year_list
y_values = [data_dict[i] for i in multi_input_country]                  #fatching emission data of selected countries in list
y_ems_flt = []

def y_ems_fun():
    global y
    for i in y_values:
        for single_y_ems in i:
            y_ems_flt.append(float(single_y_ems))                       #converting fatched data from str to float
    y = [y_ems_flt[i:i + 14] for i in range(0, len(y_ems_flt), 14)]     #creating sublist of 14 entries of each country
    return y

y_ems_fun()

# ploting data for visualization
plt.title("Year vs Emissions in capita")

plt.xlabel("Year")
plt.ylabel(f"Emissions in {multi_input_country[0]} and {multi_input_country[1]}")

df = pd.DataFrame({
    'x_values': year_list,
    'y1_values': y[0],
    'y2_values': y[1]
})

plt.plot('x_values', 'y1_values', data=df, color='blue', linewidth=2, label=multi_input_country[0])
plt.plot('x_values', 'y2_values', data=df, color='orange', linewidth=2, label=multi_input_country[1])

plt.legend()
plt.show()