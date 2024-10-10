employees = [
    {
        "employee_name": "Juan Carlos", 
        "job_title": "Software Developer", 
        "employee_id": "EMP0123", 
        "age": 36, 
        "date_of_hire": "March 22, 2009"
    },
    {
        "employee_name": "Jose Rizal", 
        "job_title": "IT Support Specialist", 
        "employee_id": "EMP0234", 
        "age": 40, 
        "date_of_hire": "February 9, 2014"
    },
    {
        "employee_name": "Juan Luna", 
        "job_title": "Network Administrator", 
        "employee_id": "EMP0345", 
        "age": 37, 
        "date_of_hire": "October 10, 2016"
    },
    {
        "employee_name": "Andres Bonifacio", 
        "job_title": "Software Engineer", 
        "employee_id": "EMP0456", 
        "age": 38, 
        "date_of_hire": "December 10, 2010"
    },
    {
        "employee_name": "Justin Bieber", 
        "job_title": "Cyber Security Analyst", 
        "employee_id": "EMP0567", 
        "age": 40, 
        "date_of_hire": "June 20, 2008"
    }
]

for employee in employees:
    print(f"Employee Name: {employee['employee_name']} | Job Title: {employee['job_title']} | Employee ID: {employee['employee_id']} | Age: {employee['age']} | Date of Hire: {employee['date_of_hire']}")
