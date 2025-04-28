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
    
#Take in which company we are gonna use, according to the log in
def company(company):
    
    while True:
        #Before starting, load the companies into an array
        companies = load_companies("companyinfo.txt")

        #Ask the users for the first option
        print(" 1) Edit Company Profile")
        print(" 2) View jobs posted")
        print(" 3) Add new job")
        print(" 4) Exit")

        option = check_input("Enter option: ", 1, 4)

        #If option is 1, then, show the currennt company info
        if option == 1:
            
            index = find_company(company, companies)

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

        elif option == 4:
            break

#Start of main code

print("@@@@ SCSU Jobs Portal @@@@")
print("1. View Jobs")
print("2. Login")
print("0. Exit")

check_input("Enter option: ", 0, 2)

company(input("Commpany: "))