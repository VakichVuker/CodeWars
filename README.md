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


## 4. Best place at concert
Files:
* place_at_concert.py

### Description
If you've ever been at rock/metal concerts, you know that they're great, but can be quite uncomfortable sometimes. In this kata, we're going to find the best place at the dance floor to be standing at!

dance_floor will be given as an array of strings, each containing:

ASCII letters (uppercase and lowercase), representing people.
Space characters (' '), representing empty space.
There will always be at least one string. All strings will have the same length (> 0).

Your task is to rank potential places to stand at and return the best one. If multiple places happen to share the same best score, you may return any of them.

In Python, return value is expected to be a tuple of two ints: (y, x), where y is index of the string and x is index of the character in that string.

### Factors for ranking
> #### The place must be empty
>> You're not a tough guy and you can't just push someone away and take their place. So, you're only considering empty space for yourself. Input will always contain at least one such place.

> #### Distance from stage
>> The closer you are to the stage, the better! So, the base score for a place equals length of the dance_floor minus the index of the string.  
>>> Example: if dance_floor contains 5 strings, the first (closest to the stage) gets score of 5 and the last gets score of 1.

> #### Height of the person in front of you
>> Even if you are close to the stage, a huge guy in front of you can spoil all the view! Because of that, you need to factor in his/her height.  
> In the input strings, people are represented as letters. Height of a person is encoded as a position of the letter in the alphabet. A has height of 1, B - 2, C - 3, and so on. You'll need to multiply the initial score by 0.99 ^ height (0.99 to the power of height). If there's nobody right in front of you, the score is left as is.

> #### Beer
>> Some of the fans are standing with a glass of beer in their hand. They are represented as uppercase letters (as opposed to lowercase letters without beer). You know that this beer always gets split around, so you want to avoid standing next to these people. For each beer holder next to you, you should multiply the score by 0.8.

> #### Moshpits
>> When you see a large free area that contains a 2x2 square of spaces, you know that it's not an accident. It's a moshpit! You don't like being kicked around, so you avoid moshpits at all costs and consider them only if there's no other free space available.  
>>> Note: moshpits can be of any shape, not necessarily square or rectangle. See example below.

### Example
dance_floor = ["gbvKq  JfiM I", "q jecl   fvoX", "L  Foa   ygKT"]
best_place(dance_floor) -> (1, 1)
dance_floor more visually:

#(stage here)  
"gbvKq  JfiM I"  
"q jecl   fvoX"  
"L  Foa   ygKT"  

#### Each ' ' explained:

(0,11) gets score of (3-0) * 0.8^2 = 1.92. Even though it's right in front of the stage, you're surrounded with 2 beer holders, which makes it not ideal.  
(1,1) gets score of (3-1) * 0.99^2 = 1.9602. This place is a bit further, but the person in front of you is very short, so you choose to spend the concert there.  
(0,5), (0,6), (1,6), (1,7), (1,8), (2,6), (2,7), (2,8) is a moshpit (looks more a wall of death in this case, haha). In this example, there are other places where you can stand in peace, so you don't even consider these, even though (0,5) has the best score in the entire club.  
(2,1) gets score of (3-2) * 0.8 = 0.8. There's nodoby in front of you, but you would stand even further away from the stage and carry a beer risk.  
(2,2) gets score of (3-2) * 0.99^10 * 0.8 = 0.7235. Same distance and risk, plus there's a person in front.  