from datetime import datetime

print("--------------------- welcome -----------------------")
name = input("Enter your name: ")

lists = '''
Rice      Rs 20/kg
Suger     Rs 30/kg
Salt      Rs 20/kg
Oil       Rs 80/kg
Paneer    Rs 110/kg
Maggi     Rs 50/kg
Boost     Rs 90/each
Colgate   Rs 85/each
'''

items = {
    'rice': 20,
    'suger': 30,
    'salt': 20,
    'oil': 80,
    'paneer': 110,
    'maggi': 50,
    'boost': 90,
    'colgate': 85
}

pricelist = []
ilist = []
qlist = []
plist = []
totalprice = 0

option = int(input("For list of items press 1: "))
if option == 1:
    print(lists)

while True:
    inp1 = int(input("If you want to buy press 1 or 2 to exit: "))
    if inp1 == 2:
        break

    item = input("Enter your item: ").lower()
    quantity = int(input("Enter quantity: "))

    if item in items:
        price = quantity * items[item]
        totalprice += price

        ilist.append(item)
        qlist.append(quantity)
        plist.append(price)
    else:
        print("❌ Item not available")

# -------- BILL --------
gst = totalprice * 0.05
finalamount = totalprice + gst

print("\n", 25*"=", "XYZ SUPERMARKET", 25*"=")
print(28*" ", "Wanaparthy")
print("Name:", name, 20*" ", "Date:", datetime.now())
print(75*"-")
print("S.No", "Item", 10*" ", "Qty", 5*" ", "Price")

for i in range(len(ilist)):
    print(i+1, 5*" ", ilist[i], 10*" ", qlist[i], 5*" ", plist[i])

print(75*"-")
print(50*" ", "Total Amount: Rs", totalprice)
print(50*" ", "GST (5%): Rs", gst)
print(50*" ", "Final Amount: Rs", finalamount)
print(75*"-")
print(20*" ", "Thanks for visiting 😊")
print(75*"-")
