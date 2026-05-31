# day-3-tuples-sets-1
# Day 3 – Tuples and Sets (Combined Exercises)

## 📘 The Exercise Instructions

### Tuples

1. Create a tuple `location` with country, city, district. Print the full tuple and the city using indexing.
2. Create a tuple `rgb` (e.g., 255,128,0). Unpack into red, green, blue and print each.
3. Create a tuple `days` with 7 days. Slice weekdays (Monday–Friday) and print the last day using negative indexing.
4. Create a tuple `student` with name and age. Try to change the age, read the error, and explain it.
5. Create a list of 5 favorite foods with duplicates. Use `.count()` and `.index()`.

### Sets

6. Create `team_a` and `team_b` sets (5 players each, 2 overlapping). Print intersection, union, and difference.
7. Create a list `votes` with 10 entries (some repeats). Convert to set to get unique voters and print the count.
8. Create a set `languages` with 3 languages. Add two more, remove one, check if "Python" is in the set.

### Combining Tuples and Sets

9. Create a tuple of 10 numbers with duplicates. Convert to set, compare lengths, and explain the difference.
10. Create a dictionary `course` with keys: `"title"`, `"topics"` (tuple of 4 topics), `"students"` (set of 5 names). Print the second topic, add a new student, print the full dictionary.

---

## 🧠 My Approach

- **Tuples 1–3:** Used direct creation, indexing, slicing, negative indexing, and unpacking.
- **Tuple 4:** Attempted `student[1] = 30` and observed `TypeError` – wrote a comment explaining tuple immutability.
- **Tuple 5:** Created a list with duplicates, used `.count()` and `.index()` methods.
- **Sets 6–8:** Used `&` (intersection), `|` (union), `-` (difference), `.add()`, `.remove()`, `in` operator.
- **Set 7:** Converted list to set with `set(votes)` and used `len()`.
- **Combining 9:** Converted tuple to set, compared lengths – the difference shows how many duplicates were removed.
- **Combining 10:** Created dictionary with tuple and set as values; accessed tuple element by index; added to set with `.add()`.

---

## 🚧 Challenges I Faced

- Understanding that tuples are **immutable** – trying to change an element raises `TypeError`.
- Remembering the syntax for set operations (`&`, `|`, `-`) vs methods (`intersection()`, etc.). I used symbols, which are concise.
- Keeping track of when to use `[]` (indexing) vs `{}` (set/dict) vs `()` (tuple).
- Adding to a set that is a dictionary value: `course["students"].add("Noah")` – correct, but had to remember not to use `append()`.

---

## ✅ What I Learned

- Tuples are **immutable** – they protect data from accidental changes.
- Sets automatically remove duplicates and are great for membership tests.
- Set operations (intersection, union, difference) are intuitive with symbols.
- Converting between types: `set(list)` removes duplicates, `tuple(set)` loses order.
- Dictionaries can hold **heterogeneous** nested structures – tuples, sets, lists, other dicts.
- Unpacking tuples makes code cleaner than indexing multiple times.

---

## 🖥️ How to Run My Code

1. Save the code as `main.py`.
2. Run `python main.py`.
3. 
4. 
---

## 📅 Part of My AI/ML Learning Journey

Day 3 – now comfortable with tuples and sets. Tuples are useful for fixed configuration data (e.g., model hyperparameters). Sets help with deduplication and fast membership checks (e.g., unique user IDs, visited nodes). Combining them in dictionaries mimics real data structures (e.g., a course with immutable topics and mutable enrolled students).

**Personal reflection from the exercise:**  
*"One thing that confused me: I still have fear that I may forget what I have learned, but so far nothing has confused me. Energy level: 8/10"*

---
*Progress over perfection. Every exercise builds confidence.*
