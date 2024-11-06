import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


# Load the .ui file
class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Calculator.ui", self)

        # Display initialization
        self.display.setText("0")

        # Connect buttons to functions
        self.button0.clicked.connect(lambda: self.add_number("0"))
        self.button1.clicked.connect(lambda: self.add_number("1"))
        self.button2.clicked.connect(lambda: self.add_number("2"))
        self.button3.clicked.connect(lambda: self.add_number("3"))
        self.button4.clicked.connect(lambda: self.add_number("4"))
        self.button5.clicked.connect(lambda: self.add_number("5"))
        self.button6.clicked.connect(lambda: self.add_number("6"))
        self.button7.clicked.connect(lambda: self.add_number("7"))
        self.button8.clicked.connect(lambda: self.add_number("8"))
        self.button9.clicked.connect(lambda: self.add_number("9"))

        self.buttonPlus.clicked.connect(lambda: self.add_operation("+"))
        self.buttonMinus.clicked.connect(lambda: self.add_operation("-"))
        self.buttonMultiply.clicked.connect(lambda: self.add_operation("*"))
        self.buttonDivide.clicked.connect(lambda: self.add_operation("/"))

        self.buttonEqual.clicked.connect(self.calculate_result)
        self.buttonClear.clicked.connect(self.clear_display)

        # Variables for operation
        self.current_expression = ""

    def add_number(self, number):
        current_text = self.display.text()
        if current_text == "0":
            self.display.setText(number)
        else:
            self.display.setText(current_text + number)

    def add_operation(self, operation):
        self.current_expression += self.display.text() + operation
        self.display.setText("")

    def calculate_result(self):
        self.current_expression += self.display.text()
        try:
            result = eval(self.current_expression)
            self.display.setText(str(result))
            self.current_expression = ""
        except Exception:
            self.display.setText("Error")
            self.current_expression = ""

    def clear_display(self):
        self.display.setText("0")
        self.current_expression = ""


if __name__ == "__main__":
    app = QApplication([])
    window = Calculator()
    window.show()
    sys.exit(app.exec_())

