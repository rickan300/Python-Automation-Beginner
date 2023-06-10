import argparse

parser = argparse.ArgumentParser(description="add info into list")

parser.add_argument("-add", nargs='+', type=str)
parser.add_argument("-remove", nargs='+', type=str)
parser.add_argument("-list", type=str)

args = parser.parse_args()

# Add to file
if args.add:
    grocery_list = open('groceries.txt', "a")
    for item in args.add:
        grocery_list.write("\n")
        grocery_list.write(item)
    grocery_list.close()
    print(f"{args.add} was added to the list!")

# Remove from file
if args.remove:
    with open('groceries.txt', 'r') as grocery_list:
        lines = grocery_list.readlines()

    with open('groceries.txt', 'w') as grocery_list:
        for line in lines:
            if not any(remove_item in line for remove_item in args.remove):
                grocery_list.write(line)
        print(f"{args.remove} was removed to the list!")

# show the list
if args.list:
    f = open('groceries.txt', 'r')
    read_list = f.read()
    print(read_list)
