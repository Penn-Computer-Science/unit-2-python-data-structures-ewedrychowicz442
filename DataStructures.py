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
    "United States": "Washington DC",
    "Russia": "Moscow",
    "Japan": "Tokyo",
    "Egypt": "Cairo",
    "Mexico": "Mexico City"
}
#2. Print the capital of 2 countries.
print("The capital of Japan is " + str(countries_capitals["Japan"]))
print("The capital of Egypt is " + str(countries_capitals["Egypt"]))
#3. Add a new country-capital pair.
countries_capitals["Canada"] = "Ottawa"
#4. Change the capital of one country.
countries_capitals["Canada"] = "Vancouver"
#5. Loop through and print all countries and capitals.
for country, capital in countries_capitals.items():
    print(f"Country: {country}, Capital: {capital}")

##Part 3: Sets

#1. Create a set of your favorite fruits.
favorite_fruits = {"Apples", "Pomegranate", "Watermelon", "Strawberries", "Raspberries"}
#2. Add a new fruit, then remove one.
favorite_fruits.add("Cherries")
favorite_fruits.remove("Watermelon")
#3. Create another set of fruits your friend likes.
fruits_2 = {"Pineapple", "Apples", "Mango", "Cherries"}
#4. Print:
#   - Fruits you both like (intersection).
intersection_set = favorite_fruits.intersection(fruits_2)
print(f"We both like: {intersection_set}")
#   - Fruits only you like (difference).
difference_set = favorite_fruits.difference(fruits_2)
print(f"Only I like: {difference_set}")
#   - All fruits either of you like (union).
union_set = favorite_fruits.union(fruits_2)
print(f"All the fruits we like combined: {union_set}")

##Part 4: Tuples

#1. Create a tuple of 5 colors.
colors = ("Red", "Blue", "Purple", "Yellow", "Green")
#2. Print the first and last color.
print("First Color: ", colors[0])
print("Last Color: ", colors[-1])
#3. Loop through the tuple and print each color.
for item in colors:
    print(item)
#4. Try to change one color (note the error).
colors[3] = "Orange"
###TypeError: 'tuple' object does not support item assignment