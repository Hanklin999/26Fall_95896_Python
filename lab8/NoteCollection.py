#%%
'''NoteCollection'''

class NoteCollection:
    def __init__(self):
        self.noteList = []
        
    def add(self, note):
        self.noteList.append(note)
        
    def getAllNotes(self):
        return self.noteList
    
    def getNoteByNumber(self, number):
        for note in self.noteList:
            if note.getNoteNumber() ==  number:
                return note
        return None
    
    
    def getNoteByName(self, name):
        names = []
        for note in self.noteList:
            if note.getName() == name:
                names.append(note)
        return names

