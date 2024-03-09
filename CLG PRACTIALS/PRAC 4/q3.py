import os

diary_directory = "diary_entries"

def read_entry(entry_filename):
    with open(entry_filename, 'r') as file:
        entry_content = file.read()
    return entry_content

def create_entry(entry_filename, entry_content):
    with open(entry_filename, 'w') as file:
        file.write(entry_content)

def update_entry(entry_filename, updated_content):
    with open(entry_filename, 'w') as file:
        file.write(updated_content)

def append_to_entry(entry_filename, additional_content):
    with open(entry_filename, 'a') as file:
        file.write('\n' + additional_content)

def entry_exists(entry_filename):
    return os.path.exists(entry_filename)

def main():
    if not os.path.exists(diary_directory):
        os.makedirs(diary_directory)

    while True:
        print("1. Read Entry")
        print("2. Create Entry")
        print("3. Update Entry")
        print("4. Append to Entry")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            entry_filename = input("Enter the filename of the entry: ")
            if entry_exists(os.path.join(diary_directory, entry_filename)):
                entry_content = read_entry(os.path.join(diary_directory, entry_filename))
                print("Entry Content:")
                print(entry_content)
            else:
                print("Entry does not exist.")
        elif choice == "2":
            entry_filename = input("Enter the filename of the new entry: ")
            entry_content = input("Enter the content of the new entry: ")
            create_entry(os.path.join(diary_directory, entry_filename), entry_content)
            print("Entry created successfully.")
        elif choice == "3":
            entry_filename = input("Enter the filename of the entry to update: ")
            if entry_exists(os.path.join(diary_directory, entry_filename)):
                updated_content = input("Enter the updated content: ")
                update_entry(os.path.join(diary_directory, entry_filename), updated_content)
                print("Entry updated successfully.")
            else:
                print("Entry does not exist.")
        elif choice == "4":
            entry_filename = input("Enter the filename of the entry to append: ")
            if entry_exists(os.path.join(diary_directory, entry_filename)):
                additional_content = input("Enter the additional content: ")
                append_to_entry(os.path.join(diary_directory, entry_filename), additional_content)
                print("Content appended successfully.")
            else:
                print("Entry does not exist.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
