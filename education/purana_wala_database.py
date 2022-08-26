import sqlite3
from time import time
import os
conn = sqlite3.connect('godseye.db',check_same_thread=False)

# conn.execute('''CREATE TABLE Jobs 
#          (JobID INTEGER PRIMARY KEY AUTOINCREMENT,
#          Job_title           TEXT    NOT NULL,
#          salary            INT     NOT NULL,
#          Description        TEXT,
#          skills_req         TEXT);''')
# conn.execute("ALTER TABLE jobs ADD category TEXT DEFAULT 'Computer Science' NOT NULL")
# conn.execute("ALTER TABLE jobs ADD empID INTEGER DEFAULT '1' NOT NULL")


def add_job(title, salary, desc, skills_req, category, empID):
    s="INSERT INTO jobs (job_title, salary, Description, skills_req, category, empID) VALUES('"+title+"', '"+str(salary)+"', '"+desc+"', '"+skills_req+"', '"+category+"', '"+str(empID)+"')"
    print(s)
    conn.execute(s)
    conn.commit()

# add_job("Dancer required in thapar University", "1000000", "We are looking for a passionate dancer", "expert in folk dance", "Dancer", "2")


def get_jobs(category):
    s="select * from jobs where category='"+category+"' "
    cursor = conn.execute(s)
    print(cursor)
    # print("@")
    res=[]
    for row in cursor:
        #print(row)
        res.append(row)
    return res

# ans=get_jobs("Dancer")
# for row in ans:
#     print(row)

# conn.execute('''CREATE TABLE applications 
#          (applicationID INTEGER PRIMARY KEY AUTOINCREMENT,
#          applicantID INTEGER NOT NULL,
#          JobID INT NOT NULL);''')

def apply(jobID, userID):
    s="INSERT INTO applications (applicantID, JobID) VALUES('"+str(userID)+"','"+str(jobID)+"')"
    # print(s)
    conn.execute(s)
    conn.commit()


def your_applications(userID):
    s="SELECT * from applications where applicantID='"+str(userID)+"'"
    print(s)
    cursor=conn.execute(s)
    res=[]
    for row in cursor:
        #print(row)
        res.append(row)
    return res

# apply(5, 1)
# apply(6, 1)
# out=your_applications(1)
# print(out)
# out=your_applications(0)
# print(out)

# conn.execute('''CREATE TABLE feedback 
#          (sno INTEGER PRIMARY KEY AUTOINCREMENT,
#          userID int NOT NULL,
#          rating INT NOT NULL);''')

def feedback(userID, rating):
    s="INSERT INTO feedback (userID, rating) VALUES('"+str(userID)+"', '"+str(rating)+"')"
    print(s)
    conn.execute(s)
    conn.commit()

# feedback(1, 5)
# cursor=conn.execute("select * from feedback")
# for row in cursor:
#     print(row)


# conn.execute('''CREATE TABLE courses 
#          (courseID INTEGER PRIMARY KEY AUTOINCREMENT,
#          Title TEXT NOT NULL,
#          description TEXT NOT NULL,
#          address TEXT NOT NULL);''')


def add_courses(title, description):
    address=title+str(round(time()))
    s="INSERT INTO courses(title, description, address) values('"+title+"', '"+description+"', '"+address+"')"
    print(s)
    conn.execute(s)
    conn.commit()
    directory = address
    parent_dir = "courses"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print("Directory '% s' created" % directory)

# add_courses("Beginner guide to braile devices", "In this we will learn about using braile devices")
# add_courses("sign adaptation for blinds", "We will learn about signs adaptation")
# add_courses("social studies for blinds", "specially designed social studies curriculum for blinds")
# conn.execute("delete from courses where courseID>=13 and courseID<=18")
def courses_available():
    s="select * from courses"
    cursor=conn.execute(s)
    res=[]
    for row in cursor:
        res.append(row)
    return res

# out=courses_available()
# for row in out:
#     print(row)

# add_courses("graph theory", "abcdefgh ijklmnop qrst")

# print(courses_available())

# conn.execute('''CREATE TABLE users 
#          (userID INTEGER PRIMARY KEY AUTOINCREMENT,
#          fname           TEXT    NOT NULL,
#          lname            TEXT,
#          email        TEXT NOT NULL
#          );''')


# conn.execute("alter table users add password TEXT")
# conn.execute("alter table users add mentorID INT")

# conn.execute('''CREATE TABLE facial 
#          (faceID INTEGER PRIMARY KEY AUTOINCREMENT,
#          Name           TEXT    NOT NULL,
#          userID            INT     NOT NULL);''')

# conn.execute("alter table facial add address TEXT")


def add_user(fname, lname, email, password):
    s="INSERT INTO users (fname, lname, email, password, mentorID) VALUES('"+fname+"', '"+lname+"', '"+email+"', '"+password+"', -1 )"
    print(s)
    conn.execute(s)
    conn.commit()

