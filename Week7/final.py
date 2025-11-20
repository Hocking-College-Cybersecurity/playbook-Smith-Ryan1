import random

def get_name():
    while True:
        name = input("Please enter your name:")
        if name.strip() and name.isalpha(): 
        # checks if the name has characters and only had alphabetical characters
            return name
        else:
            print("Error, invalid input, please enter your name:")


class UniqueNumberGenerator: 
    def __init__(self,start = 100000, end = 999999):
        self.available = set(range(start, end +1))
        self.assigned = {}
    
    def get_number(self, name):
        if not self.available:
            raise ValueError("THERE ARE NO NUMBERS LEFT")
        new_number = random.choice(list(self.available))
        self.available.remove(new_number)
        self.assigned[new_number] = name 
        return new_number

    def lookup(self,number):
        return self.assigned.get(number,None)
    
    def all_assigned(self):
        return self.assigned
    
    def random_name(self):
        if not self.assigned:
            return None
        return random.choice(list(self.assigned.values()))

if __name__ == "__main__":
    gen = UniqueNumberGenerator()

    while True:
        print("\n Menu:")
        print("1. Add a new user")
        print("2. View by number")
        print("3. View all assigned")
        print("4. Get a random Name")
        print("5. Exit")
    
        choice = int(input("Please choose an option:"))

        if choice == 1:
            name = get_name()
            unique_number = gen.get_number(name)
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
            result = gen.random_name
            if result:
                print(f"{name} has been selected.")
            else:
                print("No name has been assigned yet.")
        elif choice == 5:
            print("thank you")
            break
        else:
            print("Invalid choice please try again:")