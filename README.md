# greedy_algorithm

**Book Exhibition Pricing using Greedy Algorithm**

This repository hosts an efficient solution to a pricing problem faced by book exhibitions, formulated around a unique challenge—assigning price values to books based on their reviews, ensuring that more highly-reviewed books receive a higher price while maintaining the total price at a minimum.

**Problem Statement**

In a book exhibition, 'n' books are displayed, each with an associated number of good review comments. The task is to assign a price to each book such that:

Every book has a price, starting at 1.

Books with higher reviews have a higher price than their adjacent counterparts.

The total price for all books is the minimum sum possible given the above constraints.

**Approach**
A greedy algorithm is applied to ensure the optimal assignment of prices. The process involves a two-pass strategy:

From left to right, increasing the price of the current book if its review count is higher than the previous book's.

From right to left, ensuring that each book's price reflects its review count relative to its neighbors.

The algorithm promises a linear time and space complexity of O(n), making it an efficient solution even for a large number of books.

**Implementation Details**

The program reads input from input.txt, which contains the number of books and their respective reviews.

Prices are initialized and calculated using a custom calculate_minimum_prices function.

The total minimum price is computed and written to output.txt.

**Sample Inputs & Outputs**
**Input:** reviews = [2, 1, 3, 2 ,4 ,1]
**Output:** 9
**Input:** reviews = [1,0,2]
**Output:** 5
**Input:** reviews = [1,2,2]
**Output:** 4

**Exception Handling**

Robust exception handling is included to address file read/write issues, validate input formats, and handle empty data scenarios.

**Alternate Considerations**

The document also mentions an alternative Dynamic Programming approach, noting the potential for further optimization in scenarios with varying requirements.

This project illustrates a practical application of algorithmic problem-solving, perfect for understanding greedy algorithms and their implementation in a real-world context.

