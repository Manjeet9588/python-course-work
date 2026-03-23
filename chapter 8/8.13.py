'''Start with a copy of user_profile.py from page 153. Build
a profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you.'''


from user_profile import build_profile

info = build_profile('manjeet','saini',city='narnaul',age=20,gender='male')
print(info)