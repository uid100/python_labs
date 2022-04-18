#Variable Names:
When combining words together for variable names, there are a few well-known style patterns. These common style conventions are often language and context specific. The three most commonly used in programming are camel case, Pascal case, and snake case.

In C++, C#, and Java, the most common convention is called camel case so when words are strung together, you capitalize the first letter of each subsequent word. such as "milesPerGallon" and "totalFuelCost."

Pascal case is a particular variation of camel case which also capitalizes the first word "StudentSocialSecurityNumber". This is usually reserved for class names and public identifiers and is beyond the scope of this discussion. A simple way to remember this is that it we capitalize proper names and it was named for the famous mathematician Blaise Pascal.

The Python language is usually written using underscores to separate the words. "total_price" and "text_sent". This is known as snake case.
Best practice is to use the coding standards defined for the language and development environment.

For our purposes, any of these is fine, but be consistent with the one that you select.

---

Better to format the display with number of digits, rather than changing the value of the variable with the round() function.

Python provides several ways to do this, and as the language is evolving, this can get confusing. Recent changes are better aligning the language with other languages. Google "using f-strings in Python" for more information about how to do this. It's not the only way, but my favorite so far. It replaces the "string modulo" operator (%) that isn't as commonly used anymore.

---

#Constants:
(always!!) avoid using unnamed constants. Define them in one place near the beginning of your code and use them below.

tax_rate = .09 # local tax for Feb 2022
cost_per_text = .25

in this case, when these values change, they only need to be changed in one place and (again) it makes your code make a lot more sense and much easier to update later, when the cost or the tax_rate changes.

#Number Types:
keep in mind the meaning of each variable when declaring and using variables. number_of_text_messages should be an integer. You can't send 1/2 a message, so making it a float (decimal) number doesn't really make sense. It uses more memory (less efficient) and it can lead to errors in the application.

#Sequence and Logic:
adding some comments ( #input #process #output ... ) and blank lines(!) won't change the code and are not necessary, but it will make the code easier to read and easier to update later.

Your application asked me how many texts, and then it printed it out as a decimal. That was unexpected and could be confusing. Be sure to delete the messages you included while you were testing.

multiple print statements print on multiple lines (unless you deliberately suppress this. we'll explain how later)

#separation of concerns
keep your calculations separate from your print statements will make the code easier to read. It's not wrong, but could be much clearer. This code is correct, but a little hard to follow.

Ok, but (always!!) avoid using unnamed constants. define them in one place near the start of your code and use them below. Things like tax_rates and item_cost have a way of changing frequently. This would be very difficult to maintain if you had to come back later and figure out what it means. Made even more difficult when you use one of these "random" constants in more than one place. What if you changed one and didn't know that one of your developers used a constant someplace else in the code.

Too much on your calculation line. This is not self-documenting code. Hard to read later.

cost_per_text_message = 0.25
tax_rate = 0.09

cost*text_messages = num_text * cost*per_text_message
tax = cost_text_messages * tax_rate
amount_due = cost_text_messages + tax

Good use of Python "f-strings"! I'm glad the language finally adopted these to keep up with other languages. You've obviously done some other coding in the past. Good job.

This is your design document. It should be descriptive enough for the programmer to implement the solution.

what is a manual text variable?

what does "cost" mean? what is the tax rate and what equation should I use?

hint: it's best to keep the steps of the equation separate.

What do you mean by the "product of process?"

Spell out the values and all the steps of the process:

cost_per_text_message = 0.25
tax_rate = .09

monthly_charge = number_of_text_messages * cost*per_text_message
tax = monthly_charge \* tax_rate
amount_due = monthly_charge + tax

the total is " could be more descriptive... how about this output instead?

Summary of charges:
131 text messages
$32.75 total charges
$2.95 taxes and fees
$25.70 total amount due
