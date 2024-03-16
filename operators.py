#  Python also has some operators, and these are given below -

# Arithmetic operators
# Comparison operators
# Assignment Operators
# Logical Operators
# Bitwise Operators
# Membership Operators
# Identity Operators
# Arithmetic Operators

# Arithmetic operators used between two operands for a particular operation. There are many arithmetic operators. It includes the exponent (**) operator as well as the + (addition), - (subtraction), * (multiplication), / (divide), % (reminder), and // (floor division) operators.

#Comparison operator
# Comparison operators mainly use for comparison purposes. Comparison operators compare the values of the two operands and return a true or false Boolean value in accordance. The example of comparison operators are ==, !=, <=, >=, >, <. In the below table, we explain the works of the operators.
a = 32      # Initialize the value of a  
b = 6       # Initialize the value of b  
print('Two numbers are equal or not:',a==b)  
print('Two numbers are not equal or not:',a!=b)  
print('a is less than or equal to b:',a<=b)  
print('a is greater than or equal to b:',a>=b)  
print('a is greater b:',a>b)  
print('a is less than b:',a<b)  

# Now we give code examples of Assignment operators in Python. The code is given below -

a = 32         # Initialize the value of a  
b = 6          # Initialize the value of b  
print('a=b:', a==b)  
print('a+=b:', a+b)  
print('a-=b:', a-b)  
print('a*=b:', a*b)  
print('a%=b:', a%b)  
print('a**=b:', a**b)  
print('a//=b:', a//b)  

# Bitwise Operators
# The two operands' values are processed bit by bit by the bitwise operators. The examples of Bitwise operators are bitwise OR (|), bitwise AND (&), bitwise XOR (^), negation (~), Left shift (<<), and Right shift (>>). Consider the case below.

Now we give code examples of Bitwise operators in Python. The code is given below -

a = 5          # initialize the value of a  
b = 6          # initialize the value of b  
print('a&b:', a&b)  
print('a|b:', a|b)  
print('a^b:', a^b)  
print('~a:', ~a)  
print('a<<b:', a<<b)  
print('a>>b:', a>>b)  


Logical Operators
The assessment of expressions to make decisions typically uses logical operators. The examples of logical operators are and, or, and not. In the case of logical AND, if the first one is 0, it does not depend upon the second one. In the case of logical OR, if the first one is 1, it does not depend on the second one. Python supports the following logical operators. In the below table, we explain the works of the logical operators.

Operator	Description
and	The condition will also be true if the expression is true. If the two expressions a and b are the same, then a and b must both be true.
or	The condition will be true if one of the phrases is true. If a and b are the two expressions, then an or b must be true if and is true and b is false.
not	If an expression a is true, then not (a) will be false and vice versa.
Program Code:

Now we give code examples of arithmetic operators in Python. The code is given below -

a = 5          # initialize the value of a          
print(Is this statement true?:',a > 3 and a < 5)  
print('Any one statement is true?:',a > 3 or a < 5)  
print('Each statement is true then return False and vice-versa:',(not(a > 3 and a < 5)))  