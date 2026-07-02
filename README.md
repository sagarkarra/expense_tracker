# 💰 Expense Tracker Using Python Tkinter

A simple and user-friendly **Expense Tracker** application developed using **Python** and **Tkinter**. This desktop application allows users to record daily expenses, manage a budget, calculate total spending, and monitor expenses against a predefined budget limit through an intuitive graphical interface.

---

## 📌 Features

- ➕ Add new expense entries
- 📝 Record expense description and amount
- 🗑️ Delete selected expense entries
- 🔄 Clear all expense records
- 💰 Set and update a custom budget limit
- 📊 Automatically calculate total spending
- 🚨 Budget limit warning when expenses exceed the set budget
- 📋 Display expenses in a tabular format using Treeview
- 🖥️ Simple and user-friendly graphical interface

---

## 🛠️ Technologies Used

- Python 3
- Tkinter
- ttk Widgets
- Messagebox
- Object-Oriented Programming (OOP)

---

## 📂 Project Structure

```text
Expense-Tracker/
│
├── main.py          # Main application source code
└── README.md        # Project documentation
```

---

## 📋 Requirements

- Python 3.x

Tkinter is included with Python, so no additional installation is required.

Verify Tkinter installation:

```bash
python -m tkinter
```

---

## 🚀 How to Run

1. Download or clone the repository.

2. Navigate to the project folder.

3. Run the application:

```bash
python main.py
```

4. The Expense Tracker window will open.

---

## ⚙️ How the Application Works

### Step 1: Set Budget

- Enter your desired budget amount.
- Click **Lock & Apply Budget**.

### Step 2: Add Expenses

- Enter the expense item name.
- Enter the amount spent.
- Click **Add Expense**.

### Step 3: View Expenses

The application displays all expense records in a table with:

- Expense Description
- Amount Spent

### Step 4: Manage Expenses

- Select a row and click **Delete Highlighted Row** to remove an expense.
- Click **Master Reset Ledger Data** to clear all expense records.

### Step 5: Budget Monitoring

- The application automatically calculates the total spending.
- If total expenses exceed the budget, a warning message is displayed.

---

## 📊 Expense Calculation

The total spending is calculated using the following formula:

```text
Total Spending = Sum of All Expense Amounts
```

If:

```text
Total Spending > Budget
```

The application displays a budget warning and highlights the total amount in red.

---

## 🎯 Learning Outcomes

This project demonstrates:

- GUI development using Tkinter
- Object-Oriented Programming (OOP)
- Event-driven programming
- Working with Treeview widgets
- Data validation
- Dynamic calculations
- Budget management
- List data structures
- Message box interactions

---

## 🔮 Future Enhancements

- 💾 Save expense records to a file or database
- 📅 Filter expenses by date
- 📊 Monthly and yearly expense reports
- 📈 Expense charts and graphs
- 🔍 Search expenses
- 🏷️ Expense categories
- ✏️ Edit existing expense entries
- 📤 Export reports to Excel or PDF
- 🌙 Dark mode support
- ☁️ Cloud data synchronization

---

## ⚠️ Limitations

- Expense records are stored only during the current session.
- No database or file storage is implemented.
- Expenses cannot be categorized.
- No user authentication.
- No date-wise expense tracking.
