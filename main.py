# ------------------------------------------------- IMPORTS --------------------------------------------------- #

import pickle
from datetime import date
from colorama import Fore, Style, init

# ------------------------------------------------- CLASSES --------------------------------------------------- #

class Contact:
    def __init__(self, nickname: str, phone: str, firstName: str, lastName: str, email: str, notes: str, birthday: str, adress: str, createdAt: str, updatedAt: str, directory: str):
        """
        Initializes a new instance of the Contact class with the given parameters.

        Args:
            nickname (str): The nickname of the contact.
            phone (str): The phone number of the contact.
            firstName (str): The first name of the contact.
            lastName (str): The last name of the contact.
            email (str): The email address of the contact.
            notes (str): Any additional notes about the contact.
            birthday (str): The birthday of the contact.
            adress (str): The address of the contact.
            createdAt (str): The date and time when the contact was created.
            updatedAt (str): The date and time when the contact was last updated.
            directory (str): The directory where the contact is stored.

        Returns:
            None
        """
        self.contactNickname = nickname
        self.contactPhone = phone
        self.contactFirstName = firstName
        self.contactLastName = lastName
        self.contactEmail = email
        self.contactNotes = notes
        self.contactBirthday = birthday
        self.contactAddress = adress
        self.contactCreatedAt = createdAt
        self.contactUpdatedAt = updatedAt
        self.contactDirectory = directory
    
    def __str__(self):
        """
        Returns a string representation of the object.
        
        :return: A string containing the details of the object.
        :rtype: str
        """
        return f"\nNickname: {self.contactNickname}\nPhone: {self.contactPhone}\nFirst Name: {self.contactFirstName}\nLast Name: {self.contactLastName}\nEmail: {self.contactEmail}\nNotes: {self.contactNotes}\nBirthday: {self.contactBirthday}\nAddress: {self.contactAddress}\nCreated At: {self.contactCreatedAt}\nUpdated At: {self.contactUpdatedAt}\nDirectory: {self.contactDirectory.directoryName}"
    
    def showAllContacts(myPhone: list):
        """
        Generates a list of all contacts from the given phone directory and prints them.
        
        Parameters:
            myPhone (list): A list of phone directories.
            
        Returns:
            None
        """
        contacts = []
        print("\n")

        for directory in myPhone:
            for contact in directory.contacts:
                contacts.append(contact)

        for index, contact in enumerate(contacts):
            print(f"\n{separator}\n{index + 1}:\n\n{contact}\n{separator}")
        
        if contacts == []:
            Error("You don't have any contacts yet")
        print("\n")

    def editContact(contact: object):
        """
        Edit the contact information.

        Parameters:
        - contact: The contact object to be edited.

        Returns:
        None
        """
        contact.contactNickname = Asking("Edit contact nickname: ")
        contact.contactPhone = Asking("Edit contact phone: ")
        contact.contactFirstName = Asking("Edit contact first name: ")
        contact.contactLastName = Asking("Edit contact last name: ")
        contact.contactEmail = Asking("Edit contact email: ")
        contact.contactNotes = Asking("Edit contact notes: ")
        contact.contactBirthday = Asking("Edit contact birthday: ")
        contact.contactAddress = Asking("Edit contact address: ")
        contact.contactUpdatedAt = date.today()
        print("\n")

