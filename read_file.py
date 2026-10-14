
def read_from_file():
    filename = "sample.txt"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        print("----- File Contents -----")
        print(content)

    except FileNotFoundError:
        print(f"Error: '{filename}' was not found.")
        print("Please run write_file.py first.")

    except OSError as error:
        print(f"Error reading file: {error}")


if __name__ == "__main__":
    read_from_file()
