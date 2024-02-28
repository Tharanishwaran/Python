# Here's another Python question for you:

# Write a Python function that takes a list of integers as input and returns a new
# list containing only the even numbers from the input list. 
# The order of the even numbers in the output list should be the same as their order in 
# the input list. If there are no even numbers in the input list, the function should return 
# an empty list.

# For example, given the input [1, 2, 3, 4, 5, 6], the function should return [2, 4, 6].


def even(num_l):
    i=0
    nl = len(num_l)
    evenlist = []
    
    if(num_l == []):
        
        print("empty list")
    
    else:
        while(i < nl):
           
           if(num_l[i] %2 == 0):
              
              evenlist.append(num_l[i])
           i=i+1
            
        print(evenlist)


new = [1,2,3,4,5,6,8]

even(new)