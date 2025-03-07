class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise Exception("Pet name must be a string")
        self.name = name

        if not isinstance(pet_type, str):
            raise Exception("Pet type must be a string")
        
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        self.pet_type = pet_type


        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner")
        self.owner = owner

        Pet.all.append(self)
        pass
    pass

class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Owner name must be a string")
        self.name = name

    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("add_pet expects a Pet instance")
        pet.owner = self

    
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
        pass
    pass