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
	#set up framework
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
		if course_code in self.courses: #checks if course is a key in dictionary courses
			return self.courses[course_code] #return old object
		else:
			self.courses[course_code] = Course(course_code, credits, []) #create new object
			return self.courses[course_code] #returns the newly created object
	
	#For add_course and add_student, we could switch the if and else statements so we have "if course_code not in self.courses."

	def add_student(self, student_id, name): #will create student object if does not exist
		if student_id in self.students:
			return self.students[student_id] ##return the existing object
		else:
			self.students[student_id] = Student(student_id, name, {}) #create a new object
			return self.students[student_id] #return the newly created object
	
	def get_student(self, student_id): #returns the student object for that ID (or None if not found).
		if student_id in self.students:
			return self.students[student_id] #returns corresponding student object
		else:
			return None

	def get_course(self, course_code):#returns the course object for that code (or None if not found).
		if course_code in self.courses:
			return self.courses[course_code] #returns existing course object
		else:
			return None #if no object is found, returns None

	def get_course_enrollment(self, course_code):#returns the number of students enrolled in the given course.
		return len(self.courses[course_code].students) #finds length of list of students in corresponding course object given the course code
	#create conditional for whether course code actually exists in courses dict (return error if not)

	def get_students_in_course(self, course_code):
		return self.courses[course_code].students #returns a list of student objects enrolled in the given course.
	#create condition for if course code exists in dict 



#from csv course_catalog
c = {"CSE1010": Course("CSE1010", 3, ['111', '222']), "CSE2050": Course("CSE2050", 2, ['111'])}
s = {"111": Student("111",'joe', {"CSE1010":'B', "CSE2050":'A'}), '222': Student("222", 'jane', {"CSE1010": 'A'})}
obj1 = University(s, c) #test object of university using student and course test dictionaries
print(obj1.add_course("CSE2500", 4)) #returns new object
print(obj1.add_course("CSE2050", 4)) #returns existing CSE2050 object

print(obj1.get_course("CSE1010")) #returns existing CSE1010 object
print(obj1.get_course("CSE2500")) #return CSE2500 object
print(obj1.get_course_enrollment("CSE1010")) #returns 2
print(obj1.get_course_enrollment("CSE2050")) #returns 1

print(obj1.get_students_in_course("CSE1010")) #returns list '111', '222'
print(obj1.get_students_in_course("CSE2050")) #returns list '111'
print(obj1.get_students_in_course("CSE2500")) #returns empty list []


#Figure out how to debug the code.