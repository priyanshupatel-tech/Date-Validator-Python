# 📅 Date Validator

A Python program that validates whether a given date (day, month, year) is a **real, valid calendar date** — including proper leap year handling and month-wise day limits.

---

## 🚀 Features

- ✅ Validates day, month, and year inputs
- 🗓️ Handles **leap year** logic correctly
- 📆 Checks correct number of days per month (28/29/30/31)
- ❌ Returns clear valid/invalid result
- 🔢 Covers edge cases like Feb 29 in leap years

---

## 🛠️ Technologies Used

- **Language:** Python 3
- **Concepts:** Conditional Statements (if-else), Leap Year Logic, Input Validation

---

## 📌 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/priyanshupatel-tech/Date-Validator-Python.git
   cd Date-Validator-Python
   ```

2. Run the program:
   ```bash
   python Project8.py
   ```

3. Enter day, month, and year when prompted.

---

## 🖥️ Sample Output

```
Enter Day: 29
Enter Month: 2
Enter Year: 2024

✅ Valid Date — 29/02/2024 is a real date (2024 is a leap year)
```

```
Enter Day: 31
Enter Month: 4
Enter Year: 2023

❌ Invalid Date — April has only 30 days
```

---

## 🧠 Logic Breakdown

**Leap Year:**
- Divisible by 400 → Leap year
- Divisible by 4 but NOT by 100 → Leap year
- Otherwise → Not a leap year

**Month Day Limits:**
| Months | Max Days |
|--------|----------|
| January, March, May, July, August, October, December | 31 |
| April, June, September, November | 30 |
| February (normal year) | 28 |
| February (leap year) | 29 |

---

## 💡 Learning Outcomes

- Implementing real-world date validation logic
- Understanding leap year calculation
- Writing clean, readable conditional code in Python

---

## 👨‍💻 Author

**Priyanshu Patel**
- 🔗 [LinkedIn](https://www.linkedin.com/in/priyanshupatel-tech/)
- 💻 [GitHub](https://github.com/priyanshupatel-tech)
