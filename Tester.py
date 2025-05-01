# Job listing system
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
            print(f"Company Description: {job.company_description}")
            print(f"Company URL: {job.company_url}")
            input("Enter 0 to go back: ")

# Filter jobs using sequential search
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

    # Prints the filtered jobs
    print(f"{'Job Title':<20} {'Category':<20} {'Company':<15} {'Job Type':<20} {'Min Education':<15} {'Exp Req':<10}")
    for i, job in enumerate(filtered_jobs, start=1):
        print(f"{i}) {job.title:<20} {job.category:<20} {job.company:<15} {job.job_type:<20} {job.min_education:<15} {job.exp_required:<10}")
