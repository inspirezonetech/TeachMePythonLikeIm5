# ------------------------------------------------------------------------------------
# Tutorial: pow() built-in function in Python
# ------------------------------------------------------------------------------------

# Code here explaining concept with comments to guide


#Return base to the power exp; if mod is present, return base to the power exp, modulo mod (computed more efficiently than pow(base, exp) % mod). 
#The two-argument form pow(base, exp) is equivalent to using the power operator: base**exp.

# Syntax:

a = 5

b = 3

a_power_b = pow(a, b) # should return 5^3 which is 125

print(apowerb) # 125

bpowera = pow(b, a) # should return 3^5 which is 243

print(bpowera) # 243


# ------------------------------------------------------------------------------------
# Challenge: Use pow() in a function to print every number the power of two upto that number x.
# E.g. x = 5, 
# It should output 1,4,9,16,25
# ------------------------------------------------------------------------------------
