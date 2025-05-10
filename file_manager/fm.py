import os
import shutil
import time as t
from termcolor import colored
import random
import string

print(colored("________ File Manager ________", "red"))

#| • 'new' = store data | • 'check' = check data | • 'update' = update data | • 'delete' = delete data | • 'all' = show all data names | • 'cf' = create new folder | • 'cd' = navigate to folder | • 'cd ..' = go back | • 'list' = list all folders | • 'del' = delete folder | • 'exit' = quit | :


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_folder(folder_name):
    try:
        os.makedirs(folder_name, exist_ok=True)
        print(colored(f"□ Folder '{folder_name}' created successfully.", "green"))
    except Exception as e:
        print(colored(f"■ Failed to create folder '{folder_name}': {str(e)}", "red"))

def store_data(name, data, current_folder="default"):
    create_folder(current_folder)
    with open(os.path.join(current_folder, "data.txt"), "a") as file:
        file.write(f"{name}:{data}\n")

def check_data(name, current_folder="default"):
    try:
        with open(os.path.join(current_folder, "data.txt"), "r") as file:
            lines = file.readlines()
            for line in lines:
                entry_name, entry_data = line.strip().split(":", 1)
                if entry_name == name:
                    return entry_data
        return None
    except FileNotFoundError:
        return None

def update_data(name, new_data, current_folder="default"):
    updated = False
    try:
        with open(os.path.join(current_folder, "data.txt"), "r") as file:
            lines = file.readlines()
        
        with open(os.path.join(current_folder, "data.txt"), "w") as file:
            for line in lines:
                entry_name, entry_data = line.strip().split(":", 1)
                if entry_name == name:
                    file.write(f"{name}:{new_data}\n")
                    updated = True
                else:
                    file.write(line)
        
        if not updated:
            store_data(name, new_data, current_folder)
    
    except FileNotFoundError:
        store_data(name, new_data, current_folder)

def delete_data(name, current_folder="default"):
    try:
        with open(os.path.join(current_folder, "data.txt"), "r") as file:
            lines = file.readlines()
        
        with open(os.path.join(current_folder, "data.txt"), "w") as file:
            for line in lines:
                entry_name, entry_data = line.strip().split(":", 1)
                if entry_name != name:
                    file.write(line)
        
        print(colored(f"□ Data for {name} has been deleted from folder '{current_folder}'.", "red"))
    
    except FileNotFoundError:
        print(colored(f"■ File not found. No data to delete in folder '{current_folder}'.", "red"))

def display_all_data_names(current_folder="default"):
    try:
        with open(os.path.join(current_folder, "data.txt"), "r") as file:
            lines = file.readlines()
            if lines:
                print(f"|| All stored data in folder '{current_folder}' ||")
                print(" ")
                t.sleep(0.5)
                for line in lines:
                    entry_name, entry_data = line.strip().split(":", 1)
                    print(entry_name)
            else:
                print(f"No data found in folder '{current_folder}'.")
    except FileNotFoundError:
        print(f"No data found in folder '{current_folder}'.")

def display_all_folders(current_folder="default"):
    try:
        all_folders = [f for f in os.listdir(current_folder) if os.path.isdir(os.path.join(current_folder, f))]
        
        if all_folders:
            print(f"|| All folders in '{current_folder}' ||")
            print(" ")
            t.sleep(0.5)
            for folder in all_folders:
                print(folder)
        else:
            print(f"No folders found in '{current_folder}'.")
    except FileNotFoundError:
        print(f"No folders found in '{current_folder}'.")

def delete_folder(folder_name):
    print(" ")
    t.sleep(1)
    try:
        shutil.rmtree(folder_name)
        print(colored(f"□ Folder '{folder_name}' and its contents have been deleted.", "red"))
        print(" ")
    except Exception as e:
        print(f"■ Failed to delete folder '{folder_name}': {str(e)}")

def rename_folder(current_folder, old_name, new_name):
    try:
        old_path = os.path.join(current_folder, old_name)
        new_path = os.path.join(current_folder, new_name)
        os.rename(old_path, new_path)
        print(colored(f"□ Folder '{old_name}' has been renamed to '{new_name}'.", "green"))
    except Exception as e:
        print(f"■ Failed to rename folder '{old_name}': {str(e)}")

def install_requirements():
    print("To install required libraries, run the following commands:")
    print("pip install termcolor")

