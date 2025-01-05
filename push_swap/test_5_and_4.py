import itertools
import subprocess

# Define the range of numbers
numbers = [1, 2, 3, 4, 5]

# Generate permutations for lengths from 3 to 5
for length in range(3, 6):
    for perm in itertools.permutations(numbers, length):
        # Convert the tuple to a space-separated string
        perm_str = " ".join(map(str, perm))
        
        # Run ./push_swap and ./checker_linux
        try:
            push_swap = subprocess.run(
                ["./push_swap"] + list(map(str, perm)),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True,
            )
            checker = subprocess.run(
                ["./checker_linux"] + list(map(str, perm)),
                input=push_swap.stdout,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True,
            )

            # Count the number of lines in the output of ./push_swap
            lines_executed = len(push_swap.stdout.splitlines())

            # Check if result is KO or ERROR
            res = checker.stdout.strip()
            if res == "KO" or res == "ERROR":
                print(f"{res} for permutation: {perm_str}")

            # Print the total line count for the current permutation
             # for case of 5 numbers
            print(f"Permutation: {perm_str} -> Total lines executed: {lines_executed}")

        except subprocess.CalledProcessError as e:
            print(f"Error processing permutation {perm_str}: {e}")
