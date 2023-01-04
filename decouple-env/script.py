from decouple import config

username = config('username', default='')
password = config('password', default='')
# we set default=’’ to avoid any errors in case the first argument isn’t in the .env file (if that’s the case, it’d initialize as an empty string ‘’)

print(username, password)