class Directory:
    def __init__(self, name: str, date: str, update: str, contacts=[]):
        """
        Initializes a new instance of the Directory class with the given parameters.

        Args:
            name (str): The name of the directory.
            date (str): The creation date of the directory.
            update (str): The last update date of the directory.
            contacts (list, optional): A list of contacts associated with the directory. Defaults to an empty list.
        """
        self.directoryName = name
        self.directoryCreatedAt = date
        self.directoryUpdatedAt = update
        self.contacts = contacts

    def __str__(self):
        """
        Returns a formatted string representation of the Directory object.
        This includes the directory name, date created, date updated, and a list of contacts.
        The contacts are displayed with an index number, and each contact's information is
        indented underneath the index number. If there are no contacts, a message is displayed.

        Returns:
            str: A formatted string representation of the ContactDirectory object.
        """
        
        contact_info = ""

        for i, contact in enumerate(self.contacts, start=1):
            if i > 1:
                contact_info += "\n"
            contact_info += f"   {i}:\n"
            # Utilisez la méthode __str__ de l'objet Contact en ajoutant une indentation
            contact_info += "\n".join(f"      {line}" for line in str(contact).split('\n'))
            contact_info += "\n"

        if not contact_info:
            contact_info = "   You don't have any contacts yet." + " " * 34

        formatted_output = f"{Separator()}\n \033[1mDirectory Name:\033[0m {self.directoryName}\n{Separator()}\n \033[1mDate Created:\033[0m {self.directoryCreatedAt}\n{Separator()}\n \033[1mDate Updated:\033[0m {self.directoryUpdatedAt}\n{Separator()}\n \033[1mContacts:\033[0m\n\n{contact_info}\n{Separator()}"

        return formatted_output

    def showAllDirectories(directories: list):
        """
        Generates a list of all directories from the given phone directory and prints them.
        
        Parameters:
            directories (list): A list of phone directories.
            
        Returns:
            None
        """
        print(f"\n{Separator()}")
        for index, directory in enumerate(directories):
            print(f"{index + 1}: {directory.directoryName}")
        print(f"{Separator()}\n")

    def showAllDirectoriesContent(directories: list):
        """
        Generates a list of all directories content from the given phone directories and prints them.
        
        Parameters:
            directories (list): A list of phone directories.
            
        Returns:
            None
        """
        for index, directory in enumerate(directories):
            Render(f"\n\n\nDirectory number {index + 1}: \n\n{directory}")
        print("\n")

    def showDirectoryContent(directory: object):
        """
        Prints the content of a directory.

        :param directory: An object representing the directory to be printed.
        :return: None
        """
        print(directory, "\n")
    
    def editDirectory(directory: object):
        """
        Edit the directory object by updating its name and the timestamp of its last update.

        Parameters:
        - directory: An object representing the directory to be edited.

        Returns:
        None
        """
        directory.directoryName = Asking("Edit directory name: ")
        directory.directoryUpdatedAt = date.today()

    def createContact(directory: object):
        """
        Creates a new contact and adds it to the specified directory.

        Args:
            directory (object): The directory object where the contact will be added.

        Returns:
            None
        """
        contactNickname = Asking("Enter the nickname of the contact: ")
        contactPhone = Asking("Enter the phone of the contact: ")
        contactFirstName = Asking("Enter the first name of the contact: ")
        contactLastName = Asking("Enter the last name of the contact: ")
        contactEmail = Asking("Enter the email of the contact: ")
        contactNotes = Asking("Enter the notes of the contact: ")
        contactBirthday = Asking("Enter the birthday of the contact: ")
        contactAddress = Asking("Enter the address of the contact: ")
        contactCreatedAt = date.today()
        contactUpdatedAt = date.today()
        print("\n")
        newContact =Contact(contactNickname, contactPhone, contactFirstName, contactLastName, contactEmail, contactNotes, contactBirthday, contactAddress, contactCreatedAt, contactUpdatedAt, directory)
        directory.contacts.append(newContact)
    
    def showDirectoryContacts(directory: object):
        """
        Show the contacts in a directory.

        Parameters:
            directory (Directory): The directory object containing the contacts.

        Returns:
            None
        """
        for index, contact in enumerate(directory.contacts, start=1):
            print(f"{index}: {contact.contactNickname}")
        print("\n")
        actionChoosed = Asking("Enter the ID of the contact you want to edit: ")
        if actionChoosed.isdigit():
            actionChoosed = int(actionChoosed)
            if actionChoosed > 0 and actionChoosed <= len(directory.contacts):
               Contact.editContact(directory.contacts[actionChoosed - 1])
            else:
                Error("Invalid input.")
        else:
            Error("Invalid input.")

    def editContact(directory: object):
        """
        Edits the contact information in the given directory.

        Parameters:
            directory (object): The directory object containing the contact information.

        Returns:
            None
        """
        directory.directoryName = Asking("Edit contact nickname: ")
        directory.Phone = Asking("Edit contact phone: ")
        directory.firstName = Asking("Edit contact first name: ")
        directory.lastName = Asking("Edit contact last name: ")
        directory.email = Asking("Edit contact email: ")
        directory.notes = Asking("Edit contact notes: ")
        directory.birthday = Asking("Edit contact birthday: ")
        directory.address = Asking("Edit contact address: ")
        directory.directoryUpdatedAt = date.today()
    
    def deleteContact(directory: object):
        """
        Deletes a contact from the given directory.

        Parameters:
        - directory (object): The directory object containing the contacts.

        Returns:
        None
        """
        for index, contact in enumerate(directory.contacts, start=1):
            print(f"{index}: {contact.contactNickname}")
        print("\n")
        actionChoosed = Asking("Enter the ID of the contact you want to delete: ")
        if actionChoosed.isdigit():
            actionChoosed = int(actionChoosed)
            if actionChoosed > 0 and actionChoosed <= len(directory.contacts):
                directory.contacts.pop(actionChoosed - 1)
            else:
                Error("Invalid input.")
        else:
            Error("Invalid input.")

