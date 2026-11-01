from noteCollection import NoteCollection
from note import Note

def main():
    noteCollection = NoteCollection()
    noteCollection.readNotes('notesFile.csv')
    allNotes = noteCollection.getAllNotes()
    for note in allNotes:
        print(note)

if __name__ == '__main__':
    main()

