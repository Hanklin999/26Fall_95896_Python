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
)

from noteCollection import NoteCollection


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

        self.widget = QWidget()
        self.widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.widget)

        # Read the CSV beside this Python file
        self.notes = NoteCollection()
        csv_path = Path(__file__).resolve().parent / "notesFile.csv"
        self.notes.readNotes(csv_path)

        # Display the first note
        all_notes = self.notes.getAllNotes()

        if all_notes:
            note = all_notes[0]
            self.nameTextField.setText(note.getName())
            self.bodyTextField.setPlainText(note.getBody())
            self.numberTextField.setText(str(note.getNumber()))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()