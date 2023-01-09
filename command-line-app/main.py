import sys

# python main.py <func_1>
# pip install click-shell

from click_shell import shell


@shell(prompt="genifer shell > ", intro="""Welcome to genifer-shell! 
Please enter a command down below. If you want to seel the list of all available commands, type, 'help'. """)
def genifer_shell():
    pass


@genifer_shell.command()      # now an annotation
def help():
    print("""Here is the list of all commands:
    help: See this list
    hello-world: Prints a message
    add: Add two integers
    create-file: Create new file and write into it
    exit: Exit shell
    """)


@genifer_shell.command()
def hello_world():   # this will be translated to hello-world
    print("Hello World")


@genifer_shell.command()
def add():
    num_1 = float(input("Enter first number: "))
    num_2 = float(input("Enter second number: "))
    print(num_1 + num_2)


@genifer_shell.command()
def create_file():
    filename = input("Enter filename: ")
    message = input("Type the message: ")
    with open(filename, 'w') as file:
        file.write(message)
    print(f"Successfully created file '{filename}'!")


@genifer_shell.command()
def exit():
    sys.exit('Exited')


if __name__ == '__main__':
    genifer_shell()
