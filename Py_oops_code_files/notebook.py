# Exercise 10: Notebook Class with Add & Display Notes
class Notebook():

    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def show_notes(self):
        for i, note in enumerate(self.notes):
            print(i+1,note)

nb1 = Notebook()
nb1.add_note('Buy Groceries')
nb1.add_note('Read a book')
nb1.add_note('Wash Clothes')
nb1.add_note('Meditate')
nb1.show_notes()