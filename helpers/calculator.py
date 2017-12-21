# import pdb; pdb.set_trace()
import math

class ExpenseCalculator:

    def __init__(self, name, employer, annual_salary):
        self.name = name
        self.employer = employer
        self.annual_salary = annual_salary
        self.expenses = []

    def add_expense(self, exp_type, amount):
        self.expenses.append({exp_type: amount})
        # print "%s has been added to your expenses" % exp_type

    def print_expenses(self):
        for exp in self.expenses:
            key, value = exp.items()[0]
            print "expense type: %s. expense amount: $%i" % (key,value)

    def print_self(self):
        print "name: %s. employer: %s. annual salary: $%i" % (self.name, self.employer, self.annual_salary)

    def annual_calculation(self):
        temp_expenses = self.expenses
        total_expenses = 0
        # make all expenses annual
        for exp in self.expenses:
            key, value = exp.items()[0]
            total_expenses += exp[key] * 12

        print "Total Salary before expenses: $%i" % self.annual_salary
        print "Total annual expenses: $%i" % total_expenses
        print "total salary after expenses is: $%i" % (self.annual_salary - total_expenses)
        print ""

    def expenses_in_asc_order(self,expenses_arr):
        if len(expenses_arr) < 2:
            return expenses_arr

        lesser, greater = [], []

        p_exp = expenses_arr[0]
        expenses_arr.remove(p_exp)
        key,value = p_exp.items()[0]
        pivot = p_exp[key]

        for exp in expenses_arr:
            key,value = exp.items()[0]
            if exp[key] < pivot:
                lesser.append(exp)
            else:
                greater.append(exp)

        return self.expenses_in_asc_order(greater) + [p_exp] + self.expenses_in_asc_order(lesser)

    def print_expenses_in_asc_order(self):
        temp_exp = list(self.expenses)
        count = 1
        print "Here are your top expenses"
        for exp in self.expenses_in_asc_order(temp_exp):
            key,value = exp.items()[0]
            percent = math.ceil(float(value * 12) / float(self.annual_salary) * 100)
            print "%i. %s: $%i which is %i percent of your annual salary" % (count, key, value * 12, percent)
            count+=1


    def main_for_annual(self):
        self.annual_calculation()
        self.print_expenses_in_asc_order()
