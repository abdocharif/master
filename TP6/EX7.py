import logging
# Configure logging
logging.basicConfig(
    filename='error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_error(message):
    logging.error(message)

def read_file(filename):
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        print(content)
    except FileNotFoundError as e:
        error_message = f"File '{filename}' not found."
        print(error_message)
        log_error(error_message)
    finally:
        if file:
            file.close()

# Example usage
if __name__ == "__main__":
    read_file("zip.txt")
