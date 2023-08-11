import json

def display_items(vm_data):
    print("Available items:")
    print("Item Code\tName\t\tQuantity\t\tPrice")
    for i, item in enumerate(vm_data["items"], 1):
        print(f"{i}.\t{item['name']}\t{item['quantity']} \t{item['price']}MMK")

def update_quantity(vm_data, choice, quantity):
    vm_data["items"][choice - 1]["quantity"] -= quantity

def calculate_total(user_choices, vm_data):
    total_amount = 0
    for choice, quantity in user_choices.items():
        item = vm_data["items"][choice - 1]  
        total_amount += item["price"] * quantity
        update_quantity(vm_data, choice, quantity)
    return total_amount
user_transactions = []

def main():
    
    with open("/Users/Acer/Desktop/python/.vscode/vm1.json") as file:
        vm1_data = json.load(file)
    with open("/Users/Acer/Desktop/python/.vscode/vm2.json") as file:
        vm2_data = json.load(file)
    with open("/Users/Acer/Desktop/python/.vscode/vm3.json") as file:
        vm3_data = json.load(file)
    with open("/Users/Acer/Desktop/python/.vscode/vm4.json") as file:
        vm4_data = json.load(file)
    with open("/Users/Acer/Desktop/python/.vscode/vm5.json") as file:
        vm5_data = json.load(file)
    
    # new_items_vm1 = [
    # { "name": "New Item 1", "price": 1500, "quantity": 8 },
    # { "name": "New Item 2", "price": 2000, "quantity": 5 }
    # ]
    # vm1_data["items"].extend(new_items_vm1)
    print("Welcome to the Vending Machines!")
    while True:
        print("\nSelect a vending machine:")
        print("1. Vending Machine 1")
        print("2. Vending Machine 2")
        print("3. Vending Machine 3")
        print("4. Vending Machine 4")
        print("5. Vending Machine 5")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            display_items(vm1_data)
            user_choices = {}
            while True:
                item_code = int(input("Enter item code (0 to finish): "))
                if item_code == 0:
                    break
                quantity = int(input("Enter quantity: "))
                user_choices[item_code] = quantity
            total_amount = calculate_total(user_choices, vm1_data)
            print(f"Total amount: {total_amount}MMK")
            payments = int(input("Enter the amount you paid: "))
            amount = payments - total_amount
            if payments >= total_amount:
                  print("Your Remaining Money is: ",amount)
            else:
                 print("Your Balance in insufficient....")  
            transaction = {
        "date": "2023-08-11T20:31:37+06:30",   
        "vending_machine": choice,
        "items": user_choices,
        "total_amount": total_amount
         }
            user_transactions.append(transaction)
        elif choice == "2":
            display_items(vm2_data)
            user_choices = {}
            while True:
                item_code = int(input("Enter item code (0 to finish): "))
                if item_code == 0:
                    break
                quantity = int(input("Enter quantity: "))
                user_choices[item_code] = quantity
            total_amount = calculate_total(user_choices, vm2_data)
            print(f"Total amount: {total_amount}MMK")
            amount = payments - total_amount
            if payments >= total_amount:
                  print("Your Remaining Money is: ",amount)
            else:
                 print("Your Balance in insufficient....")  
            transaction = {
        "date": "2023-08-11T20:31:37+06:30",  
        "vending_machine": choice,
        "items": user_choices,
        "total_amount": total_amount
          }
            user_transactions.append(transaction)
        elif choice == "3":
            display_items(vm3_data)
            user_choices = {}
            while True:
                item_code = int(input("Enter item code (0 to finish): "))
                if item_code == 0:
                    break
                quantity = int(input("Enter quantity: "))
                user_choices[item_code] = quantity
            total_amount = calculate_total(user_choices, vm3_data)
            print(f"Total amount: {total_amount}MMK")
            amount = payments - total_amount
            if payments >= total_amount:
                  print("Your Remaining Money is: ",amount)
            else:
                 print("Your Balance in insufficient....")  
            transaction = {
        "date": "2023-08-11T20:31:37+06:30",  
        "vending_machine": choice,
        "items": user_choices,
        "total_amount": total_amount
          }
            user_transactions.append(transaction)
        elif choice == "4":
            display_items(vm4_data)
            user_choices = {}
            while True:
                item_code = int(input("Enter item code (0 to finish): "))
                if item_code == 0:
                    break
                quantity = int(input("Enter quantity: "))
                user_choices[item_code] = quantity
            total_amount = calculate_total(user_choices, vm4_data)
            print(f"Total amount: {total_amount}MMK")
            amount = payments - total_amount
            if payments >= total_amount:
                  print("Your Remaining Money is: ",amount)
            else:
                 print("Your Balance in insufficient....")  
            transaction = {
        "date": "2023-08-11T20:31:37+06:30",  
        "vending_machine": choice,
        "items": user_choices,
        "total_amount": total_amount
          }
            user_transactions.append(transaction)
        elif choice == "5":
            display_items(vm5_data)
            user_choices = {}
            while True:
                item_code = int(input("Enter item code (0 to finish): "))
                if item_code == 0:
                    break
                quantity = int(input("Enter quantity: "))
                user_choices[item_code] = quantity
            total_amount = calculate_total(user_choices, vm5_data)
            print(f"Total amount: {total_amount}MMK")
            amount = payments - total_amount
            if payments >= total_amount:
                  print("Your Remaining Money is: ",amount)
            else:
                 print("Your Balance in insufficient....")  
            transaction = {
        "date": "2023-08-11T20:31:37+06:30", 
        "vending_machine": choice,
        "items": user_choices,
        "total_amount": total_amount
         }
            user_transactions.append(transaction)
        
        elif choice == "6":
            print("Goodbye!")
            with open("/Users/Acer/Desktop/python/.vscode/user_transactions.json", "w") as file:
               json.dump(user_transactions, file, indent=4)
            break
       
        else:
            print("Invalid choice. Please try again.")

     # Update JSON files with modified data
    with open("vm1.json", "w") as file:
        json.dump(vm1_data, file, indent=4)
    with open("vm2.json", "w") as file:
        json.dump(vm2_data, file, indent=4)
    with open("vm3.json", "w") as file:
        json.dump(vm3_data, file, indent=4)
    with open("vm4.json", "w") as file:
        json.dump(vm4_data, file, indent=4)
    with open("vm5.json", "w") as file:
        json.dump(vm5_data, file, indent=4)
   
if __name__ == "__main__":
    main()

   