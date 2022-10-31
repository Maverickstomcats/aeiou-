def check_3digits(list1):
  three_digit_list = []
  for n in list1:
    if n in range (100,1000):
      three_digit_list.append(n)
    else:
      pass
  return three_digit_list
########################################################################################################################
# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.
def all_positives(list1):
    all_positives_list =[]
    for n in list1:
      if n in range(0,9999999):
        all_positives_list.append(n)
      else:
        pass
    return all_positives_list
# Don't call the function, you just need to define it.


########################################################################################################################
# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list (stored in the variable numbers) as long as they are greater than 0 and less than 1000, and returns the result of said sum.
def sum_less(list1):
  sum_lesslist = []
  for n in list1:
    if n in range(0,999):
      sum_lesslist.append(n)
    else:
      pass
  return sum_lesslist
  summary = sum(sum_lesslist)
  print(summary)
########################################################################################################################
# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.
def is_even(num):
    even = num % 2 == 0
    return even
def count_even(list):
  count_even_list = []
  
  
  