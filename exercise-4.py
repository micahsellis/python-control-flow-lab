# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print('Enter the lengths of three sides of a triangle: ')
len1 = int(input("a: "))
len2 = int(input("b: "))
len3 = int(input("c: "))

if len1 == len2 and len2 == len3:
    print(f"A triangle with sides of {len1}, {len2}, & {len3} is an equalateral triangle.")
elif len1 != len2 and len2 != len3 and len3 != len1:
    print(f"A triangle with sides of {len1}, {len2}, & {len3} is a scalene triangle.")
elif len1 == len2 or len1 == len3 or len2 == len3:
    print(f"A triangle with sides of {len1}, {len2}, & {len3} is an isosceles triangle.")
