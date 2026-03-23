'''Start with your work from Exercise 9-8 (page 178). Store the classes User, 
Privileges, and Admin in one module. Create a separate file, make an Admin 
instance, and call show_privileges() to show that everything is working correctly.'''

from admin import Admin

new_admin = Admin("Manjeet","Saini", 20 , "Narnaul")
new_admin.privileges.show_privileges()
