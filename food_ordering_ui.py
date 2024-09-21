#user interface to the main menu
import data
import functions
def show_main_menu():
  my_order=[]
  while True:
    print("Jayasri's diner") #edit to show your name
    print("__________")
    print('N for a new order')
    print("C to change your current order")
    print('X to close orders and print the check')
    print('R to reset the order')
    print('Q for quit')
    user_menu_choice = input('Your choice: ')
    if user_menu_choice in 'Qq':
      break
    elif user_menu_choice in 'Xx':
      print('This option prints the list of items ordered, extended price, total, Taxes, and Grand total ')
      print_check(my_order)
    elif user_menu_choice in 'Cc':
      my_order=change_order(my_order)
    elif user_menu_choice in 'Nn':
      print('New order')
      while input('Add an item? y/n: ') in 'Yy':
        ordered_item = functions.get_item_number()
        my_order.append(ordered_item)
      print('Your Current order is', my_order)  
    elif user_menu_choice in 'Rr':
       my_order=[]
       print('Order is reset')
    else:
      make_order(user_menu_choice.upper())  #calls a function for adding to the orders
    

def make_order(order):
  print("New order")
  while True:
    
    user_selection = functions.get_item_number()
    if user_selection == 'done':
        break
    # Split user_selection into item_code and quantity
    item_code, quantity = user_selection.split()  
    
    quantity = int(quantity)  # Convert quantity to an integer
    item_name, item_price = functions.get_item_information(item_code)
    item_price = int(item_price)  # Ensure price is an integer
        
    # Append the correct tuple to the order (item_code, item_name, quantity, item_price)
    order.append((item_code, item_name, quantity, item_price))
        
        # Debugging statement to ensure correct values are added to the order
    print(f"Adding to order: {item_code}, {item_name}, {quantity}, {item_price}")
    
  return order

def close_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)

def change_order(order):
    print("Change order")
    functions.display_current_order(order)
    item_code = input("Enter the item code you want to change: ")
    for i, (code, name, qty, price) in enumerate(order):
        if (code+name) == item_code:
            new_quantity = (input(f"Enter new item for {code+name} and quantity: "))
            order[i]=new_quantity
            
            print(order)
            #order[i] = (code+name, new_quantity, price)
            break
    return order

def print_check(order):
    print(" Your total is:")
    sub_total = functions.calculate_subtotal(order)
    tax = sub_total * 0.07  # Assuming 7% tax
    total = sub_total + tax
    functions.display_current_order(order)
    print(f"Subtotal: ${sub_total:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")  


if __name__ == '__main__':
    #initialize the lists
    drinks = []
    appetizers = []
    salads = []
    entrees = []
    dessert= []
      #print(functions.get_item_information('D1'))
    show_main_menu()


