For the second day of Advent of code, 

We need to find the sum of all invalid ids and the invalid id are defined as such:
-some sequence of digits are repated at least twice : 11, 22, 446446 are all invalid

So for this, I want to start by spliting them into string separated by , (commas) so "10-15, 17-30" became "10-15", "17-30", this way it will be easier to manipulate them one by one. 
After spliting them, i will further on splitting by - (dash) to have the start of by range and end of my range in order to use range() built in function in python. 
In order to use range(), we need 2 integers and not string so by using int() to convert these strings into interger i can later on use range()
And then how do i identify my sequence of digits you may ask, well: 
-as you might have notice in the advent of code exemples : 446446 they are split by half so by using len i can find the midpoint (here it's 4) so my first sequence ended at 4th poisiton and started at 4th position
but how do i do that if i already converted them into integers ? 
-i can just convert them into strings again, for i in range(start, end + 1) : s = str(i)
And so i treat them case by case: 
-if len(s) % 2 == 0, len(s) // 2 is the midpoint and so first_seq=[:midpoint] and second_seq=[midpoint:]
-if len(s) % 2 != then i just skip because whether 98 vs 8 or 9 vs 88, it doesnt lined up none of these sequences are repeated so I just skipped over this case and return nothing,
but minor thing to look for here is, in one of the advent of code exemples : 999 is invalid so whenever we have a large numbers with the same digit then it's invalid. So for this, i added one more condition : if the string is the same when 
  the first digit is multiplied by the len(s) : so 999 is the same as 9 9 9 (3 times)
                                                                                                                                  
Finally, i just added all of these invalid ids into a total : som = 0
                                                                                                                                  
                                                                                                                                  
