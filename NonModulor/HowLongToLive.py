
# How long do you have to live?

currAge = int(input("What is your current age? "))

year = 90 - currAge

days = 365 * year
weeks = 52 * year
months = 12 * year

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

daysLived = 365 * currAge
weeksLived = 52 * currAge
monthsLived = 12 * currAge

print(f"You have been alive for {daysLived} days, {weeksLived} weeks, and {months} months.")

# Joke
print("LONG LIVE THE EMPIRE!")