# add_user("jashan", "singh", "jashan@gmail.com", "apoorv1234")

def verify_user(email, password):
    s="select userID, fname, lname from users where email='"+email+"' and password='"+password+"' "
    print(s)
    cursor=conn.execute(s)
    for row in cursor:
        return [row[0],row[1],row[2]]
    return [-1,-1,-1]

# print(verify_user("apoorv@gmail.com", "apoorv1234"))

def add_relative(userID, name, address):
    s="INSERT INTO facial(name, userID, address) values( '"+name+"', '"+str(userID)+"', '"+address+"' )"
    conn.execute(s)
    conn.commit()

# add_relative(1, "jashan", "abcd.jpg")

def who_and_whos(faceID):
    s="select userID, name from facial where faceID='"+str(faceID)+"' "
    print(s)
    cursor=conn.execute(s)
    for row in cursor:
        return [row[1], row[0]]
    return {-1, -1}

# print(who_and_whos(2))



# conn.execute('''CREATE TABLE mentor
#           (mentorID INTEGER PRIMARY KEY AUTOINCREMENT,
#           userID INT NOT NULL,
#           Name           TEXT    NOT NULL,
#           MeetingLink    INT     NOT NULL);''')

#conn.execute("ALTER TABLE mentor ADD password TEXT")
#conn.execute("ALTER TABLE mentor ADD email TEXT")
def add_mentor(name, email ,password):
    s = "select userID from users where mentorID=-1"
    cursor = conn.execute(s)
    userID = -1
    for row in cursor:
        userID = row[0]
        break
    s = "INSERT INTO mentor (userID, name, email ,password, meetingLink) VALUES('" + \
        str(userID)+"',  '"+name+"', '"+email+"', '"+password+"', 'none') "
    conn.execute(s)
    conn.commit()

def verify_mentor(email, password, meetlink):
    s = "select mentorID, userID, name from mentor where email='" + \
        email+"' and password='"+password+"' "
    print(s)
    cursor = conn.execute(s)
    for row in cursor:
        mentorID=row[0]
        s="UPDATE mentor set meetinglink='"+meetlink+"' where mentorID='"+str(mentorID)+"' "
        return [row[1], row[2]]
    return [-1, -1]

# add_mentor("arnav", "google.com")


def mentor_details(userID):
    s = "select mentorID, name, meetingLink from mentor where userID='" + \
        str(userID)+"' "
    cursor = conn.execute(s)
    for row in cursor:
        return [row[0], row[1], row[2]]
    return [-1, -1, -1]

#print(mentor_details(1))
#add_user('Ritik','Puri','asdg@gmail.com','123456')
# s = "select * from users"
# cursor = conn.execute(s)
# for row in cursor:
#     print(row)
#add_relative(0,"Apoorv",'../images')



# conn.execute('''CREATE TABLE subscription 
#           (subsID INTEGER PRIMARY KEY AUTOINCREMENT,
#           userID INT NOT NULL,
#           courseID INT NOT NULL,
#           location text NOT NULL);''')

# conn.execute("ALTER TABLE subscription drop column location")

def subscribe(userID, courseID):
    s="INSERT INTO subscription (userID, courseID) VALUES( '"+str(userID)+"', '"+str(courseID)+"' )"
    print(s)
    conn.execute(s)
    conn.commit()

def courses_applied(userID):
    s="select courseID from subscription where userID='"+str(userID)+"' "
    cursor=conn.execute(s)
    courses=[]
    for row in cursor:
        courses.append(row[0])
    res=[]
    for courseID in courses:
        s="select title, address from courses where courseID='"+str(courseID)+"' "
        cursor =conn.execute(s)
        for row in cursor:
            res.append([row[0], row[1]])
    return res

# cursor=courses_applied(1)
# for row in cursor:
#     print(row)





# conn.execute("delete from subscription")
# conn.commit()
# out=courses_applied(1)
# for row in out:
#     print(row)
# subscribe(1, 4)
# out=courses_applied(1)
# for row in out:
#     print(row)


# cursor=conn.execute("select * from jobs")
# for row in cursor:
#     print(row)

def job_category():
    s="select distinct category from jobs"
    cursor=conn.execute(s)
    res=[]
    for row in cursor:
        res.append(row[0])
    return res




#conn.execute("create table employer (emID INTEGER PRIMARY KEY AUTOINCREMENT, company_name TEXT NOT NULL, email TEXT, password TEXT);")

def add_employer(company, email, password):
    s="insert into employer(company_name, email, password) values('"+company+"', '"+email+"', '"+password+"' )"
    conn.execute(s)
    conn.commit()



# add_employer("gods eye", "ge@email.com", "abcd")

def verify_employer(email, password):
    s="select emID, company_name from employer where email='"+email+"' and password='"+password+"' "
    cursor=conn.execute(s)
    for row in cursor:
        return [row[0], row[1]]
    return [-1, "none"]


# print(verify_employer("ge@email.com", "abcd"))
