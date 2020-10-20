#Say you have an array for which the ith element is the price of a given stock on day i.
#If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#Note that you cannot sell a stock before you buy one.
#brute force
#first we will check the maximum different in the array by lopping which will take O(n^2) tiem complexity 
#another approach 
# we can iterate through the array and find the min and the difference as max through the single iteration so time complexity becomes O(n)
