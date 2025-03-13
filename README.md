# Expence Tracker CLI
A simple terminal app that allows users to manage and view expenses


# 🚀 Installation
1. Clone the repository:<br>
```bash
git clone https://github.com/LewieJ08/expense_tracker_cli 
cd expense_tracker_cli 
```
2. Install the package:<br>
```bash
pip install .
```
## 📌 Usage
Run the CLI app with:<br>
```bash
expense-tracker
```

## Commands:

```bash
Expense-Tracker> add rent 300
```
Format: add 'description' 'amount'
```bash
Expense-Tracker> update 1
```
Format: update 'Expense ID'<br><br>
Then enter the new data via:

```bash
New Description> 
New Amount>
```
If you would like to only change one, simply enter the same data again😊

```bash
Expense-Tracker> delete 1
```
Format: delete 'Expense ID'

```bash
Expense-Tracker> list
```
Lists all expenses saved
```bash
Expense-Tracker> summary
```
Prints the sum of all expenses

```bash
Expense-Tracker> summary 03
```
Prints the sum of a specified month<br>
Month must be 2 digits and must be an integer 
## Roadmap.sh Project:
https://roadmap.sh/projects/expense-tracker