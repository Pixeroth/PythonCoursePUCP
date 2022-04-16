"""

Argument specifiers

%c	  character
%s	  string (conversion any object via str() prior to formatting)
%d	  signed decimal integer
%u	  unsigned decimal integer
%e	  exponential notation (with lowercase 'e')
%E	  exponential notation (with UPPERcase 'E')
%f	  floating point real number
%g	  the shorter of %f and %e
%G	  the shorter of %f and %E

Examples:
- z is some specifier: c, s, d, u,...
- x, y are integer numbers 

%xz   format z right-adjusted in a field of width x
%-xz  format z left-adjusted in a field of width x

%xs   String of characters, total width x (optional).
%xd   Signed decimal integer, total width x (optional).
%xf   Print a float with x decimal places. 

%x.yf Floating Point value, x wide with y decimal places. Note 
      that the output will contain more than x characters if 
	  necessary to show y decimal places plus the decimal point.
%x.ye Scientific notation, x wide with y decimal places.
%x.yg General notation: switches between floating point and
      scientific as appropriate.
"""

#%%
# String Formatting - Method 1
# Using the format string operator %

# Example 1
name = "cesar"
FinalExamScore = 19.43289
FinalGrade = 235

longString =  "Student %s scored %0.3f on the final exam, \
for a grade of %d." % (name, FinalExamScore, FinalGrade )
    
print(longString)

#%%
# Example 2
from math import pi, e
sum = pi + e

print ("Decimal to int: %d" % pi)
print ("Floating Point, two decimal places: %0.2f " % pi)
print ("Scientific, two D.P, total width 10: %5.2e" % pi)
print ("The sum of %15.13f and %15.13f is %15.13f." % (pi, e, sum))


#%%
# String Formatting - Method 2
# Using the format() method of a string
t = 5.
g = 9.81
v0 = 0.6
y = v0*t - 0.5*g*t**2
u_v = 'm/s'


#%%
print('''\nAt t={} s, a ball with initial velocity v0={} m/s
is located at the height {} m.'''.format(t, v0, y))


#%%
print('''\nAt t={time} s, a ball with initial velocity v0={speed} m/s
is located at the height {height} m.'''.format(time=t, speed=v0, height=y))


#%%
print('''\nAt t={time:f} s, a ball with initial velocity v0={speed:.3E} m/s
is located at the height {height:.2f} m.'''.format(time=t, speed=v0, height=y))
 

#%%
print("""\nAt t={time:f} s, a ball with initial velocity v0={speed:.3E} in {unit}
is located at the height {height:.2f} m.""".format(speed=v0, height=y, time=t, 
unit=u_v))


#%%
'''
Appendix A: escape sequences (use with strings)

\       Break a line into multiple lines while ensuring the continuation of the line
\\	    Insert a Backslash character in the string
\’	    Inserts a Single quote character in the string
\”	    Inserts a Double Quote character in the string
\n	    Insert a new line in the string
\t	    Insert a Tab in the string
\r	    Insert a Carriage return in the string
\b	    Insert a backspace in the string
\u	    Insert a Unicode character in the string
\000	Insert a character in the string based on its octal value
\xhh	Insert a character in the string based on its hex value   

'''

#%%
'''
Other supported symbols
*	        argument specifies width or precision
-	        left justification
+	        display the sign
<sp>	    leave a blank space before a positive number
#	        add the octal leading zero ( '0' ) or hexadecimal leading '0x' or '0X', 
                depending on whether 'x' or 'X' were used.
0	        pad from left with zeros (instead of spaces)
%	        '%%' leaves you with a single literal '%'
(var)	    mapping variable (dictionary arguments)
m.n.	    m is the minimum total width and n is the number of digits to display 
                after the decimal point (if appl.)
'''

#%%
'''
Appendix B: References

ASCII Characters
https://en.wikipedia.org/wiki/ASCII

Python doc
https://docs.python.org/3/library/string.html#formatspec

'''







