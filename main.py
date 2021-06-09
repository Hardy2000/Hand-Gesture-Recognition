'''
Submitted By:
-> Sauhardya Satabdi Pradhan (Betn1cs18062)

'''

import os
print("\"1\" Track Hand using Color Detection.")
print("\"2\" Detect Hand using Background Subtraction.")
val=int(input("Enter your choice (1/2/ ):"))
if (val==1):
    os.system('python Color_Detection.py')
elif(val==2):
    os.system('python Background_sub.py')
