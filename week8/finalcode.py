# A user friendly system for taking in names of employees, raffle players, etc. and assigning them
# six digit numbers at random, includes saving, loading, and delting data from a csv file.


import random
import csv
def get_name():
    while True:
        name = input("Please enter your first and last name:").strip()
        if any(char.isdigit() for char in name):
            print("Error, invalid input, please enter your name:")
        else:
            return name


class UniqueNumberGenerator: 
    def __init__(self,start = 100000, end = 999999):
        # Giving the range of numbers to use, in this case 100000 to 999999
        self.available = set(range(start, end +1))
        self.assigned = {}
    
    def get_number(self, name):
        if not self.available:
            raise ValueError("THERE ARE NO NUMBERS LEFT")
        # Important argument for making sure numbers are not regenerated and error handles for no more unique number
        new_number = random.choice(list(self.available))
        self.available.remove(new_number)
        self.assigned[new_number] = name 
        # adds the number to the dictionary
        return new_number

    def lookup(self,number):
        return self.assigned.get(number,None)
    
    def all_assigned(self):
        return self.assigned
    
    def random_name(self):
        # used for raffle winnings, chooses a random name from the list, prints their number too
        if not self.assigned:
            return None
        return random.choice(list(self.assigned.values()))
    def load(self, filename="final.csv"):
        self.assigned= {}
        try:
            with open(filename, newline="") as f:
                reader = csv.reader(f)
                for key, value in reader:
                    self.assigned[int(key)]= value
                #important to convert my csv data from a string back into a integer
        except (FileNotFoundError, ValueError):
            self.assigned= {}
    def save(self, filename="final.csv"):
        try:
            with open (filename, "w", newline = "") as f:
                writer = csv.writer(f)
                for key, value in self.assigned.items():
                    writer.writerow ([key,value])
        except (ValueError):
            self.assigned= {}
    def clear(self, filename="final.csv"):
            with open(filename ,"w", newline = "") as f:
                pass
    def delete_person(self, filename="final.csv"):
        if number in self.assigned:
            del self.assigned[number]
            return True
        return False

if __name__ == "__main__":
    gen = UniqueNumberGenerator()
    yes = 1
    no = 0
    while True:
        # standard menu options, including one to give you a random name for a raffle
        print("\n Menu:")
        print("1. Add a new user")
        print("2. View by number")
        print("3. View all assigned")
        print("4. Get a random Name")
        print("5. Load data")
        print("6. Save data")
        print("7. Delete data")
        print("8. Delete a specific person")
        print("9. Exit")
       
        try:
            choice = int(input("Please choose an option:"))
        except ValueError:
            print("please choose a number from the menu.")
            continue
        # makes sure people cannot put strings into the menu function
    
        if choice == 1:
            try:
                name = get_name()
            except ValueError:
                print("Name cannot include numbers. Please try again")
            unique_number = gen.get_number(name)
            # gives the name a number
        elif choice == 2:
            number = int(input("Please enter a number:"))
            name = gen.lookup(number)
            if name:
                print(f"Number {number} belongs to {name}.")
            else:
                print("No name associated with {number}.")
        elif choice == 3:
            print("All assigned IDs:")
            for num, name in gen.all_assigned().items():
                print(f"{num} -> {name},")
        elif choice == 4:
            result = gen.random_name()
            if result:
                print(f"{result} has been selected.")
            else:
                print("No name has been assigned yet.")
        elif choice == 5:
            gen.load("final.csv")
        elif choice == 6:
            gen.save("final.csv")
        elif choice == 7:
            gen.clear 
        # clears the csv file in case you with to delete the data   
        elif choice == 8:
            number = int(input("Please enter the number you wish to delete:"))
            if gen.delete_person(number):
                gen.save("final.csv")
            else:
                print("Number does not exist.")
        elif choice == 9:
            print("thank you")
            break
        else:
            print("Invalid choice please try again:")
