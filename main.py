from pyscript import display, document


restaurant_name = "Baker Bear Bakery" # string
owner_name = "Francesca Yao" # string
year_established = 2009 #integer
popular_item_price = 149.50 # float
has_delivery = True # boolean
product_names = ['Strawberry Bunny','Lemon Duck','Blueberry Seal','Pistachio Parakeet','Cookies n Panda Dream', 'Choco Bear'] # list
menu_prices = ['20.00','15.00','20.00','15.00','20.00','20.00'] # list
common_allergens = ['eggs','milk','wheat']
business_hours = 'Open 7:00am - 10:00pm'
tax_rate = 0.05 # float

display(f"{product_names[0]} - ${menu_prices[0]}", target='menu_list')
display(f"{product_names[1]} - ${menu_prices[1]}", target='menu_list')
display(f"{product_names[2]} - ${menu_prices[2]}", target='menu_list')
display(f"{product_names[3]} - ${menu_prices[3]}", target='menu_list')
display(f"{product_names[4]} - ${menu_prices[4]}", target='menu_list')
display(f"{product_names[5]} - ${menu_prices[5]}", target='menu_list')


# ORDER SUMMARY/CUSTOMER DETAILS

def place_order(e):
    c_name = document.getElementById('cname').value
    c_address = document.getElementById('address').value
    c_number = document.getElementById('cnumber').value

    customer_details = f'''
        Student Profile
        Order for: {c_name}
        Address: {c_address}
        Contact number: {c_number}
        '''
    display(customer_details, target='summary')
