#Author = Tom Uren;


sales = 0;
total = 0;
i = 0;

sales = float(input("Enter sales: $"))

while True:
    total = total + sales
    i = i + 1
    cont = input("Add another item? (Y or N)")
    if cont == ("n" or "N"):
        break
    else:
        sales = float(input("Enter sales: $"))


if total >= 100:
    discount = total * 0.9
    discounted = total * 0.1
else:
    discount = total;

print("Total number of items: ",format(i))
print("Total cost of: $",format(discount))
if total >= 100:
    print("Total anount saved from our 10% discount over $100: $",format(discounted))

