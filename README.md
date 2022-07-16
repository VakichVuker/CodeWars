# CodeWars
My solutions from codewars.com on 5th kyu.

## 1. Is my friend cheating?
Files:
* cheating.py

### DESCRIPTION:

* A friend of mine takes the sequence of all numbers from 1 to n (where n > 0).
* Within that sequence, he chooses two numbers, a and b.
* He says that the product of a and b should be equal to the sum of all numbers in the sequence, excluding a and b.
* Given a number n, could you tell me the numbers he excluded from the sequence?
* The function takes the parameter: n (n is always strictly greater than 0) and returns an array or a string (depending on the language) of the form:

[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or or [{a, b}, ...]
with all (a, b) which are the possible removed numbers in the sequence 1 to n.

[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or ... will be sorted in increasing order of the "a".

It happens that there are several possible (a, b). The function returns an empty array (or an empty string) if no possible numbers are found which will prove that my friend has not told the truth! (Go: in this case return nil).

### Examples:
removNb(26) should return [(15, 21), (21, 15)]
or
removNb(26) should return { {15, 21}, {21, 15} }
or
removeNb(26) should return [[15, 21], [21, 15]]
or
removNb(26) should return [ {15, 21}, {21, 15} ]
or
removNb(26) should return "15 21, 21 15"
or

in C:
removNb(26) should return  {{15, 21}{21, 15}} tested by way of strings.
Function removNb should return a pointer to an allocated array of Pair pointers, each one also allocated. 
Note
See examples of returns for each language in "RUN SAMPLE TESTS"

## 2. Valid Parentheses
Files:
* valid_parenth

Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

### Examples
"()"               =>  true
")(()))"           =>  false
"("                =>  false
"(())((()())())"   =>  true

### Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).

## 3. int32 to IPv4
Files:
* int32_to_ipv4.py

### DESCRIPTION:
Take the following IPv4 address: 128.32.10.1

This address has 4 octets where each octet is a single byte (or 8 bits).

1st octet 128 has the binary representation: 10000000
2nd octet 32 has the binary representation: 00100000
3rd octet 10 has the binary representation: 00001010
4th octet 1 has the binary representation: 00000001
So 128.32.10.1 == 10000000.00100000.00001010.00000001

Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361

Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.

### Examples
2149583361 ==> "128.32.10.1"

32         ==> "0.0.0.32"

0          ==> "0.0.0.0"