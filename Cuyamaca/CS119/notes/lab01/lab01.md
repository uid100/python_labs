# Ex.1 (multipy 2 numbers)

solution is fine. Please see my detailed feedback for more information

## pseudocode:

Be careful that your pseudocode does not look like python (or any other language).
Make sure your design is not a copy of your program code! (see the example.)

This should just be simple step-by-step instructions.
such as:
(input)
get 2 numbers from user

(process)
multiply the numbers

(output)
display the result

## program code:

- Be sure to use descriptive names for your program files.  
  "multiply.py" will multiply any two numbers for a user.

- When you declare your variables (not constants) set them to zero. Why 3? Why 5?

---

your input should only get the number of kilometers from the user.
the pseudocode is your program design. It should contain all of the information you need to give to the developer, including the conversion factor from the instructions: miles per km = 0.62
the output should be to display the result, in this case: Display miles

- Use a descriptive name for your project, such as KmToMiles. "multiply2" doesn't tell me what it does.

- Avoid using constants without labels.
  if you use the factor given:
  km_per_miles = 0.62,
  then
  miles = km \* miles_per_km

- Python's input() function returns a string from the user. In exercise 1, we used int() to convert that to an integer. in this case, float() would be better so the user can enter 5.3 and not get an error

# Ex.2

## pseudocode

remember that your pseudocode is the program design. It's usually used by the engineering team to design the sequence of processing that the the developer should follow. It contains all of the information that the developer will need to implement.

Avoid using constants without explanations.

so this is good...
num_miles = num_kilom \* 0.62

but this is better.
miles_per_kilometer = 0.62
miles = km \* miles_per_kilometer

---

## program code:

best practice to define the constants near the top of your code so that they can be maintained, never use a constant without explaining what it is.

"0.63" ... doesn't mean anything.

this is much clearer:

miles_per_km = 0.62
miles = km \* miles_per_km

recommended that you separate your display step from your processing step. This will make your code easier to maintain.

- Use descriptive names for your program files. What does Lab2PseudoCode2 do? Why not KmToMiles.py ?

- Avoid using constants without explanations.

so this is good...
miles = kilometers \* 0.62

but this is better.
miles_per_kilometer = 0.62
miles = km \* miles_per_kilometer

- when you asked the user for number of km to convert, better to use float() instead of int(). If I need to convert 10.4, I get an error. Also, even though you initialized "miles" (you called it "product", not sure why), you set it to an integer (0), because Python works a little different, when you reset it to km \* 0.62, it threw that variable away and made a new one that is a float. Other languages would have thrown en error here. Initialize to 0.0 if you need to use a variable as a floating point number.
