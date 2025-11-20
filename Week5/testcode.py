import random

class UniqueIDManager:
    def __init__(self, start=100000, end=999999):
        self.available = set(range(start, end+1))   # pool of unused IDs
        self.assigned = {}  # dictionary: {id: name}
    
    def get_id(self, name):
        if not self.available:
            raise ValueError("No IDs left!")
        # pick a random ID directly from the set
        new_id = random.choice(list(self.available))  
        self.available.remove(new_id)
        self.assigned[new_id] = name
        return new_id
    
    def lookup(self, id_number):
        return self.assigned.get(id_number, None)
