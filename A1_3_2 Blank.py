"""
A1_3_2 Keyes.py
Programmer:
"""

#Place Your Code Below

In []: import matplotlib.pyplot as plt
In []: a = randn(10000)
In []: plt.hist(a)
In []: plt.show()
In []: %logstart -ort studentNames_1_3_2.log
In []: # Jane Doe 1.3.2 IPython log
In []: 5 + 3
Out[]: 8
In []: 5 + 3.  # Note the decimal point!
Out[]: 8.0
In []: 7*2
In []: 7*2.
In []: # 5a. int*int returns an int \
  ...: # but int*float returns a float \
  ...: (Press enter here to end the continued input)
In []: 7/2
In []: 7/2.
In []: # 7b. int/int returns _______ but int/float returns _______
In []: a = 2
In []: # 8. Assignment
 
In []:(write code to assign value 16 to variable student_age)
In []: a
Out[]: 2

In []: a * 7 # multiplication
Out[]: 14

In []: 3 ** 2 # exponentiation
Out[]: 9
In []: abs(-7) # absolute value function
Out[]: 7
def add_tip(total, tip_percent):
    ''' Return the total amount of a meal including tip'''
    tip = tip_percent*total
    return total + tip
In []: a = add_tip(20, 0.15) 
In []: a
Out[]: 23.0
In []: add_tip(30, 0.15) 
Out[]: 34.5
In []: add_tip(30)
In []: # 17a. Hypotenuse test
In []: hyp(3,4)
Out[]: 5.0 
In []: # 17b. Mean test
In []: mean(3,4,7)
Out[]: 4.6666666666666667
In []: # 17c. Perimeter test
In []: perimeter(3,4)
Out[]: 14 
In []: %logstop 
     
'''
Conclusion questions

Read the introduction to this activity again. Describe something you would like to have automated by a program.

What are the native data types you learned about in this activity?

What are some differences between the command line of the interpretive IPython session and the code editor where you edit a file of code?

What do you think might be some of the advantages of putting code inside of a function definition?

'''