# ------------------------------------------------ NECESSARY -------------------------------------------------- #

# Needed for the colorama library
init(autoreset=True)

listOfActions = {
    "0": "Show all directories",
    "1": "Show all contacts",
    "2": "Create a directory",
    "3": "Edit a directory",
    "4": "Delete a directory",
    "5": "Delete all directories",
    "6": "Create a contact",
    "7": "Edit a contact",
    "8": "Delete a contact",
    "9": "Delete all contacts",
    "q": "Quit the application"
}

# ---------------------------------------------- OUTPUT STYLING ----------------------------------------------- #

def Asking(message: str):
    """
    Asks the user for input and returns the input as a string.

    Args:
        message (str): The message to display to the user before asking for input.

    Returns:
        str: The input provided by the user.
    """
    return input(Fore.GREEN + "\n" + message + " " + Style.RESET_ALL)

def Error(message: str):
    """
    Print an error message with a red color.

    Args:
        message (str): The error message to be printed.

    Returns:
        None
    """
    return print(Fore.RED + "\n" + separator + "\n" + message +  "\n" + separator + "\n" + Style.RESET_ALL)

def Success(message: str):
    """
    Print a success message with a green color.

    Args:
        message (str): The success message to be printed.

    Returns:
        None
    """
    return print(Fore.GREEN + "\n" + separator + "\n" + message +  "\n" + separator + "\n" + Style.RESET_ALL)

def Menu(message: str):
    """
    Print a menu message with a blue color.

    Args:
        message (str): The list of menu options to be printed.

    Returns:
        None
    """
    return print(Fore.CYAN  + message  + Style.RESET_ALL)

def Render(message: str):
    """
    Print a message with a yellow color.

    Args:
        message (str): The message to be printed.

    Returns:
        None
    """
    return print(Fore.YELLOW  + message  + Style.RESET_ALL)

def Separator():
    """
    Print a separator with a green color.

    Args:
        None

    Returns:
        None
    """
    return Fore.GREEN  + separator  + Style.RESET_ALL

# Calculate the maximum key length and create a format string for key-value pairs in listOfActions to render the menu
max_key_length = max(len(key) for key in listOfActions.keys())
format_string = f"{{:<{max_key_length}}} : {{}}"

separator = "-" * 48

# ------------------------------------------ DATA SAVING AND LOADING ------------------------------------------- #

def saveData(myPhone: list):
    """
    Print an error message with a red color.

    Args:
        myPhone (list): The directories with their contacts to be saved.

    Returns:
        None
    """
    with open('myPhone.pkl', 'wb') as file:
        pickle.dump(myPhone, file)

def loadData():
    """
    Load data from a pickle file.

    This function attempts to open the file 'myPhone.pkl' in read binary mode. If the file is found, it loads the data using the pickle module and returns it. If the file is not found, it initializes an empty list and returns it.

    Returns:
        list: The loaded data from the pickle file, or an empty list if the file is not found.
    """
    try:
        with open('myPhone.pkl', 'rb') as file:
            myPhone = pickle.load(file)
    except FileNotFoundError:
        myPhone = []
    return myPhone

# ----------------------------------------------- MAIN PROGRAM ------------------------------------------------- #

