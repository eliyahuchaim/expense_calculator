import os
from calculator import ExpenseCalculator

class Main:
    user = ""
    quit = False

    @classmethod
    def create_calculator(cls):
        name = str(raw_input("what is your name? ")).strip()
        employer = str(raw_input("what is the employers name? ")).strip()
        salary = int(raw_input("what is the annual salary? "))

        print "Name is: %s. Employer is: %s. Salary is: $%i" % (name, employer, salary)

        move_on = str(raw_input("Press Y to confirm, N to start Over: ")).lower()

        if move_on == 'n':
            os.system('cls||clear')
            return cls.create_calculator()
        else:
            cls.user = ExpenseCalculator(name, employer, salary)

    @classmethod
    def add_user_expenses(cls):
        expense_type = str(raw_input("Enter Expense Type: ")).strip()
        expense_amount = int(raw_input("Enter the monthly expense amount: $"))

        cls.user.add_expense(expense_type, expense_amount)

        move_on = str(raw_input("add another? Y for yes, N for No ")).lower()

        if move_on == 'y':
            os.system('cls||clear')
            return cls.add_user_expenses()


    @classmethod
    def main(cls):
        cls.create_calculator()
        os.system('cls||clear')
        cls.user.print_self()
        cls.add_user_expenses()
        os.system('cls||clear')
        options = "A - add more expenses. Q - quit. P - print out expenses. D - print out final results"
        show_options = True

        while cls.quit == False:
            if show_options == True:
                show_options = False
                print options

            user_input = str(raw_input("Please enter your option - Enter O to see options ")).lower()

            if user_input == 'q':
                print "Goodbye"
                cls.quit = True
            elif user_input == 'a':
                os.system('cls||clear')
                cls.add_user_expenses()
            elif user_input == 'p':
                os.system('cls||clear')
                cls.user.print_expenses()
            elif user_input == 'd':
                os.system('cls||clear')
                cls.user.main_for_annual()
            elif user_input == 'o':
                os.system('cls||clear')
                show_options = True


Main.main()
