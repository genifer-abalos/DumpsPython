'''Task

Ragyu is a shoe shop owner. His shop has N number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay x_i amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  earned.

Input Format
The first line contains , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.

Sample input:
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Sample output:
200

Explanation
Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.
Total sales = 200
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter


if __name__ == '__main__':
    num_shoes = int(input())
    shoe_sizes = list(map(str, input().split(" ")))
    list_shoe_sizes = set(shoe_sizes)
    availability_counter = Counter(shoe_sizes)
    num_customers = int(input())
    there_input = True
    shoe_sizes_and_prices = []
    while (there_input):
        try:
            shoe_size_and_price = list(map(str, input().split(" ")))
            shoe_size = shoe_size_and_price[0]
            if shoe_size in shoe_sizes:
                shoe_sizes_and_prices.append(shoe_size_and_price)
            else:
                pass
        except Exception as e:
            there_input = False

    # print(num_shoes, shoe_sizes, num_customers)
    # print(shoe_sizes_and_prices)
    total_sales = 0
    # print(availability_counter)
    for data in shoe_sizes_and_prices:
        # print(data)
        desired_shoe = list(data[0])
        desired_shoe_size = "".join(desired_shoe)
        desired_shoe_size_arr = [desired_shoe_size]
        # print(desired_shoe_size)
        if int(availability_counter[desired_shoe_size]) > 0:
            total_sales += int(data[1])
            availability_counter.subtract(desired_shoe_size_arr)

        # print(availability_counter)
        # print(total_sales)
    print(total_sales)



