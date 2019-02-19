class Parrot:
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def fly(self):
        print('Parrot can fly')

    def swim(self):
        print('Parrot can not swim')