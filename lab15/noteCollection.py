from note import Note

class NoteCollection():
    def __init__(self):
        self.__noteList = list()
        self.__numberOfNotes = 0

    def add(self, note):
        self.__noteList.append(note)

    def getAllNotes(self):
        return self.__noteList

    def readNotes(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                name, body = line.strip().split(',')
                note = Note(name, body)
                self.add(note)

    def getNoteByNumber(self, number):
        for note in self.__noteList:
            if note.getNumber() == number:
                return note
        return None

    def getNoteByName(self, name):
        for note in self.__noteList:
            if note.getName() == name:
                return note
        return None

