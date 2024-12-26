from tkinter import *
from tkinter import messagebox
import os

class GPA:
    # Set the initial interface of the main window
    def __init__(self, root):
        self.root = root
        # Set the size of the window
        self.root.geometry("1200x750")
        # Set the title of the window
        self.root.title("GPA Calculator")
        # Set the background color of the window
        self.root.configure(bg='#C8CFC4')
        self.main_window()

    # Saving student information to a file named student_info.txt
    def save_student_info(self, student_info):
        with open("student_info.txt", "a") as file:
            for key, value in student_info.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")

    # Saving grades to a file named grades.txt
    def save_grades(self, grades):
        with open("grades.txt", "a") as file:
            for grade in grades:
                file.write(f"Subject: {grade[0]}, Grade: {grade[1]}, Credit Hour: {grade[2]}\n")
            file.write("\n")

    # Load student information to a file named student_info.txt
    def load_student_info(self):
        if os.path.exists("student_info.txt"):
            with open("student_info.txt", "r") as file:
                data = file.readlines()
                student_info = {}
                for line in data:
                    key, value = line.strip().split(": ")
                    student_info[key] = value
                return student_info
        return None

    # Load grades to a file named grades.txt
    def load_grades(self):
        if os.path.exists("grades.txt"):
            with open("grades.txt", "r") as file:
                grades = []
                for line in file:
                    parts = line.strip().split(", ")
                    subject = parts[0].split(": ")[1]
                    grade = parts[1].split(": ")[1]
                    credit_hour = parts[2].split(": ")[1]
                    grades.append((subject, grade, credit_hour))
                return grades
        return []

    # Function for main window
    def main_window(self):
        # Welcome message for users
        Label(self.root, text='Welcome to GPA Calculator!', font=('Arial', 25, 'bold', 'italic'), fg='#5F8151', bg='#C8CFC4').place(x=430, y=30)
        # Instruction for users
        Label(self.root, text="Enter your student information below.", font=('Times New Roman', 15), fg='#5F8151', bg='#C8CFC4').place(x=480, y=100)

        # Get input from users for their student information
        self.name_entry = self.create_entry("Enter your full name:", 150)
        self.id_entry = self.create_entry("Enter your student ID:", 200)
        self.programme_entry = self.create_entry("Enter your programme:", 250)
        self.group_entry = self.create_entry("Enter your tutorial group:", 300)
        self.year_entry = self.create_entry("Enter your year of study:", 350)

        # Button for users to click to enter their grades
        Button(self.root, text="Click to enter your grades", font=('Times New Roman', 15), command=self.validate_data, activebackground='blue', width=20, height=2, bg='#5F8151').place(x=500, y=650)

    # Create multiple entry fields for user input
    def create_entry(self, label_text, y):
        Label(self.root, text=label_text, font=('Times New Roman', 15), fg='#5F8151', bg='#C8CFC4').place(x=400, y=y)
        entry = Entry(self.root, font=('Times New Roman', 15))
        entry.place(x=610, y=y)
        return entry

    # Validate the input based on the type of entry and prompt error msg
    def validate_entry(self, entry, entry_type):
        value = entry.get()
        if entry_type == "name" and not value.replace(" ", "").isalpha():
            messagebox.showerror("Invalid Input", "Name should contain only letters and spaces.")
            return False
        elif entry_type == "id" and not value.isalnum():
            messagebox.showerror("Invalid Input", "Student ID should contain only numbers and letters.")
            return False
        elif entry_type == "programme" and not value.isalpha():
            messagebox.showerror("Invalid Input", "Programme should contain only letters.")
            return False
        elif entry_type == "group" and not value.isdigit():
            messagebox.showerror("Invalid Input", "Tutorial group should contain only numbers.")
            return False
        elif entry_type == "year" and not value.isdigit():
            messagebox.showerror("Invalid Input", "Year of study should contain only numbers.")
            return False
        return True

    # Saves the student information if the input is valid
    def validate_data(self):
        if not self.validate_entry(self.name_entry, "name"):
            return
        if not self.validate_entry(self.id_entry, "id"):
            return
        if not self.validate_entry(self.year_entry, "year"):
            return
        if not self.validate_entry(self.programme_entry, "programme"):
            return
        if not self.validate_entry(self.group_entry, "group"):
            return
        student_info = {
            "Name": self.name_entry.get(),
            "Student ID": self.id_entry.get(),
            "Programme": self.programme_entry.get(),
            "Group": self.group_entry.get(),
            "Year": self.year_entry.get()
        }
        self.save_student_info(student_info)
        self.second_window()

    # Function for the second window
    def second_window(self):
        # Destroy the main window and create a new window (2nd window)
        self.root.destroy()
        second_window = Tk()
        # Set the size of the 2nd window
        second_window.geometry('1200x750')
        # Set the title of the 2nd window
        second_window.title('GPA Calculator')
        # Set the background colour of the 2nd window
        second_window.configure(bg='#C8CFC4')
        # GPA Calculator as the header
        Label(second_window, text='GPA Calculator', font=('CourierNew', 25, 'bold', 'italic', 'underline'), fg='#5F8151', bg='#C8CFC4').place(x=500, y=30)
        # Instruction for users
        Label(second_window, text='Enter your grade information below.', font=('Times New Roman', 15), fg='#5F8151', bg='#C8CFC4').place(x=500, y=80)
        self.grade_info(second_window)

    # Function for the grade information entry
    def grade_info(self, second_window):
        self.subject_entries = []
        self.grade_entries = []
        self.hour_entries = []
        self.subject_labels = []
        self.grade_labels = []
        self.hour_labels = []

        # Function to enter grade information
        def enter_grade(): 
            i = len(self.subject_entries)
            subject_label = Label(second_window, text=f"Subject {i+1}:", font=('Times New Roman', 15), fg='#5F8151', bg='#C8CFC4')
            subject_label.place(x=100, y=150 + i*50)
            subject_entry = Entry(second_window, font=('Times New Roman', 15))
            subject_entry.place(x=190, y=150 + i*50)
            self.subject_entries.append(subject_entry)
            self.subject_labels.append(subject_label)

            grade_label = Label(second_window, text=f"Grade {i+1}:", font=('Times New Roman', 15), fg='#5F8151', bg='#C8CFC4')
            grade_label.place(x=450, y=150 + i*50)
            grade_entry = Entry(second_window, font=('Times New Roman', 15))                
            grade_entry.place(x=540, y=150 + i*50)
            self.grade_entries.append(grade_entry)
            self.grade_labels.append(grade_label)

            hour_label = Label(second_window, text=f"Credit Hour {i+1}:", font=('Times New Roman', 15), fg='#5F8151', bg='#C8CFC4')
            hour_label.place(x=800, y=150 + i*50)
            hour_entry = Entry(second_window, font=('Times New Roman', 15))
            hour_entry.place(x=930, y=150 + i*50)
            self.hour_entries.append(hour_entry)
            self.hour_labels.append(hour_label)

        # Function to validate data entry and prompt error msg
        def validate_entry(entry, entry_type):
            value = entry.get()
            if entry_type == "subject" and not value.replace(" ", "").isalpha():
                messagebox.showerror("Invalid Input", "Subject should contain only letters.")
                return False
            elif entry_type == "grade" and value not in ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "F"]:
                messagebox.showerror("Invalid Input", "Grade should be one of the following: A+, A, A-, B+, B, B-, C+, C, F.")
                return False
            elif entry_type == "credit hour" and not value.isdigit():
                messagebox.showerror("Invalid Input", "Credit Hour should contain only digits.")
                return False
            return True

        # Function to save data entry
        def validate_data():
            for i in range(len(self.subject_entries)):
                if not validate_entry(self.subject_entries[i], "subject"):
                    return
                if not validate_entry(self.grade_entries[i], "grade"):
                    return
                if not validate_entry(self.hour_entries[i], "credit hour"):
                    return
            grades = [(self.subject_entries[i].get(), self.grade_entries[i].get(), self.hour_entries[i].get()) for i in range(len(self.subject_entries))]
            self.save_grades(grades)
            self.third_window(second_window, grades)

        # Function to delete data entry
        def delete_data():
            if len(self.subject_entries) > 0:
                self.subject_labels[-1].destroy()
                self.grade_labels[-1].destroy()
                self.hour_labels[-1].destroy()
                self.subject_entries[-1].destroy()
                self.grade_entries[-1].destroy()
                self.hour_entries[-1].destroy()

                self.subject_labels.pop()
                self.grade_labels.pop()
                self.hour_labels.pop()
                self.subject_entries.pop()
                self.grade_entries.pop()
                self.hour_entries.pop()

        # Button to delete data entry
        Button(second_window, text="Delete Data", font=('Times New Roman', 15), command=delete_data, activebackground='blue', width=20, height=2, bg='#5F8151').pack(side=BOTTOM, pady=10)
        # Button to add data entry
        Button(second_window, text="Add Subject", font=('Times New Roman', 15), command=enter_grade, activebackground='blue', width=20, height=2, bg='#5F8151').pack(side=BOTTOM, pady=10)
        # Button to calculate GPA
        Button(second_window, text="Calculate GPA", font=('Times New Roman', 15), command=validate_data, activebackground='blue', width=20, height=2, bg='#5F8151').pack(side=BOTTOM, pady=20)

        # Loop for 3 times for data entry
        for _ in range(3):
            enter_grade()

    # Function for 3rd window
    def third_window(self, second_window, grades):
        # Destroy 2nd window and create a new window (3rd window)
        second_window.destroy()
        third_window = Tk()
        # Set the size of the 3rd window
        third_window.geometry('1200x750')
        # Set the title of the 3rd window
        third_window.title('GPA Calculator')
        # Set the background colour of the 3rd window 
        third_window.configure(bg='#C8CFC4')

        # Display the student information
        for i, grade in enumerate(grades):
            Label(third_window, text=f"Subject {i+1}: ", font=('Times New Roman', 20), fg='#5F8151', bg='#C8CFC4').place(x=180, y=250 + i*50)
            Label(third_window, text=grade[0], font=('Times New Roman', 20, 'bold'), fg='#5F8151', bg='#C8CFC4').place(x=300, y=250 + i*50)
            Label(third_window, text=f"Grade {i+1}: ", font=('Times New Roman', 20), fg='#5F8151', bg='#C8CFC4').place(x=530, y=250 + i*50)
            Label(third_window, text=grade[1], font=('Times New Roman', 20, 'bold'), fg='#5F8151', bg='#C8CFC4').place(x=650, y=250 + i*50)
            Label(third_window, text=f"Credit Hour {i+1}: ", font=('Times New Roman', 20), fg='#5F8151', bg='#C8CFC4').place(x=880, y=250 + i*50)
            Label(third_window, text=grade[2], font=('Times New Roman', 20, 'bold'), fg='#5F8151', bg='#C8CFC4').place(x=1050, y=250 + i*50)

        # Function to calculate GPA
        def calculate_gpa():
            total_grade_points = 0
            total_credit_hours = 0
            for grade in grades:
                grade_point = 0
                if grade[1] == "A+" or grade[1] == "A":
                    grade_point = 4.0
                elif grade[1] == "A-":
                    grade_point = 3.7
                elif grade[1] == "B+":
                    grade_point = 3.3
                elif grade[1] == "B":
                    grade_point = 3.0
                elif grade[1] == "B-":
                    grade_point = 2.7
                elif grade[1] == "C+":
                    grade_point = 2.3
                elif grade[1] == "C":
                    grade_point = 2.0
                elif grade[1] == "C-":
                    grade_point = 1.7
                elif grade[1] == "D+":
                    grade_point = 1.3
                elif grade[1] == "D":
                    grade_point = 1.0
                elif grade[1] == "F":
                    grade_point = 0.0

                credit_hour = int(grade[2])
                total_grade_points += grade_point * credit_hour
                total_credit_hours += credit_hour

            gpa = total_grade_points / total_credit_hours

            # Display GPA result
            Label(third_window, text="Your GPA: " + str(round(gpa, 4)), font=('Arial', 30, 'bold', 'underline'), fg='#5F8151', bg='#C8CFC4').pack(side=TOP, pady=50)
            # Display total credit hours earned
            Label(third_window, text="Total Credit Hours Earned: " + str(total_credit_hours), font=('Arial', 20, 'bold', 'italic'), fg='#5F8151', bg='#C8CFC4').pack(side=TOP, pady=20)

            # Button to return to the main window (student info page)
            Button(third_window, text="Return to Main Window", font=('Times New Roman', 15), command=lambda: [third_window.destroy(), self.restart()], activebackground='blue', width=20, height=2, bg='#5F8151').pack(side=BOTTOM, pady=20)

            # Function to terminate the program
            def exit_program():
                messagebox.showinfo("Thank you", "Thank you for using our GPA Calculator!")
                third_window.destroy()

            # Button to terminate the program
            Button(third_window, text="Exit Programme", font=('Times New Roman', 15), command=exit_program, activebackground='blue', width=20, height=2, bg='#5F8151').pack(side=BOTTOM, pady=20)

        calculate_gpa()

        # Function to return to the main window
    def restart(self):
        self.root = Tk()
        # Set the size of the window
        self.root.geometry("1200x750")
        # Set the title of the window
        self.root.title("GPA Calculator")
        # Set the background color of the window
        self.root.configure(bg='#C8CFC4')
        self.main_window()
        self.root.mainloop()

# Main execution
def main(): 
    root = Tk()
    app = GPA(root)
    root.mainloop()

if __name__ == "__main__":
    main()