from note import Note

class NoteCollection():
    def __init__(self):
        self.__noteList = list()
        self.__numberOfNotes = 0

    def add(self, note):
        self.__noteList.append(note)
        self.__numberOfNotes = self.__numberOfNotes + 1

    def getAllNotes(self):
        return self.__noteList

    def readNotes(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                name, body = line.strip().split(',')
                if self.__numberOfNotes == 0:
                    note = Note(name, body, True)
                else:
                    note = Note(name, body)
                self.add(note)

    def writeNotes(self, filename):
        with open(filename, 'w') as f:
            for note in self.__noteList:
                f.write(note.getName() + ',' + note.getBody() + '\n')

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

    def size(self):
        return len(self.__noteList)
