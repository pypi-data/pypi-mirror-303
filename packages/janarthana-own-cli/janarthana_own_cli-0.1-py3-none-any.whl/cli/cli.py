
#   <------------PracticedBY:"JANARTHANA" ------------> 

import argparse

# Define the Jana class with different methods
class Jana:
    @staticmethod
    def greet(name):
        print("")
        print(f"Hi {name}, this is Jana. Nice to meet you!")
        print("")

    @staticmethod
    def mathumitha():
        print('')
        print("Hi, this is Mathumitha")
        print('')
        print("Press 1")
        print("")
        
        # Start reading input from the user
        while True:
            user_input = input().strip()
            if user_input == '1':
                print(" ")
                print('This Is The Message From MathuMitha...')
                print(" ")
                # Print heart shape with 8 spaces before it
                for row in range(6):
                    print(" " * 7, end="")  # Add 8 spaces before each row
                    for col in range(7):
                        if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
                            print("*", end=" ")
                        else:
                            print(" ", end=" ")
                    print()
                print(" ")
                print('143>   I Love You ❤️   <143')
                print(" ")
                break
            else:
                print(" ")
                print('😡 Just Press 1')
                print(" ")

# Main function to handle CLI commands
def main():
    parser = argparse.ArgumentParser(description="CLI to call methods from the Jana class")
    parser.add_argument('-v', '--version', action='version', version='1.0.1')

    subparsers = parser.add_subparsers(dest='command')

    greet_parser = subparsers.add_parser('greet', help='Print a greeting message')
    greet_parser.add_argument('name', type=str, help='Name to greet')

    subparsers.add_parser('mathu', help='A Message From MathuMitha...')

    args = parser.parse_args()

    if args.command == 'greet':
        Jana.greet(args.name)
    elif args.command == 'mathu':
        Jana.mathumitha()
    else:
        parser.print_help()