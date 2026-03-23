''' Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.'''

from admin import Admin

admin_user = Admin("Priyanshu","sharma",21, "Narnaul")
admin_user.privileges.show_privileges()


