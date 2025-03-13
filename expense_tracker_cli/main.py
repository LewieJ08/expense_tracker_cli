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
    
    
def update():
    pass

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

        if splitInput[0] == COMMANDS[0]:
            break

        command, argument, amount = splitInput 
      
        if command == COMMANDS[1]:
            try:
                amount = int(amount)
                add(argument, amount)
            except ValueError:
                print("Amount must be an integer ")

#entry point
if __name__ == "__main__":
    main()