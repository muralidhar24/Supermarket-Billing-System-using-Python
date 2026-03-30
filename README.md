# 🛒 XYZ Supermarket Billing System

> A simple console-based supermarket billing application built with **Python**  
> Generates itemized bills with GST calculation and formatted receipts

---

## 📌 About the Project

This is a beginner-friendly Python project that simulates a **supermarket billing counter**. The program allows a customer to:
- Browse available grocery items and prices
- Add multiple items with quantities to a cart
- Automatically calculate total cost, GST, and final payable amount
- Print a neatly formatted bill receipt with date and time

---

## ✨ Features

- 📋 Displays a price list of available items on request
- 🛍️ Interactive item selection with quantity input
- ❌ Handles unavailable item entries gracefully
- 🧾 Generates a formatted bill with serial numbers, item names, quantities, and prices
- 💰 Auto-calculates **5% GST** on the total
- 🕐 Prints the current **date and time** on the bill
- 👤 Personalized with the customer's name

---

## 🗃️ Available Items

| Item | Price |
|------|-------|
| Rice | Rs 20 / kg |
| Sugar | Rs 30 / kg |
| Salt | Rs 20 / kg |
| Oil | Rs 80 / kg |
| Paneer | Rs 110 / kg |
| Maggi | Rs 50 / kg |
| Boost | Rs 90 / each |
| Colgate | Rs 85 / each |

---

## 🚀 How to Run

**Prerequisites:** Python 3.x installed

```bash
# Run the program
python billing.py
```

**Step-by-step usage:**

```
1. Enter your name when prompted
2. Press 1 to view the item price list
3. Press 1 to add an item, or 2 to finish shopping
4. Enter the item name and quantity
5. Repeat for all items
6. Your bill is printed automatically
```

---

## 🖥️ Sample Output

```
--------------------- welcome -----------------------
Enter your name: Rahul
For list of items press 1: 1

Rice      Rs 20/kg
Sugar     Rs 30/kg
...

If you want to buy press 1 or 2 to exit: 1
Enter your item: rice
Enter quantity: 2

If you want to buy press 1 or 2 to exit: 1
Enter your item: oil
Enter quantity: 1

If you want to buy press 1 or 2 to exit: 2

========================= XYZ SUPERMARKET =========================
                            Wanaparthy
Name: Rahul                             Date: 2024-11-10 10:45:22
---------------------------------------------------------------------------
S.No Item            Qty     Price
1     rice            2       40
2     oil             1       80
---------------------------------------------------------------------------
                                                  Total Amount: Rs 120
                                                  GST (5%): Rs 6.0
                                                  Final Amount: Rs 126.0
---------------------------------------------------------------------------
                    Thanks for visiting 😊
---------------------------------------------------------------------------
```

---

## 📁 Project Structure

```
supermarket-billing/
│
└── billing.py        # Main billing program
```

---

## 🧠 Concepts Used

| Concept | Usage |
|---------|-------|
| `input()` | Taking user input |
| `dictionary` | Storing item-price mappings |
| `list` | Tracking items, quantities, prices |
| `while` loop | Continuous item addition until exit |
| `datetime` module | Printing current date and time on bill |
| String formatting | Aligning bill layout |
| Arithmetic | GST and total calculation |

---

## 🔧 Possible Improvements

- [ ] Add input validation (non-integer quantity, empty item name)
- [ ] Support decimal quantities (e.g., 0.5 kg)
- [ ] Save the bill to a `.txt` file
- [ ] Add a discount feature for bulk purchases
- [ ] Build a GUI version using `tkinter`

---

## 👨‍💻 Author

**Dasari Muralidhar**

B.Tech — Computer Science & Engineering

Academic Year 2024–25

---

## 📄 License

This project is for **educational and learning purposes** only.
