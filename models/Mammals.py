from models.Animal import Animal

class Mammals(Animal):


    def __init__(self):
        '''Constructor for this class'''
        super(Mammals, self).__init__()
        self.members = ['Tiger', 'Elephant', 'Wild Cat']


    def printMembers(self):
        print('Printing all the members of mammals class')
        for member in self.members:
            print(member)

        print('Printing class attributes')
        print(self.get_species())
        self.set_species('Animals of Marsh')
        print(self.get_species())