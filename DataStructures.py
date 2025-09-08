## Part 1: Lists

#1. Create a list of 10 numbers.
numbers = [5, 24, 32, 79, 100, 15, 63, 81, 97, 11]
#2. Print the first, last, and middle number.
print(numbers[0:3])
#3. Add a new number to the end of the list.
numbers.append(7)
#4. Replace the third number with 99.
numbers[2] = 99
#5. Loop through the list and print only the even numbers.
for i in numbers:
    if i % 2 == 0:
        print(i)

## Part 2: Dictionaries

#1. Create a dictionary of 5 countries and their capitals.
countries_capitals  = {
    "United States": "Washington DC"
    "Russia": "Moscow"
    "Japan": "Tokyo"
    "Egypt": "Cairo"
    "Mexico": "Mexico City"
}
#2. Print the capital of 2 countries.
print("The capital of Japan is " + str(countries_capitals["Japan"]))
print("The capital of Egypt is " + str(countries_capitals["Egypt"]))
#3. Add a new country-capital pair.

#4. Change the capital of one country.

#5. Loop through and print all countries and capitals.

