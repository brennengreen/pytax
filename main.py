import profile as us
import taxmath as tmath

user_state = "Kentucky"
user_city = "Georgetown"
user_zip = "40324"
sale_price = 19.95

'''
COMMENTED FOR TESTING PURPOSES, UNCOMMENT IF PUSHING TO REPO
# Using while loops to continuously prompt the user for input in the case they just hit enter/return
while len(user_state) < 1:
    user_state = input("Please provide a valid state: ")
while len(user_city) < 1:
    user_city = input("Please provide a valid city: ")
while len(user_zip) < 1:
    user_zip = input("Please provide a valid zip code: ")
while sale_price <= 0:
    sale_price = input("How much does the item cost: ")
'''

# In order to use the profiles created by profile.py you must create a user profile
# TO DO: Create profile based on whether or not the sale was made to a US or international customer
# (Implementation needed outside of main.py)
user_profile = us.TaxProfile(user_city, user_state, user_zip)

# Example of the main purpose of taxcalculator, find the total sale cost including all tax rates
total_sale = round(tmath.calc_total_sale(user_profile.get_rate().combined_rate,
                                         float(sale_price)), 2)

# A contrary to the intended purpose of this program, you may also use remove_tax ala taxmath to remove the total
# sales tax from a total sale cost, just in case you needed the original price
orig_sale_total = round(tmath.remove_tax(user_profile.get_rate().combined_rate,
                                         total_sale))

# Printed for example
print("The total sale cost is: {0}, The og price was {1}".format(total_sale, orig_sale_total))
