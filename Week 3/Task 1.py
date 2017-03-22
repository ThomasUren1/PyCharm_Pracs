# def main():
#     no_months = float(input("How many months? "))
#     income_monthly = []
#     i = 0
#     total = 0
#     while no_months > 0:
#         income = float(input("Enter the income for month #: "))
#         income_monthly.append(income)
#         no_months -= 1
#         total += income
#
#     print(income_monthly)
#     print(no_months)
#     print(total)
#
# main()

"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    global incomes
    global no_months
    incomes = []
    no_months = int(input("How many months? "))

    for month in range(1, no_months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)


def report():
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, no_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
report()