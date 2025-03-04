#in a real world situation I'd have added this file to the .gitignore
DB_PASSWORD = "wannasucceed"
DB_USER = "interviewee"
DB_HOST = "host.docker.internal"  # switch to localhost if you are not using the dev container
DB_NAME = "awesomeinc"
DB_PORT = 5432 
with open("tables.txt", "r") as file:
    string_tables = file.readline()
ALLOWED_TABLES = [items.strip() for items in string_tables.split(',')]