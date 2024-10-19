import argparse

class Jana:
    @staticmethod
    def greet(name):
        print(f"Hi {name}, this is Jana. Nice to meet you!")

    @staticmethod
    def mathumitha():
        print("Hi, this is Mathumitha")
        print("Press 1")
        
        while True:
            user_input = input().strip()
            if user_input == '1':
                print("This Is The Message From MathuMitha...")
                # Print heart shape here
                for row in range(6):
                    print(" " * 7, end="")
                    for col in range(7):
                        if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
                            print("*", end=" ")
                        else:
                            print(" ", end=" ")
                    print()
                print('143>   I Love You ❤️   <143')
                break
            else:
                print('😡 Just Press 1')

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

if __name__ == "__main__":
    main()