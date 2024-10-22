#Loan Management System Library

This library provides a set of functionalities for managing loans in a financial application, including loan applications, EMI calculations, loan eligibility checks, and custom exception handling. 
The primary modules include tools for calculating EMIs, checking customer loan eligibility, managing data helpers, and handling custom exceptions.

##Features:
    1.Loan EMI Calculation: Calculate the equated monthly installment (EMI) for a specific loan based on the principal, interest rate, and loan term.
    2.Loan Eligibility Check: Determine whether a customer is eligible for a loan based on their credit score, income, previous loans, and other parameters.
    3.Custom Exception Classes: Handle errors related to loan processing, customer eligibility, and payment issues.
    4.Data Validators: Utility functions to support data validations across the system.

##Installation:

To use the loan management library in your Django project:
	```	
		pip install x23113383_loan_management_system
 	  
    ````
##Functions Overview:
###1. calculate_emi(loan_application)

	This function calculates the Equated Monthly Installment (EMI) for a loan based on the loan amount, interest rate, and loan term. The EMI is calculated using the following formula:
	```
	  EMI=P⋅r⋅(1+r)**n / (1+r)**n−1
    ````
	Where:
		P = Loan amount (Principal)
		r = Monthly interest rate (Annual interest rate / 12 / 100)
		n = Loan tenure (Number of months)

	Parameters:
		loan_application: The loan application object containing the loan amount and loan type.
		loan: The loan object with the loan tenure.
		loan_customer: The loan customer object (used for future extensions).

	Returns:
		The calculated EMI amount, rounded to two decimal places.

	Example Usage:
	```
		emi = calculate_emi(loan_application, loan, loan_customer)
		print(f"Monthly EMI: {emi}")
			
	```

##Detailed Explanation:
	The function extracts the principal amount and the interest rate from the loan_application and converts the annual interest rate to a monthly interest rate. 
	Using the formula, it calculates the EMI based on the loan term (in months) and returns the amount the customer needs to pay each month.
	If the interest rate is zero, the EMI is simply the loan amount divided by the loan term.
	
###2. check_loan_eligibility(loan_customer, loan_type, previous_loans)

	This function checks whether a customer is eligible for a particular loan based on multiple factors, such as:

		Credit score
		Monthly or yearly income
		Total pending EMI payments
		Number of overdue loans
		Interest rate for the new loan
		Previous loans of the same type (customers are not allowed to have more than three active loans of the same type)

	Parameters:
		loan_customer: The customer applying for the loan.
		loan_type: The type of loan being applied for (e.g., personal loan, vehicle loan, etc.).
		previous_loans: A list of the customer’s previous loans, including those that are still active and any overdue loans.

	Returns:
		Max Amount Eligible by the customer for this LoanType
		
	Throws:
		CustomerNotEligible
	
	Example:
	```
		max_loan_amount_eligible = get_customer_eligibility(loan_type, loan_customer, previous_loans)
		print(f"Max LoanAmount Eligible: {max_loan_amount_eligible}")
		
	```

##Detailed Explanation:
	The function checks whether the customer’s credit score meets the minimum requirement for the loan type. It also verifies whether the customer’s income can support additional EMIs based on their current EMI commitments (from active loans). 
	Customers with overdue loans or more than three active loans of the same type are automatically disqualified.
	Additionally, the function calculates the maximum loan amount a customer can apply for based on their remaining EMI capacity (income minus existing EMI obligations) and the interest rate of the new loan.






