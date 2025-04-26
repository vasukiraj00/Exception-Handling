from Student_Manager import StudentManager
def main():
    manager = StudentManager()  # Create the StudentManager object
    
    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            manager.add_student()  # Call add_student method
        elif choice == '2':
            manager.display_all_students()  # Display all students
        elif choice == '3':
            print("Exiting program...")  # Exit the loop and terminate
            break
        else:
            print("Invalid choice, please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
