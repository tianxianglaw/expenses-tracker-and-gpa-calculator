from tkinter import *
from tkinter import messagebox

#import expenses tracker and gpa calculator
import expenses_tracker
import gpa_calculator

#run the expenses tracker application
def run_expense_tracker(root):
    try:
        root.destroy()  # close the menu window
        expenses_tracker.main()
        #reopen the main menu after the expenses tracker is closed
        menu()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run Expense Tracker: {str(e)}")


#run the gpa calculator application
def run_gpa_calculator(root):
    try:
        root.destroy()  #close the menu window
        gpa_calculator.main()
        #reopen the main menu after the gpa calculator is closed
        menu() 
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run GPA Calculator: {str(e)}")

def menu():
    #create the main menu window
    root = Tk()
    root.geometry("700x300")
    root.title("Main Application")
    root.configure(bg='gold')

    #title of the main menu window
    label = Label(root, text="Choose an Application", font=('Times New Roman', 30, 'bold'),bg='gold',fg='dark blue')
    label.pack(pady=20)

    #expenses tracker application button 
    button_expense_tracker = Button(root, text="Expense Tracker", font=('Helvetica', 14), command=lambda: run_expense_tracker(root), activebackground='green', bg='dark blue', fg='white',width=20, height=2)
    button_expense_tracker.pack(pady=10)

    #gpa calculator application button
    button_gpa_calculator = Button(root, text="GPA Calculator", font=('Helvetica', 14), command=lambda: run_gpa_calculator(root), activebackground='green', bg='dark blue', fg='white',width=20, height=2)
    button_gpa_calculator.pack(pady=10)

    #run the main menu window
    root.mainloop()

menu() #run the main menu window
