# Student: Hank Lin
# Andrew ID: hanklin
# 95896 A, Lab16

import sys
from pathlib import Path

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QTextEdit,
    QGridLayout,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QFileDialog
)

from PyQt6.QtGui import QAction

from noteCollection import NoteCollection
from note import Note

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hank Lin's App")
        self.setFixedSize(QSize(500, 300))

        # Name
        self.nameLabel = QLabel("Name")
        self.nameTextField = QLineEdit()
        self.nameTextField.setFixedSize(220, 30)

        # Body
        self.bodyLabel = QLabel("Body")
        self.bodyTextField = QTextEdit()
        self.bodyTextField.setMinimumHeight(150)

        # Number
        self.numberLabel = QLabel("Number")
        self.numberTextField = QLineEdit()
        self.numberTextField.setFixedSize(100, 30)

        # Q5 / Q6: original horizontal and vertical layouts
        # nameLayout = QHBoxLayout()
        # nameLayout.addWidget(self.nameLabel)
        # nameLayout.addWidget(self.nameTextField)

        # bodyLayout = QHBoxLayout()
        # bodyLayout.addWidget(self.bodyLabel)
        # bodyLayout.addWidget(self.bodyTextField)

        # numberLayout = QHBoxLayout()
        # numberLayout.addWidget(self.numberLabel)
        # numberLayout.addWidget(self.numberTextField)

        # self.mainLayout = QVBoxLayout()
        # self.mainLayout.addLayout(nameLayout)
        # self.mainLayout.addLayout(bodyLayout)
        # self.mainLayout.addLayout(numberLayout)

        # Q7: grid layout
        self.mainLayout = QGridLayout()

        # Labels in row 0
        self.mainLayout.addWidget(self.nameLabel, 0, 1)
        self.mainLayout.addWidget(self.numberLabel, 0, 2)

        # Data in row 2
        self.mainLayout.addWidget(self.nameTextField, 2, 1)
        self.mainLayout.addWidget(self.numberTextField, 2, 2)

        # Body in row 3, spanning columns 1 and 2
        self.mainLayout.addWidget(self.bodyLabel, 3, 0)
        self.mainLayout.addWidget(self.bodyTextField, 3, 1, 1, 2)
        
        
        # 16 Q2 - add button
        self.nextNoteButton = QPushButton("Next Note")
        self.clearButton = QPushButton("Clear")
        self.newNoteButton = QPushButton("New Note")
        
        # 16 Q2 - add button to widget
        self.mainLayout.addWidget(self.nextNoteButton, 4, 0)
        self.mainLayout.addWidget(self.clearButton, 4, 1)
        self.mainLayout.addWidget(self.newNoteButton, 4, 2)
        

            
        

        self.widget = QWidget()
        self.widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.widget)

        # Read the CSV beside this Python file
        self.notes = NoteCollection()
        csv_path = Path(__file__).resolve().parent / "notesFile.csv"
        self.notes.readNotes(csv_path)

        # Display the first note
        # all_notes = self.notes.getAllNotes()

        #if all_notes:
        #    note = all_notes[0]
        #    self.nameTextField.setText(note.getName())
        #    self.bodyTextField.setPlainText(note.getBody())
        #    self.numberTextField.setText(str(note.getNumber()))
        
    
    # 16 Q3
        # setting details for nextNoteButton
        self.counter = 1  # next notes' code
        self.nextNoteButton.clicked.connect(self.showNextNote)
    
    # 16 Q4
        # setting details for clearButton
        self.clearButton.clicked.connect(self.clearNote)
        
        # setting details for newNoteButton
        self.newNoteButton.clicked.connect(self.createNote)
    
    # 16 Q5 file menu
        menuBar = self.menuBar()
        file_menu = menuBar.addMenu("&File")
        
        openAction = QAction("Open File", self)
        openAction.triggered.connect(self.openFile)
        file_menu.addAction(openAction)
        
        saveAction = QAction("Save File", self)
        saveAction.triggered.connect(self.saveFile)
        file_menu.addAction(saveAction)
        
    
    def showNextNote(self):
        if self.notes.size() == 0:
            return
        # go through and find the line showing this time
        # NoteCollection, getNoteByNumber
        note = self.notes.getNoteByNumber(self.counter)
        
        
        # put this line into the columns
        self.nameTextField.setText(note.getName())
        self.numberTextField.setText(str(note.getNumber()))
        self.bodyTextField.setPlainText(note.getBody())
        
        # counter + 1
        self.counter += 1
        
        
        # if the counter is more than there are notes (the method NoteCollection.size( ) will help here), re-set it back to one
        if self.counter > self.notes.size():
            self.counter = 1


    # 16 Q4
        # setting actions for clearButton            
    def clearNote(self):
        self.nameTextField.clear()
        self.numberTextField.clear()
        self.bodyTextField.clear()
        
    # 16 Q4
        # setting actions for newNoteButton
    def createNote(self):
        
        # get the inputs into Note
        name = self.nameTextField.text()
        body = self.bodyTextField.toPlainText()
        
        new_note = Note(name, body)
        
        # New note add into self.notes
        self.notes.add(new_note)
        
        # get new number for the note
        number = new_note.getNumber()
        
        # add to counter
        self.counter = number
        
        # show on screen
        self.numberTextField.setText(str(number))
        
        
# 16 Q5 - open file

def openFile(self):
    self.filename, x = QFileDialog.getOpenFileName(
        self, "Open File", "", "All Files (*)"
        )
    if not self.filename:
        return
    
    
    # Replace the old collection
    self.notes = NoteCollection()
    self.notes.readNotes(self.filename)
    self.counter = 1
    
    # Clear the previous display
    self.clearNote()
    
    # Get the list of notes from the new collection
    all_notes = self.notes.getAllNotes()
    
    # Display the first note if the list is not empty.
    if len(all_notes) != 0:
        note = all_notes[0]
        self.nameTextField.setText(note.getName())
        self.numberTextField.setText(str(note.getNumber()))
        self.bodyTextField.setPlainText(note.getBody())
                

# 16 Q5 - Save File
def saveFile(self):
    # Let the user choose the save location and filename.
    self.filename, _ = QFileDialog.getSaveFileName(
        self, "Save As", "", "All Files (*)"
    )

    # Do nothing if the user cancels.
    if not self.filename:
        return

    # Write all notes in the collection to the selected file.
    self.notes.writeNotes(self.filename)
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()