import sys

if __name__ == "__main__":
    count = len(sys.argv)
    print("=== Command Quest ===")
    if count == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {count - 1}")
        i = 1
        while i < count:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {count}")
