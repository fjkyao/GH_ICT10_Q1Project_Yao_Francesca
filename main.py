from pyscript import display


restaurant_name = "Baker Bear Bakery" # string
owner_name = "Francesca Yao" # string
year_established = 2009 #float
popular_item_price = 149.50 # float
has_delivery = True # boolean
product_names = ['Strawberry Bunny','Lemon Duck','Blueberry Seal','Pistachio Parakeet','Cookies n Panda Dream', 'Choco Bear'] # list
business_hours = 'Open 7:00am - 10:00pm'
menu_prices = ['$20.00','$15.00','$20.00','$15.00','$20.00','$20.00'] # list
common_allergens = ['eggs','milk','wheat']
tax_rate = 0.05 # floa


display(f"A cozy welcome to {restaurant_name}!", 
target='div1')

display(f"serving you since {year_established}", 
target='div2')

display(f"Our Menu {product_names}{menu_prices}",
target='div4')