import os
import json
import datetime

JSONFILE = "data.json"
COMMANDS = ["exit","add","update","delete","list","summary"]

def current_date():
    return str(datetime.datetime.now().strftime("%d/%m/%Y"))

def add(description,amount):
    with open(JSONFILE) as file:
        data = json.load(file)
    iD = 1
    current_ids = []

    for item in data:
        current_ids.append(item["id"])

    while iD in current_ids:
        iD += 1

    data.append({
        "id": iD,
        "date": current_date(),
        "description": description,
        "amount": amount
    })

    with open(JSONFILE,"w") as file:
        json.dump(data,file,indent=4)
    
    
def update(iD):
    with open(JSONFILE) as file:
        data = json.load(file)

    for item in data:
        if item["id"] == iD:
            description = input("New description> ")
            amount = int(input("New amount> "))

            item["description"] = description
            item["amount"] = amount

            with open(JSONFILE,"w") as file:
                json.dump(data,file,indent=4)  

            print("Expense updated successfully")
            return
        
    print(f"Expence with ID '{iD}' not found")

def delete(iD):
    with open(JSONFILE) as file:
        data = json.load(file)

    updatedData = []

    for item in data:
        if item["id"] != iD:
            updatedData.append(item)

    if len(updatedData) == len(data):
        print("Expense not found.")
        return 
    
    with open(JSONFILE,"w") as file:
        json.dump(updatedData,file,indent=4)

def summary(month):
    with open(JSONFILE) as file:
        data = json.load(file)

    total = 0

    if month == False:
        for item in data:
            total += item["amount"]

        print(f"Total expenses: £{total}")


def list():
    pass

#main function
def main():
    if not os.path.exists(JSONFILE):
        with open(JSONFILE,"w") as file:
            json.dump([], file)

    while True:
        uinput = input("Expense-Tracker> ").lower().strip()
        splitInput = uinput.split(" ",2)

        if len(splitInput) == 3:
            command, argument, amount = splitInput 
      
            if command == COMMANDS[1]:
                try:
                    amount = int(amount)
                    add(argument, amount)
                    continue
                except ValueError:
                    print("Amount must be an integer")
                    continue

        elif len(splitInput) == 2:
            command, iD = splitInput

            if command == COMMANDS[2]:
                try:
                    iD= int(iD)
                    update(iD)
                    continue
                except ValueError:
                    print("ID must be an integer")
                    continue
            
            elif command == COMMANDS[3]:
                try:
                    iD= int(iD)
                    delete(iD)
                    continue
                except ValueError:
                    print("ID must be an integer")
                    continue

            command, month = splitInput

            if command == COMMANDS[5]:
                try:
                    month = int(month)
                    summary(month)
                    continue
                except ValueError: 
                    print("Month must be an integer")
                    continue

        elif splitInput[0] == COMMANDS[0]:
            break

        elif splitInput[0] == COMMANDS[5]:
            summary(False)
            continue

        print("Invalid command.")

#entry point
if __name__ == "__main__":
    main()