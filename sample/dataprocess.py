import requests

def fill_properties(properties, countries_list):
    for i in range(1, len(countries_list)):
        try:
            response = requests.get("https://restcountries.eu/rest/v2/name/"+countries_list[i]).json()[0]
            print(response["capital"])
            properties[0].append(response["capital"])
            properties[1].append(response["population"])
            properties[2].append(response["area"])
            properties[3].append(response["currencies"][0]["name"])
            properties[4].append(response["region"])
            properties[5].append(response["subregion"])
        except:
            print("An exception occurred")
            countries_list[i] = "Invalid country's name: " + countries_list[i]
            properties[0].append("ERROR")
            properties[1].append("ERROR")
            properties[2].append("ERROR")
            properties[3].append("ERROR")
            properties[4].append("ERROR")
            properties[5].append("ERROR")

def remove_strings(number_list):
    no_integers = [x for x in number_list if not isinstance(x, str)]
            
    return no_integers

def sort_data(list1, list2, countries_list):
    print("Population " + str(remove_strings(list1)))
    print("Area " + str(remove_strings(list2)))

    biggest_population = max(remove_strings(list1))
    largest_area = max(remove_strings(list2))
    print("Biggest population" + str(biggest_population))
    print("Biggest area" + str(largest_area))

    smallest_population = min(remove_strings(list1))
    smallest_area = min(remove_strings(list2))
    print("Smallest population" + str(smallest_population))
    print("Smallest area" + str(smallest_area))

    biggest_population_index = list1.index(biggest_population)
    largest_area_index = list2.index(largest_area)

    smallest_population_index = list1.index(smallest_population)
    smallest_area_index = list2.index(smallest_area)
    print(smallest_population_index)

    biggest_country = [countries_list[biggest_population_index+1], countries_list[largest_area_index+1]]
    smallest_country = [countries_list[smallest_population_index+1], countries_list[smallest_area_index+1]]

    print(biggest_country)
    print(smallest_country)
    return biggest_country, smallest_country