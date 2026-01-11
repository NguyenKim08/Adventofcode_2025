For the second day of Advent of code, 

We need to find the sum of all invalid ids and the invalid id are defined as such:
-some sequence of digits are repated twice : 11, 22, 446446 are all invalid

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

For the second 2 part 2, 

We need to find the sum of all the invalid ids and the invalid ids are defined as such:
-some sequence of digits are repeated at least twice : 11, 22, 1188511885, 999, 12121212 are all invalid

So for this, same as part 1. 
I started by spliting them by the commas (,) and the dash (-) the same way as before and convert the numbers into string.
Next step, I will explain the basic logic on how I do it:
So to find the sequence of digits where it is repeated, in part one I find the mid point and compare the first sequence to the second sequence after the midpoint, if they are identical then it's an invalid id.But the same method will not work the same on day 2 beacause part 1 is only counting when the numbers had sequence that reapeated twice, and exactly twice but for day 2 part 2, it has to be repeated AT LEAST twice meaning, it could be repated thrice, four times, etc 

The question is how will I find the correct sequence that is repeating?
I find no way than just keep on trying each combination of digits to find the correct sequence,
So there is another way to compare the repetitions, it's when you observe a number : 121212, you can see that 12 is repeated 3 time so we can use this condition to check if an id is invalid or not. First we find the sequence and we check if the number of repeats * the sequence is equal or not to the string(original number), then we add this invalid id to the counter and return the counter's value.
                                                                                                                                  
                                                                                                                                  
