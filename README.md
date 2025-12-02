Hello, my name is Nguyen Kim Ngan and this year I will be attempting to do Advent of code :'D
Whether or not I can do it, it'll be just a fun challenge for me :3 (even though I'm already late but whatever, we can just ignore that part for now)
But, first... Merry Christmas to you all !!
(Big note : I'm doing this as I'm learning, so if it's messy I've tried my best)

Day 1: We need to find a password that's hidden in a file.txt and here are some basic rules: 

Part 1: -in the file.txt there will be letters in the beginining which follows with a number right after (ex : L34), ranging from 0-99 

-We need to see if it's L or R, to determine where we would go : L is down and R is up so if we start at 7 and is L3 we go down to 4

-if we start at 0 and it's L1 we go back to 99 and if we start at 99 and it's R1 we go to 99

-and the password is how many times the number 0 appeared during calculations, so we need a counter :'D

I start by telling Python to read the file.txt, then I use strip() to clean them to manipulate easier (Unwanted spaces, and all that) and set up our position as 50, x = 50 
Then using index, I identfy the first index [0] of the string is an "R" or an "L" : if an L, I return x = 50 - number in the string and if it's an R, I return x = 50 + number. 

But there's one more problem : 

I forgot the loop rule as in L1 from 0 to 99 and R1 from 99 to 0, so I use modulo 100 to loop them (we need to find the actual position here as in (whatever value we have over 99, actual value - 99 = position we need to be so the value we search for, and using modulo - a function built in python, send us back the rest which is the value we search for (ex : L68 with current position is 50, send us back with -18 for position so we go left 18 steps and land on 82 for value) Then whatever it reaches 0 I add 1 to the counter and return the final count.

Part 2:

Same rules, we now need to counter each time we pass by 0 which also needs a separate counter and sum of two counters gives us the password. 
So if I use sum(the current position + steps) and if sum > 99 alors counter + 1 et inverse si sum < 0 alors counter = 0
