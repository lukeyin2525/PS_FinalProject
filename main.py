#Function to check input, takes 3 parameters -  question to ask, lower limit of the input, upper limit of the inputs
def check_input(question, lower, upper):
    while True:
        try:
            choice = int(input(question))
            if choice < lower or choice > upper:
                print("Please enter either 0, 1 or 2.")
            else:
                return choice
        except:
            print("Please enter a valid number.")    

#Job listing system
def view_jobs(jobs):
    while True:
        #Display the job listings in a formatted table, aligning the columns
        print(f"{'Job Title':<20} {'Category':<20} {'Company':<15} {'Job Type':<20} {'Min Education':<15} {'Exp Req':<10}")
        #Displays index of each job in the list(1 to n) and the details of each job in the list
        for i, job in enumerate(jobs, start=1):
            print(f"{i}) {job.title:<20} {job.category:<20} {job.company:<15} {job.job_type:<20} {job.min_education:<15} {job.exp_required:<10}")
        print("To filter jobs, enter -1.")
        option = check_input("Enter the job number to view details, or 0 to go back: ", -1, len(jobs))

        #If user enters 0, exit the loop
        if option == 0:
            break

        #If user enters -1, call the filter_jobs function to filter jobs
        elif option == -1:
            filter_jobs(jobs)

        #If user enters a valid job number, display the details of that job
        else:
            job = jobs[option - 1]
            print(f"Job Title: {job.title}")
            print(f"Category: {job.category}")
            print(f"Pay: {job.pay}")
            print(f"Job Type: {job.job_type}")
            print(f"Min Education: {job.min_education}")
            print(f"Years of Experience required: {job.exp_required}")
            print(f"Company: {job.company}")
            print(f"Technical skills required: {', '.join(job.tech_skills)}")
            print(f"Managerial skills required: {', '.join(job.mgr_skills)}")
            print(f"Additional Job Description: {job.description}")
            print(f"Company Description: {job.company.description}")
            print(f"Company URL: {job.company.url}")
            input("Enter 0 to go back: ")

#Filter jobs using sequential search
def filter_jobs(jobs):
    #Filter options for user to pick
    print("1) Filter by Category")
    print("2) Filter by Job Type")
    print("3) Filter by Years Exp")
    print("4) Filter by Pay")
    option = check_input("Enter filter option: ", 1, 4) #Check input for valid option

    filtered_jobs = [] #Initialise empty list to store filtered jobs

    #If user selects option 1, filter by category
    if option == 1:
        category = input("Enter category (e.g., Cybersecurity, Software Engineering, A.I & Data Science): ").strip()
        for job in jobs:
            if job.category == category:
                filtered_jobs.append(job)

    #If user selects option 2, filter by job type
    elif option == 2:
        job_type = input("Enter job type (e.g., Full Time (Senior), Full Time (Junior), Part Time): ").strip()
        for job in jobs:
            if job.job_type == job_type:
                filtered_jobs.append(job)

    #If user selects option 3, filter by years of experience
    elif option == 3:
        years_exp = int(input("Enter years of experience: ").strip())
        for job in jobs:
            if int(job.exp_required) <= years_exp:
                filtered_jobs.append(job)

    #If user selects option 4, filter by pay
    elif option == 4:
        pay = int(input("Enter minimum pay: ").strip())
        for job in jobs:
            min_pay = int(job.pay.split(' to ')[0])  # Assumes format like "5000 to 7000"
            if min_pay >= pay:
                filtered_jobs.append(job)

    #Prints the filtered jobs
    print(f"{'Job Title':<20} {'Category':<20} {'Company':<15} {'Job Type':<20} {'Min Education':<15} {'Exp Req':<10}")
    for i, job in enumerate(filtered_jobs, start=1):
        print(f"{i}) {job.title:<20} {job.category:<20} {job.company:<15} {job.job_type:<20} {job.min_education:<15} {job.exp_required:<10}")

