def calculate_minimum_prices(n, reviews):
    prices = [1] * n  # Initialize all prices to 1

    for i in range(1, n):
        if reviews[i] > reviews[i - 1]:
            prices[i] = prices[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if reviews[i] > reviews[i + 1]:
            prices[i] = max(prices[i], prices[i + 1] + 1)

    total_price = sum(prices)
    return total_price

try:
    # Read input from input.txt
    with open("input.txt", "r") as file:
        # Read all lines and split at "=" to extract reviews list
        input = file.read().strip().split('\n')

    # Initialize an empty list to store output results
    output_results = []
    i=1
    for input_str in input:
        # Split the string at "=" to separate variable name and list
        valid = input_str.split("=")
        if len(valid) != 2:
            raise ValueError("Invalid input format")

        # Extract and parse the list
        reviews = valid[1].strip()
        if not reviews.startswith("[") or not reviews.endswith("]"):
            raise ValueError("Invalid Reviews List")
        reviews_list = list(map(int, reviews[1:-1].split(',')))

        # Check if input data is empty
        if not reviews_list:
            raise ValueError("Input data is empty")
        result = calculate_minimum_prices(len(reviews_list),reviews_list)
        
        if result == -1:
            output_results.append(-1)
        else:
            output_results.append(chr(ord('@')+i)+')'+str(result))
            i=i+1

    # Write the results to output.txt
    with open("output.txt", "w") as file:
        for result in output_results:
            file.write(str(result) + '\n')

except FileNotFoundError:
    print("Error: The input file 'inputPS05.txt' was not found.")
except ValueError as ve:
    print("ValueError:", ve)
except Exception as e:
    print("An error occurred:", str(e))








