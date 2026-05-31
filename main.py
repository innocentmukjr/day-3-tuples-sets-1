# ================================================
# DAY 3 EXERCISES - TUPLES AND SETS
# ================================================

# TUPLES

# 1. Create a tuple called 'location' with three values:
#    your country, your city, and your district.
#    Print the full tuple.
#    Print only the city using indexing.

# 2. Create a tuple called 'rgb' with three numbers representing
#    a color (e.g. 255, 128, 0).
#    Unpack it into three variables: red, green, blue.
#    Print each variable on its own line like: "Red: 255"

# 3. Create a tuple called 'days' with 7 days of the week.
#    Slice and print only the weekdays (Monday to Friday).
#    Print the last day using negative indexing.

# 4. Create a tuple called 'student' with your name and age.
#    Try to change the age. Read the error carefully.
#    Write a comment explaining what the error means.

# 5. Create a list of your 5 favorite foods with some duplicates.
#    Count how many times one food appears using .count()
#    Find the index of one food using .index()

# ================================================
# SETS

# 6. Create a set called 'team_a' with 5 player names.
#    Create a set called 'team_b' with 5 player names.
#    Make sure 2 names appear in both teams.
#    Print players in both teams (intersection).
#    Print all players combined (union).
#    Print players only in team_a (difference).

# 7. Create a list called 'votes' with 10 entries
#    where some names repeat (people voting multiple times).
#    Convert it to a set to get unique voters only.
#    Print how many unique voters there are.

# 8. Create a set called 'languages' with 3 programming languages.
#    Add two more languages.
#    Remove one language.
#    Check if "Python" is in the set and print the result.

# ================================================
# COMBINING TUPLES AND SETS

# 9. Create a tuple of 10 numbers with some duplicates.
#    Convert it to a set to remove duplicates.
#    Print the original tuple length and the new set length.
#    What does the difference tell you?

# 10. Create a dictionary called 'course' with keys:
#     "title", "topics", "students"
#     "topics" value should be a TUPLE of 4 topic names
#     "students" value should be a SET of 5 student names
#     Print the second topic from the tuple.
#     Add a new student to the set.
#     Print the full dictionary.


#                                   solution
# tuples
# 1
location = ("Uganda", "Kampala", "Wakiso")
print(location)
print(location[1])

#2 
rbg = (255, 128, 0)
red, green, blue = rbg
print("Red:", red)
print(f"Green: {green}")
print("Blue: ", blue )

#3
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
print(days[1:6])
print(days[-1])

#4
student = ("Mukwaya", 20)
student[1] = 30
print(student)
#TypeError: 'tuple' object does not support item assignment
# this error means once you assign a value to a tuple, at an index, that index will always stand as the value for that tuple, it will never be updated or changed

#5
foods = ["carrot", "rice", "rice", "matooke", "carrot"]
print(foods.count("rice"))
print(foods.index("carrot"))

#sets
#6
team_a = {"Innocent", "Noah", "Sofia", "Julius", "Emma"}
team_b = {"Innocent", "Sofia", "Kellen", "Precious", "Mercy"}
print(team_a & team_b) 
print(team_a | team_b)
print(team_a - team_b)

#7
votes = ["Innocent", "Noah", "Sofia", "Julius", "Emma", "Innocent", "Sofia", "Kellen", "Precious", "Mercy"]
unique_votes = set(votes)
print(len(unique_votes))

#8
languages = {"Python", "C++", "React"}
languages.add("HTML")
languages.add("Java")
languages.remove("Python")
if "Python" in languages:
    print("Yes it is")
else:
    print("No It isn't")

# COMBINING TUPLES AND SETS
#9
numbers = (1,2,3,2,4,5,6,4,5,10)
unique_numbers = set(numbers)
print(len(numbers))
print(len(unique_numbers))
# the difference tells me that sets discard any duplicates immediately noticed and return unique elements only

#10
course = {"topics": ("sets","lists", "dictionaries","tuples"),
          "students": {"Innocent", "Sofia", "Kellen", "Precious", "Mercy"}}
print(course["topics"][1])
course["students"].add("Noah")
print(course)

#one thing that confused me: i still have fear that i may forget what i have learned but so far nothing has confused me
#energy level : 8/10