#Login System
def login_system():
    #Login system(Includes admin, company and jobseeker)
    while True:
        print("Enter username and password to login.")
        userInput = input("Enter username: ").strip()
        passwordInput = input("Enter password: ").strip()
        #Check if the username and password belongs to an admin, company or jobseeker
        with open("users.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                if len(parts) < 3:
                    continue
                username = parts[0].strip()
                password = parts[1].strip()
                user_type = parts[2].strip()

                #If the username and password match, proceed with role specific actions
                if username == userInput and password == passwordInput:
                    if user_type == "admin":
                        print("Welcome Admin!")
                        admin()
                        break
                    elif user_type == "company":
                        print("Welcome Company!")
                        company(username)
                        break
                    elif user_type == "jobseeker":
                        print("Welcome Jobseeker!")
                        jobseeker(username)
                        break
                    #If the username and password do not match, ask the user for input again
            print("Invalid username or password. Please try again.")

class Job:
    #CompanyTitle, Category, Job Type, Min Education, Exp Required
    def __init__(self, title, category, job_type, company, min_education, exp_required, tech_skills, mgr_skills, description):  
            self.title = title
            self.category = category
            self.job_type = job_type
            self.company = company
            self.min_education = min_education
            self.exp_required = exp_required
            self.tech_skills = tech_skills
            self.mgr_skills = mgr_skills
            self.description = description.strip()
            self.applicants = []
    
    def add_applicant(self,application):
        self.applicants.append(application)

class Jobseeker:
    def __init__(self, username, name, email, education, age, years_experience, tech_skills, mgr_skills, description, applications):
        self.username = username
        self.name = name
        self.email = email
        self.education = education
        self.age = age
        self.years_experience = years_experience
        self.tech_skills = tech_skills
        self.mgr_skills = mgr_skills
        self.description = description
        if applications:
            self.applications = applications
        else:
            self.applications = []

    #To add the job and application to both jobseeker and job class as a link
    def apply_for_job(self, job):
        application = Application(self, job)
        self.applications.append(application)
        job.add_applicant(application)

#To use as a linkage between Jobseeker and Jobs
class Application:
    def __init__(self, jobseeker, job, company):
        self.jobseeker = jobseeker
        self.job = job
        self.company = company
        self.status = "Pending"  # Status can be "Pending", "Accepted", or "Rejected"

    def update_status(self, status):
        self.status = status

#Company class, will be used for two companies, include all information.
class Company:
    #When user calls the company( ), this will load the company 
    def __init__(self, name, url, username, description):
        self.name = name
        self.url = url
        self.username = username
        self.description = description
        self.jobs = []

    #If user chooses option to edit, they can put in the new name, url and description to edit.
    def edit_profile(self, new_name, new_url, new_description):
        self.name = new_name
        self.url = new_url
        self.description = new_description
    
    def add_job(self, job):
        self.jobs.append(job)

def load_companies(filename):
    #Create a list companies to go through
    companies = []

    #Take in the user given file name and open the file
    with open(filename, 'r') as file:

        #Split the file into different blocks/companies using '-----'
        blocks = file.read().split('-----')

        #Go through each block
        for block in blocks:

            #If the block is empty, skip
            if block.strip() == '':
                continue
            
            #Split the block into two parts, the header line and the description
            split_block = block.strip().split("\n", 1)
            header = split_block[0].strip()

            #For descriptions that might be more than 1 line
            description = "".join(split_block[1:]).strip()
            

            #If the splitted parts is less than 3, then continue, so no index error will occur when setting variables later
            parts = header.split(',')

            if len(parts) < 3:
                continue

            name = parts[0]
            url = parts[1]
            comp = parts[2]

            #Append it into a list while creating it as a class Company( )
            companies.append(Company(name.strip(), url.strip(), comp.strip(), description.strip()))

    #Finally, return the companies array
    return companies

def find_company(user, array):

    #Keep a record of which index we are at
    index = 0

    #Go through the array and see which username value matches
    for comp in array:
        if user.strip() == comp.username.strip():
            return index
        else:
            index += 1
    
    #If company is not found, return -1
    return -1

def save_companies(filename, companies):
    #Open the file and rewrite
    with open(filename, 'w') as file:
        #For every company, write into the original format, with ----- in between each company
        for company in companies:
            file.write(f"{company.name},{company.url},{company.username}\n")
            file.write(f"{company.description.strip()}\n")
            file.write("-----\n")
        
        print("Loading................")
        print("File has been successfully updated.")

def load_jobs(filename):
    #Create a list jobs to go through
    jobs = []

    #Take in the user given file name and open the file
    with open(filename, 'r') as file:

        #Split the file into different blocks/jobs using '-----'
        blocks = file.read().split('-----')

        #Go through each block
        for block in blocks:

            #If the block is empty, skip
            if block.strip() == '':
                continue
            
            #Split the block into two parts, the header line and the description
            split_block = block.strip().split("\n", 1)
            header = split_block[0].strip()

            #For descriptions that might be more than 1 line
            description = "".join(split_block[1:]).strip()
            

            #If the splitted parts is less than 3, then continue, so no index error will occur when setting variables later
            parts = header.split(',')

            if len(parts) < 6:
                continue

            title = parts[0]
            category = parts[1]
            job_type = parts[2]
            company = parts[3]
            min_education = parts[4]
            exp_required = parts[5]

            #Append it into a list while creating it as a class Job( )
            jobs.append(Job(title.strip(), category.strip(), job_type.strip(), company.strip(), min_education.strip(), exp_required.strip(), [], [], description.strip()))

    #Finally, return the jobs array
    return jobs

def load_jobseekers(filename):
    #Create a list jobseekers to go through
    jobseekers = []

    #Take in the user given file name and open the file
    with open(filename, 'r') as file:

        #Split the file into different blocks/jobseekers using '-----'
        blocks = file.read().split('-----')

        #Go through each block
        for block in blocks:

            #If the block is empty, skip
            if block.strip() == '':
                continue
            
            #Split the block into different lines
            lines = block.strip().splitlines()
            if len(lines) < 1:
                continue
            
            #First, the header
            header = lines[0].strip().split(',')
            if len(header) < 6:
                continue

            username = header[0].strip()
            name = header[1].strip()
            email = header[2].strip()
            education = header[3].strip()
            age = header[4].strip()
            years_experience = header[5].strip()
            
            #Then, empty strings to store the values
            tech_skills = ""
            mgr_skills = ""

            #Only if the number of values is greater than 1, split
            if len(lines) > 1:
                skills = lines[1].strip().split(',')
                if len(skills) > 0:
                    tech_skills = skills[0].strip()
                if len(skills) > 1:
                    mgr_skills = skills[1].strip()
             
            #Since, description is stored on third line, only if length of the lines are greater than 3, add description
            description = ""
            if len(lines) > 2:
                description = lines[2].strip()
            
            #List to store the applications
            apps = []
            #only after description
            for i in range(3, len(lines)):

                #If the line starts with "Application"
                line = lines[i].strip()
                if line.startswith("Application"):
                    app_info = line.split(":")[1].strip()
                    parts = app_info.split(",")
                    if len(parts) >= 3:
                        job_title = parts[0].strip()
                        job_company = parts[1].strip()
                        apps.append(Application(username, job_title, job_company))
            
            jobseeker = Jobseeker(username, name, email, education, age, years_experience, 
                                tech_skills, mgr_skills, description, apps)
            jobseekers.append(jobseeker)

    #Finally, return the jobseekers array
    return jobseekers

def link_applications(jobseekers, jobs):
    #Go through jobseeker
    for jobseeker in jobseekers:
        #Create a copy since we dont want to change the list directly to not have errors
        copy = jobseeker.applications
        for application in copy:
            # Find the job by title and company
            for job in jobs:
                if job.title.strip() == application.job.strip() and job.company.strip() == application.company.strip():
                    application.job = job
                    application.jobseeker = jobseeker
                    job.add_applicant(application)

                    #Replace the first placeholder since it doesnt include proper Job and Jobseeker Object
                    jobseeker.applications.pop(0) 


def save_jobs(filename, jobs):
    #Open the file and rewrite
    with open(filename, 'w') as file:
        #For every job, write into the original format, with ----- in between each job
        for job in jobs:
            file.write(f"{job.title},{job.category},{job.job_type},{job.company},{job.min_education},{job.exp_required}\n")
            file.write(f"{job.description.strip()}\n")
            file.write("-----\n")
        
        print("Loading................")
        print("File has been successfully updated.")
        print()

def save_jobseekers(filename, jobseekers):
    #Open the file and rewrite
    with open(filename, 'w') as file:
        #For every jobseeker, write into the original format, with ----- in between each jobseeker
        for jobseeker in jobseekers:
            file.write(f"{jobseeker.username},{jobseeker.name},{jobseeker.email},{jobseeker.education},{jobseeker.age},{jobseeker.years_experience}\n")
            file.write(f"{jobseeker.tech_skills.strip()},{jobseeker.mgr_skills.strip()}\n")
            file.write(f"{jobseeker.description.strip()}\n")
            for application in jobseeker.applications:
                file.write("Application: ")
                file.write(f"{application.jobseeker},{application.job.title},{application.status}\n")
            file.write("-----\n")
        
        print("Loading................")
        print("File has been successfully updated.")

#Take in which company we are gonna use, according to the log in
def company(company):
    
    while True:
        #Before starting, load the companies into an array
        companies = load_companies("companyinfo.txt")
        jobs = load_jobs("jobs.txt") 
        jobseekers = load_jobseekers("jobseeker.txt")
        
        link_applications(jobseekers, jobs)
        
        index = find_company(company, companies)

        #Ask the users for the first option
        print(" 1) Edit Company Profile")
        print(" 2) View jobs posted")
        print(" 3) Add new job")
        print(" 4) Exit")

        option = check_input("Enter option: ", 1, 4)

        #If option is 1, then, show the currennt company info
        if option == 1:

            if index == -1:
                print("The company does not exist.")
            
            print(f"Company index : {index}")
            print(f"Company Name : {companies[index].name}")
            print(f"Company Url: {companies[index].url}")
            print(f"Company Description: {companies[index].description}")

            answer = check_input("Enter 1 to edit, or 0 to return back to menu", 0, 1)

            if answer == 1:

                #Ask the user for new descriptions
                new_name = input("Enter the new company name: ")
                new_url = input("Enter the new company url: ")
                new_description = input("Enter the new company description: ")

                companies[index].name = new_name
                companies[index].url = new_url
                companies[index].description = new_description

                save_companies("companyinfo.txt", companies)
            
            elif answer == 0:
                continue
        
        if option == 2:
            #If option is 2, then show the jobs that the company has posted
            print("Jobs posted by the company:")
            i = 1
            job_index = {}
            for job in jobs:
                if job.company == companies[index].username:
                    print(f"{index}) Title: {job.title}, Category: {job.category}, Job Type: {job.job_type}, Min Education: {job.min_education}, Exp Required: {job.exp_required}")
                    print(f"Description: {job.description}")
                    job_index[i] = job
                    i+=1
            
            if len(job_index) == 0:
                print("No jobs posted by the company.")
                continue
            else:
                option = check_input("Enter the number of job to view in detail, or 0 to exit", 1,i)

                if option == 0:
                    continue
                else:

                    #Get the selected job from the dictionary
                    selected_job = job_index[option]
                    #Get how many applicants there are
                    print(f"There are {len(selected_job.applicants)} applicants for this job.")
                    option = check_input("Enter 1 to view applicants, or 0 to exit",0,1)

                    if option == 1:
                        print(f"{"":<4} {"Name":<20} {"Age":<15} {"Education":<20} {"Years Experience":<25}")
                        index = 1
                        for applicant in selected_job.applicants:
                            print(f"{index}{")":<3} {applicant.jobseeker.name :<20} {applicant.jobseeker.age :<15} {applicant.jobseeker.education:<20} {applicant.jobseeker.years_experience:<25}")

        elif option == 4:
            break

#Start of main code

print("@@@@ SCSU Jobs Portal @@@@")
print("1. View Jobs")
print("2. Login")
print("0. Exit")

option = check_input("Enter option: ", 0, 2)

if option == 1:
    #Load the jobs from the file
    jobs = load_jobs("jobs.txt")
    view_jobs(jobs)

elif option == 2:
    login_system()

elif option == 0:
    print("Exiting the application. Thank you for using SCSU Jobs Portal.")