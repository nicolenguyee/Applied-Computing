countryPop = { "Japan":"127000000",
               "Germany":"81000000",
               "Iran":"77000000",
               "UK":"64000000",
               "Canada":"33000000",
               "Australia":"23000000",
               "USA":"317000000",
               "Bulgaria":"7000000",
               "Sweden":"10000000"}
#extension
country1 = ""
while country1 not in countryPop:
    country1 = input("Enter the name of the first country: ")
    if country1 not in countryPop:
        print("Sorry, can't find that information. Please try again.")
print("I've found the information for you. The population of", country1, "is:", countryPop[country1], "\n")

countrytwo = ""
while countrytwo not in countryPop:
    countrytwo = input("Enter the name of the second country: ")  # <-- changed this!
    if countrytwo not in countryPop:
        print("Sorry, can't find that information. Please try again.")
print("I've found the information for you. The population of", countrytwo, "is:", countryPop[countrytwo], "\n")

# Total population
population = int(countryPop[country1]) + int(countryPop[countrytwo])
print("Combined population of", country1, "and", countrytwo, "is:", population)
