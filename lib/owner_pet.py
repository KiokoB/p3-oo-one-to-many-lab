class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type= "bird", owner= None):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError("Invalid pet_type")
        self.name = name
        self.pet_type = pet_type
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of the Owner class.")
        self.owner = owner
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        #self.pets = []

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self,pet):
        if isinstance(pet,Pet):
            pet.owner = self
        else:
            raise TypeError("The pet must be an instance of Pet class")
        
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)