def main():
    current_folder = "default"
    print("Welcome to File Executor. You can use the following commands:")
    print("new - store data | check - check data | update - update data | delete - delete data | all - show all data names | cf - create folder | cd - navigate to folder | del - delete folder | exit - quit")
    install_requirements()

    while True:
        action = input("X》 ").strip().lower()
        
        print(" ")

        if action == "new":
            name = input("Enter the name of the data: ")
            data = input("Enter the data to store: ")
            store_data(name, data, current_folder)
            print(" ")
            t.sleep(1)
            print(colored(f"□ Data saved to '{current_folder}/data.txt'", "green"))
            print(" ")

        elif action == "check":
            name = input("Enter the name of the data to check: ")
            t.sleep(1)
            print("Checking...")
            t.sleep(1)
            print(" ")
            data = check_data(name, current_folder)
            if data:
                print(colored(f"▪︎ Data found for {name} in folder '{current_folder}': {data}", "green"))
                print(" ")
            else:
                print(f"Data not found in folder '{current_folder}'.")
                print(" ")
        
        elif action == "update":
            name = input("Enter the name of the data to update: ")
            print(" ")
            new_data = input("Enter the new data: ")
            update_data(name, new_data, current_folder)
            t.sleep(1)
            print(colored(f"□ Data for {name} has been updated in folder '{current_folder}'.", "green"))
            print(" ")

        elif action == "delete":
            name = input("Enter the name of the data to delete: ")
            t.sleep(1)
            print(" ")
            delete_data(name, current_folder)
            print(" ")

        elif action == "all":
            t.sleep(1)
            print(" ")
            display_all_data_names(current_folder)
            print(" ")

        elif action == "rs":
            a = 1
            for a in range(14):
                print("Refreshing....", a)
                a += 1
                t.sleep(0.3)
                b = 13
                c = 2
                while b:
                    print(colored("Imprompt", "red"))
                    t.sleep(0.5)
                    print("fetching....", b, b, a, c)
                    b += 1
                    a += 2
                    c -= 10
        			
        elif action == "rp":
            def generate_random_string(length=4):
                return ''.join(random.choice(string.ascii_letters) for _ in range(length))
            def generate_random_string2(length=6):
                return ''.join(random.choice(string.ascii_letters) for _ in range(length))
            while True:
                random_string = generate_random_string()
                random_string2 = generate_random_string2()
                print(random_string, "|", random_string2)
                t.sleep(0.1)

        elif action.startswith("cd "):
            _, folder = action.split(" ", 1)
            if folder == "..":
                if current_folder != "default":
                    current_folder = os.path.dirname(current_folder)
                    t.sleep(1)
                    print(f"□ Navigated back to folder '{current_folder}'.")
                else:
                    print("■ Already at root folder.")
            else:
                new_folder = os.path.join(current_folder, folder)
                if os.path.exists(new_folder) and os.path.isdir(new_folder):
                    current_folder = new_folder
                    t.sleep(1)
                    print(f"□ Navigated to folder '{current_folder}'.")
                else:
                    print(f"■ Folder '{new_folder}' does not exist.")

        elif action == "cf":
            folder_name = input("Enter the name of the new folder: ")
            create_folder(os.path.join(current_folder, folder_name))
            print(" ")

        elif action.startswith("del "):
            _, folder_to_delete = action.split(" ", 1)
            folder_path = os.path.join(current_folder, folder_to_delete)
            if os.path.exists(folder_path) and os.path.isdir(folder_path):
                delete_folder(folder_path)
            else:
                print(f"■ Folder '{folder_to_delete}' does not exist or is not a directory.")

        elif action.startswith("rename "):
            try:
                _, old_name, new_name = action.split(" ", 2)
                rename_folder(current_folder, old_name, new_name)
            except ValueError:
                print("■ Invalid command format. Use 'rename <old_name> <new_name>'.")

        elif action == "list":
            t.sleep(1)
            print(" ")
            display_all_folders(current_folder)
            print(" ")

        elif action == "exit":
            print("Exiting the program.")
            break

        elif action == "clear":
            clear_screen()
         
        elif action == "exp":
            a = 138282828.0293
            b = 2294938282838.293
            c = 1
            for a in range(299248):
                print(colored(a + b, "red"))
                print(colored(c + b, "green"))
                
                a += 32934.0238
                b -= 3.28385848328294959595858483
                c += b

        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
