# Employee Task Management

### Video Demo : <https://youtu.be/DYozZxPNGg4>

### Description : The Employee Task Management of my project are described as below.

### Employee :

In the Employee section, there is a login page for already existing employees and also a
register page for new employees. New employees can register by filling the fields: their email-id , name , and password . And after registering the current page will be redirected to the login page and employee can log in by filling the fields: their email-id , and password . After login the employees can see their tasks assigned to them.

### Manager :

In the Manager section, there is a login page for the manager. manager can log in by filling their password and then confirm their password. After login manager can give task to the employees by filling the fields: Task , Employee name , and Deadline.

### Manager Privilages :

In the Navbar there is a option "Task Assigned" on clicking that the manager can see the status about the task.

### Employee Privilages :

After login employees can see their tasks table. And also their is a checkbox, if the employee has done their task he can click the checkbox named as 'completed' and after clicking submit button the information about completion the task will sent to the manager. And manager can see the details.

### Database Explained :
To store data sqlite database was used which consisted of table :

### employee :
The employee table stored the 'email_id', 'name', 'password'.
when new employee registers his details stores in this database.

### task :
The task table stored the 'task_assigned','assigned_at','deadline','employee_name','completed_at','id','completed'.
When the manager give tasks to the employee and filled the details :'task','employee_name','deadline'. This data is stored in this database. Along with the current timestamp of assigning task named as 'assigned_at'.

And in the employee field When the employee will log in , they can show the table task assigned to them . and if they click on the 'complete' checkbox after completing their task.and submitting that information.

Manager can see the status of that task and also the current timestamp of submitting that task.

### Technologies Used :

 * Python
 * Flask
 * HTML
 * CSS
 * Bootstrap


 ### How to Run :

 * Download the Source Code
 * Locate app.py
 * Run flask run
 *(optional) Run phpliteadmin data.db to check the database and see the tables


 ### Documentation :

 * Flask - <https://flask.palletsprojects.com/en/2.2.x/>
 * Python - <https://docs.python.org/3/>
 * Sqlite3 - <https://www.sqlite.org/docs.html>
 * Bootstrap - <https://getbootstrap.com/docs/5.0/getting-started/introduction/>


 ### About CS50 :

CS50 is a openware course from Havard University and taught by David J. Malan

Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, and software engineering. Languages include C, Python, and SQL plus students’ choice of: HTML, CSS, and JavaScript (for web development).

Thank you for all CS50.