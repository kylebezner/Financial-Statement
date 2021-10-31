# Name: Kyle Bezner

# Description
# As an accounting major, the importance of financial statement analysis is at the forefront of all things we consider
# when releasing financial statements.
# We need to be able to quickly analyze a company’s financial position in order to accurately release an opinion for
# ongoing business decisions.
# This project will help accountants and finance professionals quickly analyze the core financial ratios of a company.

total_sales = float(input("Total sales: "))
total_gross_profit = float(input("Total gross profit: "))
total_cost_of_goods_sold: float = float(input("Cost of goods sold: "))
total_net_profit: float = float(input("Net profit: "))
total_inventory = float(input("Inventory: "))
total_assets = float(input("Total assets: "))
total_current_assets: float = float(input("Total current assets: "))
total_current_liabilities = float(input("Total current liabilities: "))
total_accounts_receivable = float(input("Total accounts receivable: "))
ending_stockholders_equity = float(input("Ending stockholders equity: "))
total_liabilities = float(input("Ending stockholders equity: "))
cash_flow_from_operations = float(input("Cash flow from operations: "))
cash_flow_to_creditors = float(input("Cash flow to creditors: "))
cash_flow_to_stockholders = float(input("Cash flow to stockholders: "))

for count in range(1, 1):
    cash_flow_from_operations = float(input("Cash flow to operations: "))

# Gross Profit - profit a company earns after subtracting costs associated with core products or services
print("Gross Profit", end=" ")
print(total_sales - total_cost_of_goods_sold)

# Gross Profit Percentage- financial ratio that measures gross profit as a percentage
print("Gross Profit Percentage", sep=" ")
print(total_gross_profit / total_sales * 100)

# Net Profit margin - Indicates the efficiency of a company at its cost control
print("Net Profit margin", sep=" ")
print(total_net_profit // total_sales)

# Inventory Turnover - the rate at which a company can sell it's inventory
print("Inventory Turnover", sep=" ")
print(total_cost_of_goods_sold / total_inventory)

# Current Ratio - liquidity ratio that analyzes a companies short term cash obligations
print("Current Ratio", sep=" ")
print(total_current_assets - total_current_liabilities)

# Quick Ratio - liquidity ratio that measures the companies most liquid assets
print("Quick Ratio", sep=" ")
print((total_current_assets - total_inventory) / total_current_liabilities)

# Receivables Turnover - number of times per years a collects its receivables
print("Receivables Turnover", sep=" ")
print(total_sales / total_accounts_receivable)

# Change from end to sep function to help empathize important financial ratios.
# Return on Equity - measures a company's profitability compared to stockholder's equity
print("Return on Equity", sep=" ")
print(total_net_profit / ending_stockholders_equity)

# Return on Assets - measures how efficient a company's uses its assets
print("Return on Assets", sep=" ")
print(total_net_profit / total_assets)

# Cash Flow From Assets - total cash flows related to the assets of a business
print("Cash Flow From Assets", sep=" ")
print(cash_flow_to_creditors + cash_flow_to_stockholders)

# Multiple arithmetic operators are used in this program. Two frequent ones you will see are + and *.
# In python the use of + in the context of arithmetic adds operations together. However, + can be used as an expression
# In python, the use of * creates multiplication of two products. For example print(2 * 2) would output 4.

# Ensuring that the company is solvent through gross profit
if total_cost_of_goods_sold >= total_sales:
    print("Company will fail")
elif total_cost_of_goods_sold < total_sales:
    print("Company has a positive gross profit")
elif total_cost_of_goods_sold == total_sales:
    print("Company is in trouble")
else:
    print("An accounting error has occurred")

# Ensuring the that company can met going concern standards
if total_current_assets == total_current_liabilities:
    print("Further analysis is required")
elif total_current_assets >= total_current_liabilities:
    print("Company has a positive current ratio")
elif total_current_assets < total_current_liabilities:
    print("Company has a negative current ratio")
elif total_current_assets != total_current_liabilities:
    print("An accounting error has occurred")

# Checking to see where the cash flow is coming from
if cash_flow_from_operations >= cash_flow_to_creditors and cash_flow_from_operations >= cash_flow_to_stockholders:
    print("Positive cash flow from on going operations")
else:
    print("Negative cash flow from on going operations")

# Checking the difference between profit and cash flows
if total_net_profit == total_cost_of_goods_sold or total_net_profit >= total_cost_of_goods_sold:
    print("The company days payable outstanding needs to decrease")
else:
    print("The company days payable outstanding is standard")

# Testing if accounting equation has balanced
if not total_assets == total_liabilities + ending_stockholders_equity:
    print("An accounting an error has occurred")
else:
    print("Accounting equation balance")

# While Loop to see if financial statements need to be rounded
while total_sales > 1000000:
    print("Round three decimal points")
    total_sales = total_sales > 9999999
    total_sales = total_sales + 1

# If it the statements need to be rounded
def my_func():
    unrounded_total_sales = 10
    print("Unrounded Sales:", unrounded_total_sales)


round_total_sales = 20
my_func()
print("Rounded Sales:", total_sales)