while True:
    for key, action in listOfActions.items():
        Menu(format_string.format(key, action))

    actionChoosed = Asking("What do you want to do?")
    myPhone = loadData()

    if actionChoosed == "0":
        if not myPhone:
            separator = "-" * 48
            Error("You don't have any directory.")
        else:
            Directory.showAllDirectories(myPhone)

            listOfActionsSubMenu = {
                "0": "Show all directories content",
                "1": "Show specific directory content",
                "b": "Back to the main menu",
                "q": "Quit the application"
            }

            while True:
                for key, action in listOfActionsSubMenu.items():
                    print(f"{key}: {action}")

                actionChoosed = Asking("What do you want to do?")

                if actionChoosed == "0":
                    Directory.showAllDirectoriesContent(myPhone)
                elif actionChoosed == "1":
                    Directory.showAllDirectories(myPhone)
                    actionChoosed = input("Choose the directory id of the directory content you want to see: ")
                    if actionChoosed in ["1", "2"]:
                        print("\n")
                        Directory.showDirectoryContent(myPhone[int(actionChoosed) - 1])
                    else:
                        Error("Invalid input.")
                elif actionChoosed == "b":
                    print("\n")
                    break
                elif actionChoosed == "q":
                    exit()
                else:
                    Error("Invalid input.")
    elif actionChoosed == "1":
        Contact.showAllContacts(myPhone)
    elif actionChoosed == "2":
        directoryName = Asking("Enter the name of the directory:")
        directoryName = Directory(directoryName, date.today(), date.today())
        myPhone.append(directoryName)
        saveData(myPhone)
    elif actionChoosed == "3":
        if not myPhone:
            separator = "-" * 48
            Error("You don't have any directory.")
        else:
            Directory.showAllDirectories(myPhone)
            actionChoosed = Asking("Choose the directory id you want to edit:")
            if actionChoosed in ["1", "2"]:
                myPhone[int(actionChoosed) - 1].editDirectory()
                saveData(myPhone)
                print("\n")
            else:
                Error("Invalid input.")
    elif actionChoosed == "4":
        if not myPhone:
            separator = "-" * 48
            Error("You don't have any directory.")
        else:
            Directory.showAllDirectories(myPhone)
            actionChoosed = Asking("Choose the directory id you want to delete:")
            if actionChoosed in ["1", "2"]:
                del myPhone[int(actionChoosed) - 1]
                saveData(myPhone)
                print("\n")
            else:
                Error("Invalid input.")
    elif actionChoosed == "5":
        if not myPhone:
            separator = "-" * 48
            Error("You don't have any directory.")
        else:
            print("\n")
            myPhone = []
            saveData(myPhone)
    elif actionChoosed == "6":
        if not myPhone:
            separator = "-" * 48
            Error("You don't have any directory.")
        else:
            Directory.showAllDirectories(myPhone)
            contactDirectory = Asking("Enter the directory id you want to add the contact to:")
            Directory.createContact(myPhone[int(contactDirectory) - 1])
            saveData(myPhone)
    elif actionChoosed == "7":
        if not myPhone:
            separator = "-" * 48
            Error(f"You don't have any directory.")
        else:
            Directory.showAllDirectories(myPhone)
            num_directories = len(myPhone)
            actionChoosed = input(f"Choose the directory ID you want to edit a contact (1-{num_directories}): ")
            if actionChoosed.isdigit():
                actionChoosed = int(actionChoosed)
                if 1 <= actionChoosed <= num_directories:
                    Directory.showDirectoryContacts(myPhone[actionChoosed - 1])
                    saveData(myPhone)
                else:
                    Error("Invalid input.")
            else:
                Error("Invalid input.")
    elif actionChoosed == "8":
        if not myPhone:
            separator = "-" * 48
            Error(f"You don't have any directory.")
        else:
            Directory.showAllDirectories(myPhone)
            num_directories = len(myPhone)
            actionChoosed = input(f"Choose the directory ID you want to delete a contact (1-{num_directories}): ")
            if actionChoosed.isdigit():
                actionChoosed = int(actionChoosed)
                if 1 <= actionChoosed <= num_directories:
                    Directory.deleteContact(myPhone[actionChoosed - 1])
                    saveData(myPhone)
                else:
                    print("Invalid input.")
            else:
                print("Invalid input.")
    elif actionChoosed == "9":
        if not myPhone:
            separator = "-" * 48
            Error(f"You don't have any directory.")
        else:
            myPhone = []
            saveData(myPhone)
    elif actionChoosed == "q":
        exit()
    else:
        Error("Invalid input.")