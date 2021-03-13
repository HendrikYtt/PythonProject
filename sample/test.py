import os
import io
import csv
import pathlib
from dataprocess import sort_data, remove_strings, fill_properties

countries_list = ["Country"]
file_name = "Countries.csv"
path = str(pathlib.Path(__file__).parent.absolute())
print(path)
is_file_open = False

while True:
    print("Enter country's name, type 'Stop' to stop: ")
    x = input().capitalize()
    if x.lower() == "stop":
        break
    countries_list.append(x)

properties = [["Capital"], ["Population"], ["Area (km2)"], ["Currency"], ["Region"], ["Subregion"]]

fill_properties(properties, countries_list)

sorted_data = sort_data(properties[1][1:], properties[2][1:], countries_list)

biggest_list = ["Country with the biggest population:", sorted_data[0][0], "Country with the largest area:",sorted_data[0][1]]
smallest_list = ["Country with the smallest population:", sorted_data[1][0], "Country with the smallest area:", sorted_data[1][1]]
try:
    with io.open(path + "\Generated csv files\\" + file_name, 'w', encoding="utf-8", newline = '') as f: 
          
        write = csv.writer(f)
        write.writerow(countries_list)
        for i in range(len(properties)):
            write.writerow(properties[i])
        write.writerow("\n\n")
        write.writerow(biggest_list)
        write.writerow(smallest_list)
except:
    is_file_open = True
    print("Please close " + file_name + " to generate a new file.")
if(is_file_open == False):
    print("A csv file named " + file_name + " has been created at " + path + "\Generated csv files")
    os.startfile(path + "\Generated csv files\Countries.csv")