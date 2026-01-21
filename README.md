# start-to-python-pro-Journey
Starting my Python journey from scratch — beginning with the basics like 'Hello World' and advancing step-by-step through practical projects, exercises, and hands-on learning.

# Intro to Programming with Python

### Software

Software is a set of instructions to the hardware.

### Programming

Programming means writing the instructions to create a software.

### Code

The instructions that we write to create software is called Code.

### Syntax

Similar to Grammar rules in English, Hindi, each programming language has a unique set of rules. These rules are called the Syntax of a Programming Language.

## Why Python

Python is an easy to learn, powerful programming language. With Python, it is possible to create programs with minimal amount of code.

## Applications of Python

Python is a versatile language which has applications in almost every field

Artificial intelligence (AI)
Machine Learning (ML)
Big Data
Smart Devices/Internet of Things (IoT)
Cyber Security
Game Development
Backend Development, etc.

## Career Opportunities

Python developers have plenty of opportunities across the world

DevOps Engineer
Software Developer
Data Analyst
Data Scientist
Machine Learning (ML) Engineer
AI Scientist, etc.

# Variables and Data Types

### Variables

Variables are like containers for storing values.
Values in the variables can be changed.

### Values

Consider that variables are like containers for storing information.
In context of programming, this information is often referred to as value.

# Data Type

In programming languages, every value or data has an associated type to it known as data type.

### Some commonly used data types

String
Integer
Float
Boolean

This data type determines how the value or data can be used in the program. For example, mathematical operations can be done on Integer and Float types of data.

### String

A String is a stream of characters enclosed within quotes.
Stream of Characters

