<h1 align="center">Expenses Tracker and GPA Calculator Application</h1>

## Table of Contents 
- [Install the required dependencies](#install-the-required-dependencies)
- [How to run the application](#how-to-run-the-application)
- [Application menu](#application-menu)
- [Expenses tracker application](#expenses-tracker-application)
- [GPA Calculator application](#gpa-calculator-application)

## Install the required dependencies
- type the command below in command prompt:
    ```
    pip install matplotlib
    ```
    
## Run the application

A. Visual Studio Code:
   ```
    - open visual studio code make sure have install python extension then only debug the python file.
   ```

B. Command Prompt:
   ```
    - open the assignment.py file folder
    - right click the folder, choose command prompt
    - enter command "python main.py"
   ```

C. Anaconda Prompt:
```
     - please make sure downloaded Anaconda Distribution from https://docs.anaconda.com/anaconda/getting-started
     - open anaconda prompt 
     - enter the right path (foward): cd "folder name"
     - enter the right path (backward): cd..
     - enter command "python main.py" to execute the python file
```

## Application menu

- This application menu has 2 application to choose which application need to use 
```
   - Expenses Tracker 
   - GPA Calculator 
```

## Expenses tracker application

- First of all, need to make sure 4 bank transaction text file has been downloaded, which is RHB Bank, CIMB Bank, Public Bank and MayBank.

1. Set Monthly Budget:
   ```
    - click the set monthly budget, it will show the set budget page 
    - then, enter the budget you want to save this month 
    - after press set budget it will show the budget status 
    - back to menu button can let you back to expenses tracker menu page
   ```
   
2. Sync with Bank:
   ```
    - click the sync the sync with bank button it will show the sync bank page 
    - then, you need to choose the bank company that you use and enter the bank account number 
    - after sync, you can get the transaction history and confirm the sync
    - lastly, the transaction history will automatically update to appliction
    - back to menu button can let you back to expenses tracker menu page
   ```

3. Add Expenses:
   ```
    - click the add expenses button if will show the add expenses page 
    - then, you need to enter the amount of expense with date, description and choose category
    - after add the expense, the expense will save into the application, and prompt out expenses status
    - back to menu button can let you back to expenses tracker menu page
   ```

4. View Expenses:
   ```
    - click the view expenses button it will show the expenses that you have enter just now
    - if you have sync the bank, you can see the transaction history inside the view expenses
    - after that you can see the detail about te expenses 
    - back to menu button can let you back to expenses tracker menu page
   ```

5. Report:
    ```
    - click the report button it will show the summary report page 
    - then, it will show your monthly expenses and expenses breakdown
    - monthly expenses show the sum of the expenses, and your budget status
    - expenses breakdown is the every ategory percentage 
    - if you want see chart, you can press show chart button, and it will show the chart is accourding the expenses breakdown
    - back to menu button can let you back to expenses tracker menu page
    ```

6. Exit:
    ```
    - exit button is to close the application and bank to application menu 
    ```

## GPA Calculator application
- This is a GPA Calculator application built using Python and Tkinter. It allows users to enter their student information and grades, and then calculates their GPA.
1. Student Information (Main Window):
   ```
    - Enter student information (name, student ID, programme, tutorial group, year of study) in the data entry.
    - After entering the information, the user clicks a "Validate" button to proceed.
    - If the input is correct and all fields are filled, the user can proceed to the next window to enter grade information.
    - If any information is missing or incorrect, the system prompts the user to re-enter the details.
   ```
2. Grade Information (Second Window):
   ```
    - Enter grade information (subject, grade, credit hour) in the data entry.
    - The user can add additional subjects by clicking the "Add Subject" button.
    - The user can remove any subject entry by clicking the "Delete Subject" button.
    - Once all subjects and grades are entered, the user clicks the "Calculate GPA" button to calculate the GPA.
    - The system will validate the grade and credit hour inputs before proceeding to calculate the GPA.
    - If all data is valid, the user can proceed to the third window to view their GPA result.
    - If any data is invalid (e.g., missing grades or invalid credit hours), the system prompts the user to re-enter the grade information.
   ```
3. GPA Result (Third Window):
   ```
    - The calculated GPA based on the input grades and credit hours.
    - Total Credit Hours Earned will also be displayed for user reference.
    - A summary of the grade information (subject, grade, and credit hours) is presented for the user's review.
    - The user can exit the program by clicking the "Exit Program" button, which shows a thank-you message before closing the application.
    - The user can return to the first window to enter new student information and perform another calculation by clicking the "Return to Main Window" button.
    ```
