
def write_to_file():
    filename = "sample.txt"

    content = (
        "Welcome to the Python and Bash DevOps Assignment.\n"
        "Task 3: Writing data to a text file.\n"
        "Python makes file handling simple and efficient.\n"
    )

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"Content written successfully to '{filename}'.")

    except OSError as error:
        print(f"Error writing to file: {error}")


if __name__ == "__main__":
    write_to_file()
