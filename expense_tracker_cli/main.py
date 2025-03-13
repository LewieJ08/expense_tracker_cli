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
            print(item)
            description = input("New description> ")
            amount = int(input("New amount> "))

            item["description"] = description
            item["amount"] = amount

            with open(JSONFILE,"w") as file:
                json.dump(data,file,indent=4)  

            print("Expense updated successfully")
            return
        
    print(f"Expence with ID '{iD}' not found")

def delete():
    pass

def summary():
    pass

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
                except ValueError:
                    print("Amount must be an integer")

        elif len(splitInput) == 2:
            command, iD = splitInput

            if command == COMMANDS[2]:
                try:
                    iD= int(iD)
                    update(iD)
                except ValueError:
                    print("Amount must be an integer")
        

        if splitInput[0] == COMMANDS[0]:
            break


#entry point
if __name__ == "__main__":
    main()