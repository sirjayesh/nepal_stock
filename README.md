# nepal_stock
Get Nepal Stock Exchange 'nepse' value of Trading Companies

installation:

pip install nepal_stock

usage:


from nepal_stock import *

# to display all details of the trading company:
dispStock('SBI')

"""
Output:

*** As of 2016-11-03     15:00:00     ***

Name and Symbol : Nepal SBI Bank Limited(SBI)
Address : HATTISAR
Email Address : corporate@nsbl.com.np
Website :
Last Traded Price (Rs.) : 1776.00
Change (Rs.) and (%) : -14(-0.78)
Total Listed Shares : 38,814,528.00
Total Bonus Shares : 8,359,636.00
Paid Up Value (Rs.) : 100
Total Paid Up Value (Rs.) : 3,881,452,800.00
Closing Market Price (Rs.) : 1776.00
Market Capitalization (Rs.) : 68,934,601,728.00
"""

# to get the current stock value of specific trading company
print getStock('ADBL')

"""
Output

*** As of 2016-11-03     15:00:00     ***

Name and Symbol : Agriculture Development Bank Limited(ADBL)
Address : Kathmandu
Email Address : info@adbl.com.np
Website :
Last Traded Price (Rs.) : 645.00 & Change (Rs.) and (%) : 7(1.10)
"""

# to display total bonus share amount of specific trading company
print getTotalBonusShares('NABIL')

# to get the closing value of specific trading company
print getClosingValue('SBI')
