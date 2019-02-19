class Penguin:
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def fly(self):
        print('Penguin can not fly')

    def swim(self):
        print('Penguin can swim')