Capital Letters ( A – Z )
Small Letters ( a – z )
Digits ( 0 – 9 )
Special Characters (~ ! @ # $ % ^ . ?,)
Space

#### Some Examples

"Hello World!"
"some@example.com"
"1234"

### Integer

All whole numbers (positive, negative and zero) without any fractional part come under Integers.
Examples

...-3, -2, -1, 0, 1, 2, 3,...

### Float

Any number with a decimal point
24.3, 345.210, -321.86

### Boolean

In a general sense, anything that can take one of two possible values is considered a Boolean. Examples include the data that can take values like 

True or False
Yes or No
0 or 1
On or Off, etc.

As per the Python Syntax, True and False are considered as Boolean values.
Notice that both start with a capital letter.

## Sequence of Instructions

### Program
A program is a sequence of instructions given to a computer.

### Defining a Variable
A variable gets created when you assign a value to it for the first time.

Variable name enclosed in quotes will print variable rather than the value in it.
If you intend to print value, do not enclose the variable in quotes.

## Order of Instructions

Python executes the code line-by-line.

## Spacing in Python

Having spaces at the beginning of line causes errors.

## Expression

An expression is a valid combination of values, variables and operators.

#### Examples 
    a * b
    a + 2
    5 * 2 + 3 * 4

### BODMAS
The standard order of evaluating an expression

Brackets (B)
Orders (O)
Division (D)
Multiplication (M)
Addition (A)
Subtraction (S)

## Inputs and Outputs Basics
Working with Strings

### String Concatenation
Joining strings together is called string concatenation.

### Concatenation Errors
String Concatenation is possible only with strings.

### String Repetition
* operator is used for repeating strings any number of times as required.

### Length of String
len() returns the number of characters in a given string.

### Take Input From User
input() allows flexibility to take the input from the user.
input() reads a line of input as a string.

### String Indexing
We can access an individual character in a string using their positions (which start from 0).
These positions are also called as index.

### IndexError
Attempting to use an index that is too large will result in an error.

## Type Conversion

### String Slicing
Obtaining a part of a string is called string slicing.

### Slicing to End
If end index is not specified, slicing stops at the end of the string.

### Slicing from Start
If start index is not specified, slicing starts from the index 0.

### Checking Data Type
Check the datatype of the variable or value using type() 

## Type Conversion

Converting the value of one data type to another data type is called Type Conversion or Type Casting.

### We can convert

String to Integer
Integer to Float
Float to String and so on.

#### String to Integer
int() converts valid data of any type to integer

#### Integer to String
str() converts data of any type to a string.

int() -> Converts to integer data type
float() -> Converts to float data type
str() -> Converts to string data type
bool() -> Converts to boolean data type

## Relational Operators

Relational Operators are used to compare values.
Gives True or False as the result of a comparison.    

### These are different relational operators    

>	Is greater than
<	Is less than
==	Is equal to
<=	Is less than or equal to
>=	Is greater than or equal to
!=	Is not equal to

## Logical Operators

The logical operators are used to perform logical operations on Boolean values.
Gives True or False as the result.  

### Following are the logical operators  

and
or
not

### Logical AND Operator
Gives True if both the booleans are true else, it gives False

### Logical OR Operator
Gives True if any one of the booleans is true else, it gives False

### Logical NOT Operator
Gives the opposite value of the given boolean.

##### Logical AND Operator gives True if all the booleans are true.
##### Logical OR Operator gives True if any of the booleans are true.
##### Logical NOT Operator gives the opposite value

## Conditional Statements

### Block of Code
A sequence of instructions are called block of code.
Python executes code in a sequence.

### Condition
An expression that results in either True or False

##### Examples 

i. 2 < 3
ii. a == b
iii. True

### Conditional Statement
Conditional Statement allows you to execute a block of code only when a specific condition is True

##### if condition:

### Conditional Block
Block of code which executes only if a condition is True is called Conditional Block.

### Indentation
Space(s) in front of the conditional block is called indentation.
Indentation(spacing) is used to identify Conditional Block.
Standard practice is to use four spaces for indentation.

## If - Else Syntax
When If - Else conditional statement is used, Else block of code executes if the condition is False
if condition:
   block of code
else:
   block of code

## More Arithmetic Operators

### Modulus
To find the remainder, we use Modulus operator %
a % b

### Exponent
To calculate a power b, we use Exponent Operator **
a ** b  

### Square of a number
We can find the square of a number using the exponent operator by keeping the exponent as 2.

### Square root of a number
We can find the square root of a number using the exponent operator to calculate the square root of a number by keeping the exponent as 0.5
Any number to the power of 0.5 we give the square root value of that number.

## Nested Conditional Statements

### Nested Conditions
The conditional block inside another if/else conditional block is called as nested conditional block.
###### In the below example, 
Block 2 is nested conditional block and condition B is called nested conditional statement.


<img width="922" height="394" alt="image" src="https://github.com/user-attachments/assets/7f33f677-3e12-458a-8edc-05bb4d5d0f3b" />

### Nested Condition in Else Block
We can also write nested conditions in Else Statement.
###### In the below example Block 2 is a nested conditional block.


<img width="511" height="451" alt="image" src="https://github.com/user-attachments/assets/a2b74449-0aa5-44b6-b2ba-294cf142c830" />

### Elif Statement
Use the elif statement to have multiple conditional statements between if and else.
The elif statement is optional.


<img width="513" height="439" alt="image" src="https://github.com/user-attachments/assets/913e191c-207f-4004-8b66-b9fb17572bbb" />

### Multiple Elif Statements
We can add any number of elif statements after if conditional block.


<img width="510" height="444" alt="image" src="https://github.com/user-attachments/assets/ef7c8e77-075c-45dd-834d-84aa647d6f2b" />

### Execution of Elif Statement
Python will execute the elif block whose expression evaluates to true.
If multiple elif conditions are true, then only the first elif block which is True will be executed.


<img width="510" height="444" alt="image" src="https://github.com/user-attachments/assets/94fdf575-a85e-4e9a-ba80-898e647a5d51" />

## Loops

So far we have seen that Python executes code in a sequence and each block of code is executed once.
Loops allow us to execute a block of code several times.

### While Loop
Allows us to execute a block of code several times as long as the condition is True.

<img width="922" height="394" alt="image" src="https://github.com/user-attachments/assets/d2b2109f-8aba-482d-a430-aef9bc2c8caa" />

### Nested Condition in Else Block
We can also write nested conditions in Else Statement.
#### In the below example Block 2 is a nested conditional block.

<img width="511" height="451" alt="image" src="https://github.com/user-attachments/assets/4f7e361a-fba7-4ddf-b301-177adab0f5b6" />

### Elif Statement
Use the elif statement to have multiple conditional statements between if and else.
The elif statement is optional.

<img width="513" height="439" alt="image" src="https://github.com/user-attachments/assets/4eeabf3b-8b90-4af6-becd-51de5aac8bab" />

### Multiple Elif Statements
We can add any number of elif statements after if conditional block.

<img width="510" height="444" alt="image" src="https://github.com/user-attachments/assets/2706a4bf-2302-4823-9892-d8cc37c3e9a0" />

### Execution of Elif Statement
Python will execute the elif block whose expression evaluates to true.
If multiple elif conditions are true, then only the first elif block which is True will be executed.

<img width="510" height="444" alt="image" src="https://github.com/user-attachments/assets/fd6b5d16-e3f1-4df2-a83d-bbbee4d53dac" />

### Optional Else Statement
Else statement is not compulsory after if - elif statements.

<img width="491" height="357" alt="image" src="https://github.com/user-attachments/assets/91080ec7-a846-4af8-9802-8e71b35e49f5" />
