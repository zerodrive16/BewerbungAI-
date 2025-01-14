def write_and_read_file():
    # Open the file in write mode to write content
    with open("./frontend/build/static/text.txt", "w") as file:
        file_result = "Hello World"
        file.write(file_result)
    return file_result


# Call the function
file_result = write_and_read_file()
print(file_result)
