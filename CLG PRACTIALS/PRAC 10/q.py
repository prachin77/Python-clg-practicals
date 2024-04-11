class StudentRepository:
    def __init__(self):
        self.students = {}

    def insert_student(self, sid, name, contact_number, status):
        self.students[sid] = {'name': name, 'contact_number': contact_number, 'status': status}

    def update_student(self, sid, name=None, contact_number=None, status=None):
        if sid in self.students:
            if name:
                self.students[sid]['name'] = name
            if contact_number:
                self.students[sid]['contact_number'] = contact_number
            if status:
                self.students[sid]['status'] = status
        else:
            print("Student with ID {} not found.".format(sid))

    def remove_duplicates(self):
        unique_students = {}
        for sid, student_details in self.students.items():
            if student_details not in unique_students.values():
                unique_students[sid] = student_details
        self.students = unique_students

    def fetch_current_students(self):
        current_students = {}
        for sid, student_details in self.students.items():
            if student_details['status'] == 'current student':
                current_students[sid] = student_details
        return current_students


# Sample usage of the StudentRepository class
repository = StudentRepository()

# Inserting student records
repository.insert_student(1, 'Alice', '1234567890', 'current student')
repository.insert_student(2, 'Bob', '9876543210', 'alumni')
repository.insert_student(3, 'Charlie', '5555555555', 'current student')
repository.insert_student(4, 'David', '4444444444', 'alumni')
repository.insert_student(5, 'Alice', '1234567890', 'current student')  # Duplicate entry

# Update student record
repository.update_student(5, name='Alice Smith', contact_number='9999999999')

# Remove duplicate entries
repository.remove_duplicates()

# Fetch records related to current students
current_students = repository.fetch_current_students()

# Display current students
print("Current Students:")
for sid, student_details in current_students.items():
    print("ID:", sid)
    print("Name:", student_details['name'])
    print("Contact Number:", student_details['contact_number'])
    print("Status:", student_details['status'])
    print()
