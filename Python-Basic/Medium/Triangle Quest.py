You are given a positive integer N. Print a numerical triangle of height N-1 like the one below:
1
22
333
4444
55555
......
Can you do it using only arithmetic operations, a single for loop and print statement?

Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.

Input Format
A single line containing integer, N.
Output Format
Print N-1 lines as explained above.

Sample Input

5
Sample Output

1
22
333
4444
Code:
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((pow(10,i)//9)*i)
