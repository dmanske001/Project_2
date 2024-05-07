from PyQt6.QtWidgets import *
from gui import *
from math import pi

class Logic(QMainWindow, Ui_MainWindow):
    """
    This class contains all the logic for the program
    """
    area_displayed = True


    def __init__(self) -> None:
        """
        Method hides area UI on program start. Also contains code triggers for all buttons being clicked.
        """
        super().__init__()
        self.setupUi(self)
        self.toggle_area_display()
        self.output_display.setText('0')


        self.button_0.clicked.connect(lambda: self.button_clicked('0'))
        self.button_1.clicked.connect(lambda: self.button_clicked('1'))
        self.button_2.clicked.connect(lambda: self.button_clicked('2'))
        self.button_3.clicked.connect(lambda: self.button_clicked('3'))
        self.button_4.clicked.connect(lambda: self.button_clicked('4'))
        self.button_5.clicked.connect(lambda: self.button_clicked('5'))
        self.button_6.clicked.connect(lambda: self.button_clicked('6'))
        self.button_7.clicked.connect(lambda: self.button_clicked('7'))
        self.button_8.clicked.connect(lambda: self.button_clicked('8'))
        self.button_9.clicked.connect(lambda: self.button_clicked('9'))
        self.button_divide.clicked.connect(lambda: self.button_clicked('/'))
        self.button_multiply.clicked.connect(lambda: self.button_clicked('*'))
        self.button_subtract.clicked.connect(lambda: self.button_clicked('-'))
        self.button_add.clicked.connect(lambda: self.button_clicked('+'))

        self.button_clear.clicked.connect(lambda: self.button_clicked('Clear'))

        self.button_mode.clicked.connect(lambda: self.toggle_area_display())

        self.button_dot.clicked.connect(lambda: self.dot_clicked())

        self.button_delete.clicked.connect(lambda: self.delete_clicked())

        self.button_toggle_negative.clicked.connect(lambda: self.toggle_negative())

        self.button_equals.clicked.connect(lambda: self.calculate())

        self.radiobutton_circle.clicked.connect(lambda: self.display_circle_area())
        self.radiobutton_triangle.clicked.connect(lambda: self.display_triangle_area())
        self.radiobutton_rectangle.clicked.connect(lambda: self.display_rectangle_area())
        self.radiobutton_square.clicked.connect(lambda: self.display_square_area())

        self.button_area_calculate.clicked.connect(lambda: self.calculate_area())


    def button_clicked(self, button_clicked) -> None:
        """
        This method handles buttons 0-9 and operators.
        It adds the clicked button to the output display.
        If the Clear button is clicked, it will clear the display.
        :param button_clicked: button the user has clicked
        """
        self.label_error.setText('')
        if button_clicked == 'Clear':
            self.output_display.setText("0")
        else:
            #gets rid of starting 0
            if self.output_display.text() == "0":
                self.output_display.setText("")

            self.output_display.setText(f'{self.output_display.text()}{button_clicked}')

    def dot_clicked(self) -> None:
        """
        This method will add a dot to the current number.
        It checks if the dot function is valid by checking
        if there has been a dot since the last operator.
        """
        current_display = self.output_display.text()
        operator_list = ['/', '*', '-', '+']

        valid_dot = True

        for character in current_display:
            if character in operator_list:
                valid_dot = True
            elif character == '.':
                valid_dot = False

        if valid_dot == True:
            self.output_display.setText(f'{self.output_display.text()}.')

    def delete_clicked(self) -> None:
        """
        This method deletes the last character in the output display when clicked.
        """
        current_display = self.output_display.text()
        current_display = current_display[:-1]

        self.output_display.setText(current_display)

    def toggle_negative(self) -> None:
        """"
        This method will toggle a number entered between positive and negative
        """
        current_display = self.output_display.text()

        if current_display[0] == '-':
            current_display = current_display[1:]
            self.output_display.setText(current_display)
        else:
            self.output_display.setText(f'-{current_display}')

    def calculate(self) -> None:
        """
        This method will calculate the expression in the output display
        """
        current_display = self.output_display.text()
        try:
            answer = eval(current_display)
            self.output_display.setText(str(answer))
        except:
            self.label_error.setText(f'Please check your expression\n'
                                     f'"{current_display}"\n'
                                     f' for errors, then press Clear.')
            self.label_error.setStyleSheet('color: red')
            self.output_display.setText('ERROR')


    def toggle_area_display(self) -> None:
        """
        This method toggles whether or not
        the area functionality is currently
        displayed. By default, it is hidden.
        """
        if self.area_displayed == True:
            self.label_area.hide()
            self.radiobutton_circle.hide()
            self.radiobutton_square.hide()
            self.radiobutton_triangle.hide()
            self.radiobutton_rectangle.hide()
            self.label_area_1.hide()
            self.label_area_2.hide()
            self.input_area_1.hide()
            self.input_area_1.clear()
            self.input_area_2.clear()
            self.input_area_2.hide()
            self.button_area_calculate.hide()
            self.label_error.clear()
            self.area_displayed = False
        else:
            self.label_area.show()
            self.radiobutton_circle.show()
            self.radiobutton_square.show()
            self.radiobutton_triangle.show()
            self.radiobutton_rectangle.show()
            self.radiobutton_circle.setChecked(True)
            self.label_area_1.show()
            self.display_circle_area()
            self.button_area_calculate.show()
            self.area_displayed = True

    def display_circle_area(self) -> None:
        """
        This method displays labels and input boxes for
        the calculate circle area functionality
        """
        self.label_area_1.setText('Radius')
        self.label_area_2.hide()
        self.input_area_2.hide()
        self.input_area_1.clear()
        self.input_area_2.clear()
        self.input_area_1.show()
    def display_triangle_area(self) -> None:
        """
        This method displays labels and input boxes for
        the calculate triangle area functionality
        """
        self.label_area_1.setText('Base')
        self.label_area_2.setText('Height')
        self.label_area_1.show()
        self.label_area_2.show()
        self.input_area_1.show()
        self.input_area_2.show()
        self.input_area_1.clear()
        self.input_area_2.clear()
    def display_square_area(self) -> None:
        """
        This method displays labels and input boxes for
        the calculate square area functionality
        """
        self.label_area_1.setText('Side')
        self.label_area_2.hide()
        self.input_area_1.clear()
        self.input_area_2.hide()
        self.input_area_1.show()
    def display_rectangle_area(self) -> None:
        """
        This method displays labels and input boxes for
        the calculate rectangle area functionality
        """
        self.label_area_1.setText('Length')
        self.label_area_2.setText('Width')
        self.label_area_1.show()
        self.label_area_2.show()
        self.input_area_1.show()
        self.input_area_2.show()
        self.input_area_1.clear()
        self.input_area_2.clear()


    def calculate_area(self) -> None:
        """
        This method calculates the area, based
        on which area functionality is currently
        selected
        """
        if self.radiobutton_circle.isChecked():
            try:
                radius = int(self.input_area_1.text())
                circle_area = pi * (radius ** 2)
                self.output_display.setText(f'Area = {circle_area}')
            except:
                self.label_error.setText(f'Please enter a number\n for radius.')
                self.label_error.setStyleSheet('color: red')
                self.output_display.setText('ERROR')

        if self.radiobutton_rectangle.isChecked():
            try:
                length = int(self.input_area_1.text())
                width = int(self.input_area_2.text())
                rectangle_area = length * width
                self.output_display.setText(f'Area = {rectangle_area}')
            except:
                self.label_error.setText(f'Please enter a number\n for both length and width.')
                self.label_error.setStyleSheet('color: red')
                self.output_display.setText('ERROR')

        if self.radiobutton_square.isChecked():
            try:
                side = int(self.input_area_1.text())
                square_area = side ** 2
                self.output_display.setText(f'Area = {square_area}')
            except:
                self.label_error.setText(f'Please enter a number\n for side.')
                self.label_error.setStyleSheet('color: red')
                self.output_display.setText('ERROR')

        if self.radiobutton_triangle.isChecked():
            try:
                base = int(self.input_area_1.text())
                height = int(self.input_area_2.text())
                triangle_area = (base*height) / 2
                self.output_display.setText(f'Area = {triangle_area}')
            except:
                self.label_error.setText(f'Please enter a number\n for both base and height.')
                self.label_error.setStyleSheet('color: red')
                self.output_display.setText('ERROR')



