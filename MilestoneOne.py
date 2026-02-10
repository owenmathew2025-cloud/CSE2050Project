class Course:
	def init(self, course_code, credits, students):
		self.course_code = course_code
		self.credits = credits
		self.students = students #represents list of students - course roster
    
	def add_student(self, student):
		self.students.append(self.student)
   
	def get_student_count(self):
		pass


class Student:
	def __init__(self, student_id, name, courses):
		self.id = student_id
		self.name = name
		self.courses = courses #dictionary of courses student takes (course:grade)
	
	def enroll(self, course, grade): #enrolls student in course with the given grade; updates course roster
		pass
	
	def calculate_gpa(self): #finds GPA (based on graded courses and their credits)
		pass
	
	def get_courses(self): # returns list of course objects
		pass

	def get_course_info(self): #return summary of enrollments (course code, grade, credits)
		pass


class University:
	def __init__(self, students, courses): 
		self.students = students #dictionary of student objects (maps student_id to student object)
		self.courses = courses #dictionary of course objects (maps course_code to course object)
	
	def add_course(self, course_code, credits): #will create and store new course if it does not exist; return course object
		if course_code in self.courses: #cvhecks if course is a key in dictionary courses
			pass #return old object
		else:
			pass #create new object
	
	def add_student(self, student_id, name): #will create student object if does not exist
		if student_id in self.students:
			pass #return the existing object
		else:
			pass #create a new object
	
	def get_student(self, student_id):
		pass #returns the student object for that ID (or None if not found).
		if self.student_id in self.students:
			pass
		else:
			return None

	def get_course(self, course_code):
		pass #returns the course object for that code (or None if not found).
		
	def get_course_enrollment(self, course_code):
		pass #returns the number of students enrolled in the given course.
		
	def get_students_in_course(self, course_code):
		pass #returns a list of student objects enrolled in the given course.
