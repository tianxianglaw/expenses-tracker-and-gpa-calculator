from tkinter import *
from tkinter import messagebox, ttk
from datetime import datetime
import matplotlib.pyplot as plt

#expenses breakdown pie chart
def show_chart(category_totals): 
    labels = list(category_totals.keys()) #variable name
    sizes = list(category_totals.values()) #variable size
    
    #to avoid an error when there are no expenses 
    if sum(sizes) == 0: 
        messagebox.showinfo("Expense Tracker", "No expenses to display.") #no expenses message 
        return 
        
    fig, ax = plt.subplots() #create a figure and a set of subplots in matplotlib
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140) #draw the pie chart
    ax.axis('equal') #equal aspect ratio ensures that pie is drawn as a circle. 
    
    plt.title("Expense Breakdown") #set the title of the pie chart
    plt.show() #display the pie chart

class ExpenseTracker:
    def __init__(self, root):
        #initialize the window
        self.root = root #set the window
        root.geometry("800x770") #set the window size
        self.root.title("Expense Tracker") #window title 
        self.expenses = [] #initialize expenses list
        self.budget = 0 #initialize budget
        root.configure(bg='dark grey') #set the window background colour

        #create menu
        self.main_menu = Frame(self.root, bg='dark grey') #create main menu frame
        self.main_menu.pack() #pack the main menu

        self.create_menu() 

    def create_menu(self):
        #remove all widget from the window
        for widget in self.main_menu.winfo_children():
            widget.destroy()

        Label(self.main_menu, text="Welcome to Expenses Tracker",  font=("Times New Roman", 30, "bold"),fg='dark blue', bg='dark grey').pack() #welcome message
        #menu buttons
        #set monthly budget button
        set_button=Button(self.main_menu, text="Set Monthly Budget", command=self.set_budget, activebackground='green', width=20, height=2, font=("Arial", 15), bg='orange', fg='black')
        set_button.pack(pady=10) #padding set monthly budget button
        set_button.bind("<Enter>", self.on_enter) #change color when mouse enter
        set_button.bind("<Leave>", self.on_leave) #change color when mouse leave
        #sync bank button
        sync_button = Button(self.main_menu, text="Sync With Bank", command=self.sync_bank, activebackground='green', width=20, height=2, font=("Arial", 15), bg='orange', fg='black') 
        sync_button.pack(pady=10) #padding sync bank button
        sync_button.bind("<Enter>", self.on_enter) #change color when mouse enter
        sync_button.bind("<Leave>", self.on_leave) #change color when mouse leave
        #add expenses button
        add_button=Button(self.main_menu, text="Add Expenses", command=self.add_expense, activebackground='green', width=20, height=2, font=("Arial", 15), bg='orange', fg='black')
        add_button.pack(pady=10) #padding add expenses button
        add_button.bind("<Enter>", self.on_enter) #change color when mouse enter
        add_button.bind("<Leave>", self.on_leave) #change color when mouse leave
        #view expenses button
        view_button=Button(self.main_menu, text="View Expenses", command=self.view_expenses, activebackground='green', width=20, height=2, font=("Arial", 15), bg='orange', fg='black')
        view_button.pack(pady=10)  #padding view expenses button
        view_button.bind("<Enter>", self.on_enter) #change color when mouse enter
        view_button.bind("<Leave>", self.on_leave) #change color when mouse leave
        #report button
        report_button=Button(self.main_menu, text="Report", command=self.show_report, activebackground='green', width=20, height=2, font=("Arial", 15), bg='orange', fg='black')
        report_button.pack(pady=10) #padding report button
        report_button.bind("<Enter>", self.on_enter) #change color when mouse enter
        report_button.bind("<Leave>", self.on_leave) #change color when mouse leave
        #exit button
        exit_button=Button(self.main_menu, text="Exit", command=self.exit, activebackground='green', width=20, height=2, font=("Arial", 15), bg='orange', fg='black')
        exit_button.pack(pady=10) #padding exit button
        exit_button.bind("<Enter>", self.on_enter) #change color when mouse enter
        exit_button.bind("<Leave>", self.on_leave) #change color when mouse leave

    #default account number for validation 
    DEFAULT_ACCOUNT_NUMBER = "123456789012"

    def sync_bank(self): 
        self.clear_menu() 
        self.sync_bank_frame = Frame(self.root, bg='dark grey') 
        self.sync_bank_frame.pack() 
            
        #add title 
        Label(self.sync_bank_frame, text="Sync with Bank", font=("Times New Roman", 30, "bold"), fg='dark blue', bg='dark grey').pack() 
        
        #select bank 
        Label(self.sync_bank_frame, text="Select Bank", font=("Arial", 15), fg='dark blue', bg='dark grey').pack() 
        self.bank_var = StringVar(self.sync_bank_frame) #create a variable to store bank selection
        self.bank_var.set("Public Bank") #set Public Bank as default bank choice
        banks = ["Public Bank", "CIMB Bank", "Maybank", "RHB Bank"] #bank list
        self.bank_menu = OptionMenu(self.sync_bank_frame, self.bank_var, *banks) #create a dropdown menu for bank selection
        self.bank_menu.config(font=("Arial", 15), bg='orange', width=15) #set the bank list size
        self.bank_menu.pack() #padding bank list
        
        #set the bank list font size 
        menu = self.bank_menu.nametowidget(self.bank_menu.menuname) 
        menu.config(font=("Arial", 15), bg='orange') 
        
        #bank account number entry 
        Label(self.sync_bank_frame, text="Bank Account Number", font=("Arial", 15), fg='dark blue', bg='dark grey').pack() #title for bank account number entry
        self.bank_account_entry = Entry(self.sync_bank_frame, font=("Arial", 15)) #bank account number input entry
        self.bank_account_entry.pack() #padding bank account number entry
        
        #button to sync bank transaction history 
        fetch_button = Button(self.sync_bank_frame, text="Sync", command=self.fetch_transactions, activebackground='green', width=15, height=2, font=("Arial", 15), bg='orange', fg='black') 
        fetch_button.pack(pady=10) #padding sync button
        fetch_button.bind("<Enter>", self.on_enter) #change color when mouse enter
        fetch_button.bind("<Leave>", self.on_leave) #change color when mouse leave
        
        #back to menu button 
        back_button = Button(self.sync_bank_frame, text="Back to Menu", command=self.back_to_menu, activebackground='green', width=15, height=2, font=("Arial", 15), bg='orange', fg='black') 
        back_button.pack(pady=10) #padding back to menu button
        back_button.bind("<Enter>", self.on_enter) #change color when mouse enter
        back_button.bind("<Leave>", self.on_leave) #change color when mouse leave
        
    def fetch_transactions(self): 
        bank = self.bank_var.get() #get the selected bank
        account_number = self.bank_account_entry.get() #get the bank account number
        
        #validate account number with the default account number 
        if not account_number: 
            messagebox.showwarning("Warning", "Please enter the account number.") #warning message for empty account number
            return

        if account_number != self.DEFAULT_ACCOUNT_NUMBER: 
            messagebox.showerror("Invalid Account Number", "Please enter a valid account number.") #error message for invalid account number
            return 
            
        #display transaction history from a text file 
        try: 
            with open(f"{bank}.txt", "r") as file: 
                transactions = file.readlines() 
                
            #debug print statements 
            print(f"Bank: {bank}") 
            print(f"Account Number: {account_number}") 
            print(f"Transactions: {transactions}") 
            
            if not transactions: 
                messagebox.showinfo("No Transactions", "No transactions found in the file.") #no transactions message
                return 
                
            #clear any existing content in sync_bank_frame 
            for widget in self.sync_bank_frame.winfo_children(): 
                widget.destroy() 
                
            transaction_frame = Frame(self.sync_bank_frame, bg='dark grey')
            transaction_frame.pack() 
             
            #title for transaction history 
            Label(transaction_frame, text="Transaction History", font=("Times New Roman", 30, "bold"), fg='dark blue', bg='dark grey').pack() 
            
            self.synced_transactions = [] #initialize synced transactions 
            
            for transaction in transactions: 
                try: 
                    date, method, place, amount = transaction.strip().split(", ") 
                    
                    #remove "RM" prefix and convert to float 
                    amount = amount.replace("RM", "") 
                    amount = float(amount) 
                    
                    #categorize transactions based on method 
                    if method == "Credit Card": #pay by credit card
                        category = "Shopping" #show as shopping category
                    elif method == "Duit Now Transfer": #pay by duit now transfer
                        category = "Food & Drinks" #show as food & drinks category
                    elif method == "Debit Card": #pay by debit card
                        category = "Bills" #show as bills category
                    else: #pay by other methods
                        category = "Other" #show as other category
                    
                    self.synced_transactions.append({"amount": amount, "date": date, "description": place, "category": category}) #table title for transaction history
                    
                    color = 'red' #set the font colour for transaction history data
                    Label(transaction_frame, text=f"{date}, {method}, {place}, {amount:.2f}", font=("Arial", 12), fg=color, bg='dark grey').pack() #transaction history details
                except ValueError: #validation for error to sync transaction history data
                    print("Error sync transaction history:", transaction.strip()) #error message for unable to sync transaction history
                    
            #confirm sync button 
            confirm_button = Button(transaction_frame, text="Confirm Sync", command=self.confirm_sync, activebackground='green', width=15, height=2, font=("Arial", 15), bg='orange', fg='black') 
            confirm_button.pack(pady=10) #padding confirm sync button
            confirm_button.bind("<Enter>", self.on_enter) #change color when mouse enter
            confirm_button.bind("<Leave>", self.on_leave) #change color when mouse leave
            
            #back to menu button 
            back_button = Button(transaction_frame, text="Back to Menu", command=self.back_to_menu, activebackground='green', width=15, height=2, font=("Arial", 15), bg='orange', fg='black') 
            back_button.pack(pady=10) #padding back to menu button
            back_button.bind("<Enter>", self.on_enter) #change color when mouse enter
            back_button.bind("<Leave>", self.on_leave) #change color when mouse leave
        except FileNotFoundError: #validation for error to sync transaction history file
            messagebox.showerror("Error", f"No transaction history found for {bank}.") #error message for not found the transaction file 
        except Exception as e: #handle other exceptions
            messagebox.showerror("Error", str(e)) #show error message for other exceptions
            print("Error:", str(e)) #error message details for other exceptions

    def confirm_sync(self): 
        #save synced transactions to self.expenses 
        if hasattr(self, 'synced_transactions'): 
            self.expenses.extend(self.synced_transactions) 
            messagebox.showinfo("Sync Confirmed", "Transactions successfully synced with the bank.") 
            
        self.back_to_menu()

    def add_expense(self):
        #show the add expenses page
        self.clear_menu() #clear all widget from the window
        self.add_expense_frame = Frame(self.root, bg='dark grey') #create add expenses frame
        self.add_expense_frame.pack() #padding add expenses frame

        #add expenses title
        Label(self.add_expense_frame, text="Add Expenses", font=("Times New Roman", 30, "bold"), fg='dark blue', bg='dark grey').pack()

        #amount entry
        Label(self.add_expense_frame, text="Amount (RM)", font=("Arial", 15), fg='dark blue', bg='dark grey').pack() #amount entry title 
        self.amount_entry = Entry(self.add_expense_frame, font=("Arial", 15)) #amount entry input
        self.amount_entry.pack() #padding amount entry

        #date entry
        Label(self.add_expense_frame, text="Date (DD-MM-YYYY)", font=("Arial", 15), fg='dark blue', bg='dark grey').pack() #date entry title 
        self.date_entry = Entry(self.add_expense_frame, font=("Arial", 15)) #date entry input 
        self.date_entry.pack() #padding date entry

        #description entry
        Label(self.add_expense_frame, text="Description", font=("Arial", 15), fg='dark blue', bg='dark grey').pack() #description entry title 
        self.desc_entry = Entry(self.add_expense_frame, font=("Arial", 15)) #description entry input
        self.desc_entry.pack() #padding description entry

        #select category
        Label(self.add_expense_frame, text="Category", width=20, height=1, font=("Arial", 15), fg='dark blue', bg='dark grey').pack() #category selection title 
        self.category_var = StringVar(self.add_expense_frame) #create a variable to store category selection
        self.category_var.set("Shopping") #set shopping as default category

        #category drawer
        categories = ["Shopping", "Food & Drinks", "Bills", "Other"] #categories list
        self.option_menu = OptionMenu(self.add_expense_frame, self.category_var, *categories) #create a dropdown menu for category selection
        self.option_menu.config(font=("Arial", 15), bg='orange', width=15) #set the category drawer size
        self.option_menu.pack() #padding category drawer

        #set the category list font size
        menu = self.option_menu.nametowidget(self.option_menu.menuname) 
        menu.config(font=("Arial", 15), bg='orange')

        #add button
        add_exp = Button(self.add_expense_frame, text="Add", command=self.save_expense, activebackground='green', width=15, height=2, font=("Arial", 15), bg='orange', fg='black')
        add_exp.pack(pady=10) #padding add button
        add_exp.bind("<Enter>", self.on_enter) #change color when mouse enter
        add_exp.bind("<Leave>", self.on_leave) #change color when mouse leave

        #back to menu button
        back_button = Button(self.add_expense_frame, text="Back to Menu", command=self.back_to_menu, activebackground='green', width=15, height=2, font=("Arial", 15), bg='orange', fg='black')
        back_button.pack(pady=10) #padding back to menu button
        back_button.bind("<Enter>", self.on_enter) #change color when mouse enter
        back_button.bind("<Leave>", self.on_leave) #change color when mouse leave


    def save_expense(self):
        #check if any field is left blank
        if not self.amount_entry.get() or not self.date_entry.get() or not self.desc_entry.get():
            messagebox.showwarning("Warning", "Please fill in all fields.") #show warning message for blank fields
            return

        try:
            amount = float(self.amount_entry.get()) #get the amount(RM)
        except ValueError:
            messagebox.showerror("Invalid Amount", "Please enter a valid number for the amount.") #show error message for invalid amount
            return

        #get the data 
        date = self.date_entry.get() #get the date(DD-MM-YYYY)
        desc = self.desc_entry.get() #get the description
        category = self.category_var.get() #get the category

        #validate the date format
        try:
            datetime.strptime(date, "%d-%m-%Y") #validate the date format
        except ValueError: 
            messagebox.showerror("Invalid Date Format", "Please enter a valid date in DD-MM-YYYY format.") #show the date format error message
            return

        #save the expense to view expenses
        self.expenses.append({"amount": amount, "date": date, "description": desc, "category": category}) #table title for expenses
        messagebox.showinfo("Expense Added", f"Added: RM{amount:.2f}, {date}, {desc}, {category}") #show the expense added data

        #check new expenses if exceeded the budget
        if self.check_budget(amount): #check the sum of expenses
            messagebox.showwarning("Budget Alert", "You have exceeded your monthly budget!") #show warning message when expenses exceeded the budget

        #back to the menu
        self.back_to_menu() #return to the main menu



    def view_expenses(self): 
        #show the expenses history page 
        self.clear_menu() #clear all widget from the window
        self.view_expense_frame = Frame(self.root, bg='dark grey') #create view expenses frame
        self.view_expense_frame.pack() #padding view expenses frame
        
        #customize the table style 
        style = ttk.Style() 
        style.configure("Treeview", background="dark grey", foreground="dark blue", rowheight=25, fieldbackground="dark grey", font=("Helvetica", 15)) #customize table style
        style.configure("Treeview.Heading", background="orange", foreground="black", fieldbackground="orange", font=("Times New Roman", 15, "bold")) #customize table heading style
        style.map('Treeview', background=[('selected', 'dark orange')]) #customize table background color
        
        #ensure background color is applied to all widgets 
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})]) 
        
        #create a table widget 
        columns = ("Date", "Description", "Category", "Amount") #table column title 
        tree = ttk.Treeview(self.view_expense_frame, columns=columns, show='headings', style="Treeview") #create a table widget
        
        for col in columns: 
            tree.heading(col, text=col.capitalize()) #set the table column title first letter to uppercase
            tree.column(col, anchor=CENTER) #set the table column data to center alignment
            
        for expense in self.expenses: 
            tree.insert("", END, values=(expense['date'], expense['description'], expense['category'], expense['amount'])) #insert the expenses data to the table
            
        tree.pack() #padding the table
        
        #back to menu button 
        view_exp = Button(self.view_expense_frame, text="Back to Menu", command=self.back_to_menu, activebackground='green', width=15, height=2, font=("Arial", 15), bg='orange', fg='black') 
        view_exp.pack(pady=10) #padding back to menu button
        view_exp.bind("<Enter>", self.on_enter) #change color when mouse enter
        view_exp.bind("<Leave>", self.on_leave) #change color when mouse leave

    def set_budget(self):
        #show the set budget page 
        self.clear_menu() #clear all widget from the window
        self.set_budget_frame = Frame(self.root, bg='dark grey' ) #create set budget frame
        self.set_budget_frame.pack() #padding set budget frame

        #set budget
        Label(self.set_budget_frame, text="Set Monthly Budget(RM)", font=("Times New Roman", 30, "bold"),fg='dark blue', bg='dark grey').pack() #set monthly budget title
        self.budget_entry = Entry(self.set_budget_frame,  font=("Arial", 15)) #set monthly budget input entry
        self.budget_entry.pack() #padding set monthly budget entry

        #set budget button
        set_bud=Button(self.set_budget_frame, text="Set Budget", command=self.save_budget, activebackground='green', width=15, height=2, font=("Arial", 15), bg='orange', fg='black')
        set_bud.pack(pady=10) #padding set budget button
        set_bud.bind("<Enter>", self.on_enter) #change color when mouse enter
        set_bud.bind("<Leave>", self.on_leave) #change color when mouse leave
        #back to menu button
        back_button=Button(self.set_budget_frame, text="Back to Menu", command=self.back_to_menu, activebackground='green', width=15, height=2, font=("Arial", 15), bg='orange', fg='black')
        back_button.pack(pady=10) #padding back to menu button
        back_button.bind("<Enter>", self.on_enter) #change color when mouse enter
        back_button.bind("<Leave>", self.on_leave) #change color when mouse leave

    def save_budget(self):
        if not self.budget_entry.get():
            messagebox.showwarning("Warning", "Please enter the budget amount.") #show warning message for blank budget
            return
        #save the budget that just now entered
        try:
            self.budget = float(self.budget_entry.get()) #get the budget amount
            messagebox.showinfo("Budget Set", f"Monthly Budget set to: RM{self.budget:.2f}") #show the budget set data message
            self.back_to_menu() #return to the main menu
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for the budget.") #show error message for invalid input
            self.set_budget() #let user reenter the budget

    def check_budget(self, new_expense):
        #check if the total expense exceed the budget
        total_expense = sum(exp['amount'] for exp in self.expenses) #calculate the total expenses
        return total_expense + new_expense > self.budget #check if the total expenses exceed the budget

    def show_report(self):
        self.clear_menu() #clear all widget from the window
        self.report_frame = Frame(self.root, bg='dark grey') #create report frame
        self.report_frame.pack() #padding report frame

        #monthly report title
        Label(self.report_frame, text="Summary Report", font=("Times New Roman", 30, "bold"), fg='dark blue', bg='dark grey').pack()

        #calculate total expenses and budget status
        total_expense = sum(exp['amount'] for exp in self.expenses) #calculate the total expenses
        remaining_budget = self.budget - total_expense #calculate the remaining budget
        budget_status = "Under Budget" if remaining_budget >= 0 else "Over Budget" #budget status

        #create a summary report frame
        summary_frame = Frame(self.report_frame, bg='dark grey') #create summary report frame
        summary_frame.pack(pady=10) #padding summary report frame

        #summary report of the monthly expenses
        Label(summary_frame, text="Monthly Expenses", font=("Helvetica", 20, "bold"), fg='dark blue', bg='dark grey').pack() #monthly expenses title
        Label(summary_frame, text=f"Total Expenses: RM{total_expense:.2f}", font=("Helvetica", 15), fg='dark blue', bg='dark grey').pack() #show total expenses
        Label(summary_frame, text=f"Monthly Budget: RM{self.budget:.2f}", font=("Helvetica", 15), fg='dark blue', bg='dark grey').pack() #show monthly budget
        Label(summary_frame, text=f"Remaining Budget: RM{remaining_budget:.2f}", font=("Helvetica", 15), fg='dark blue', bg='dark grey').pack() #show remaining budget
        Label(summary_frame, text=f"Budget Status: {budget_status}", font=("Helvetica", 15, "bold"), 
        fg="red" if budget_status == "Over Budget" else "green", bg='dark grey').pack() #show budget status

        #expense breakdown
        category_totals = {
            "Shopping": sum(exp['amount'] for exp in self.expenses if exp['category'] == "Shopping"), #calculate the total expenses for shopping category
            "Food & Drinks": sum(exp['amount'] for exp in self.expenses if exp['category'] == "Food & Drinks"), #calculate the total expenses for food & drinks category
            "Bills": sum(exp['amount'] for exp in self.expenses if exp['category'] == "Bills"), #calculate the total expenses for bills category
            "Other": sum(exp['amount'] for exp in self.expenses if exp['category'] == "Other") #calculate the total expenses for other category
        }

        #debug print to check category totals
        print(f"Category Totals: {category_totals}")

        #create expense breakdown frame
        percentages_frame = Frame(self.report_frame, bg='dark grey')
        percentages_frame.pack(pady=10) #padding expense breakdown frame

        #expense breakdown title
        Label(percentages_frame, text="Expense Breakdown", font=("Times New Roman", 20, "bold"), fg='dark blue', bg='dark grey').pack() 

        #calculate the percentage of each category
        if total_expense > 0: 
            shopping_percent = (category_totals["Shopping"] / total_expense) * 100 #calculate the percentage of shopping category
            food_drinks_percent = (category_totals["Food & Drinks"] / total_expense) * 100 #calculate the percentage of food & drinks category
            bills_percent = (category_totals["Bills"] / total_expense) * 100 #calculate the percentage of bills category
            other_percent = (category_totals["Other"] / total_expense) * 100 #calculate the percentage of other category
        else:
            shopping_percent = food_drinks_percent = bills_percent = other_percent = 0 #set the percentage to 0 if total expense is 0

        #display the percentage of each category
        Label(percentages_frame, text=f"Shopping: {shopping_percent:.2f}%", font=("Helvetica", 15), fg='dark blue', bg='dark grey').pack() #show the percentage of shopping category
        Label(percentages_frame, text=f"Food & Drinks: {food_drinks_percent:.2f}%", font=("Helvetica", 15), fg='dark blue', bg='dark grey').pack() #show the percentage of food & drinks category
        Label(percentages_frame, text=f"Bills: {bills_percent:.2f}%", font=("Helvetica", 15), fg='dark blue', bg='dark grey').pack() #show the percentage of bills category
        Label(percentages_frame, text=f"Other: {other_percent:.2f}%", font=("Helvetica", 15), fg='dark blue', bg='dark grey').pack() #show the percentage of other category

        #show chart button
        chart_button = Button(self.report_frame, text="Show Chart", command=lambda: show_chart(category_totals), activebackground='green', width=15, height=2, font=('Arial', 15), bg='orange', fg='black')
        chart_button.pack(pady=10) #padding show chart button
        chart_button.bind("<Enter>", self.on_enter) #change color when mouse enter
        chart_button.bind("<Leave>", self.on_leave) #change color when mouse leave

        #back to menu button
        back_button = Button(self.report_frame, text="Back to Menu", command=self.back_to_menu, activebackground='green', width=15, height=2, font=('Arial', 15), bg='orange', fg='black')
        back_button.pack(pady=10) #padding back to menu button
        back_button.bind("<Enter>", self.on_enter) #change color when mouse enter
        back_button.bind("<Leave>", self.on_leave) #change color when mouse leave

    def exit(self):
        messagebox.showinfo("Goodbye", "Thanks for using Expenses Tracker!") #thanks for using message
        self.root.destroy() #close the window

    #function to change color while mouse enter 
    def on_enter(self, event): 
        event.widget['background'] = 'dark orange' 

    #function to change color while mouse leave   
    def on_leave(self, event): 
        event.widget['background'] = 'orange'

    def clear_menu(self):
        #clear all widget from the window
        for widget in self.root.winfo_children():
            widget.destroy()

    def back_to_menu(self):
        #return to main menu
        self.clear_menu()
        self.main_menu = Frame(self.root, bg='dark grey')
        self.main_menu.pack()
        self.create_menu()

def main(): 
    root = Tk() 
    app = ExpenseTracker(root) 
    root.mainloop() 
    
if __name__ == "__main__":
    main()
