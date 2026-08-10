# Name: Niyati Sharma
# Description: Personal Information Manager - A Python program that stores, calculates,
#              validates, and displays personal information using string formatting.

# Welcome message
print("=" * 40)
print("     PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()

# Store static information
name = "Niyati Sharma"
age = 20
city = "Safidon"
hobby = "coding and web dev"

# Get user input
print("Please tell me about yourself:")
print("-" * 30)

favorite_food = input("What's your favorite food? ").strip()
while favorite_food == "":
    print("Please enter a valid food!")
    favorite_food = input("What's your favorite food? ").strip()

favorite_color = input("What's your favorite color? ").strip()
while favorite_color == "":
    print("Please enter a valid color!")
    favorite_color = input("What's your favorite color? ").strip()

# Calculate age in months
age_in_months = age * 12

# Display all information
print()
print("=" * 40)
print("         YOUR INFORMATION")
print("=" * 40)
print()

print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print()
print(f"Favorite Food: {favorite_food.title()}")
print(f"Favorite Color: {favorite_color.title()}")
print()

# Goodbye message
print("=" * 40)
print("Thanks for using this program!")
print("=" * 40)