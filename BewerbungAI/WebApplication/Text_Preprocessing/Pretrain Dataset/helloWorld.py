import os
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

print("Script Path:", script_path)

with open("./frontend/public/static/media/text.txt", "w") as file:
    file.write("Hello World!")
