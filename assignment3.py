#Github Username: PhilipQuarshie


#Github Link: https://github.com/PhilipQuarshie/Data-Structures






import numpy as np


#Length of beam
L = 12


#Load intensity (w) in KN/m
w = 10




#Question (a)
#The Bending moment(M) and shear force(V) at the first end


x = 0


M = (w*(-6*x**2 + 6*L*x-L**2))/12


V = w*(L/2 - x)




print('(a.(i))' + 'The bending moment atx=0 is: ' + str(M) + ' and ' + 'the shear force atx=0 is: ' + str(V))




#The Bending moment(M) and shear force(V) at the first end
#x=L=12


X = L
m = (w*(-6*X**2 + 6*L*X-L**2))/12
v = w*(L/2 - X)


print()
print('(a.(ii))' + 'The bending moment atx=12 is: ' + str(m) + ' and ' + 'the shear force atx=12 is: ' + str(v))




#Question (b)
"""
When the bending moment is zero, the expression is x**2 - Lx + L**2/6 = 0


"""
#from the expression
a = 1


b = -L


c = L**2/6


#Using the Almighty formula the two roots are;


discriminant = b**2 - 4*a*c


root_1b = (-b + np.sqrt(discriminant))/2*a


root_2b = (-b - np.sqrt(discriminant))/2*a


print()


print('(b.) The points of contra-flexure are {0} and {1}'.format(root_1b,root_2b))#Question c
"""
When the shear force is zero, x = L/2
"""
x = L/2
print()
print('(c) The point at which V=0 is {}'.format(x))


#Question C


"""
When the shear force is zero, x = L/2
"""


x = L/2


print()
print('(c) The point at which V=0 is {}'.format(x))




#Question D


p = 0

q = L + s


x = np.arange(p,q,s)


M = (w*(-6*x**2 + 6*L*x-L**2))/12


print()
print('(d.) Using the initialized variable,the bending moment at each step in the array is {0}'.format(M))


#Question E
V = w*(L/2 - x)


print()
print('(e) The shear force for each step along the span is {}'.format(V))




#Question F
"""
Let the absolute value of the bending moment array be AM
Also let the minimum AM be m_AM
"""
AM = abs(M)
m_AM = min(AM)


"""
When the bending moment is m_AM, we get an expression x**2 - Lx + (L**2/6)+(2*m_AM)/w = 0
"""


#from the above expression

a = 1
b = -L
c = (L**2/6)+(2*m_AM)/w


#Using the Almighty formula the two roots are;


discriminant = b**2 - 4*a*c
root_1f = (-b + np.sqrt(discriminant))/2*a
root_2f = (-b - np.sqrt(discriminant))/2*a


print()
print('(f) The points along L at which the absolute values of the bending moment array is minimum are{0} and {1}'.format(root_1f,root_2f))


#Question G
"""
Let the relative errors be r_e
"""


r_e1 = ((root_1b - root_1f)/root_1b*100)
r_e2 = ((root_2f - root_2b)/root_2f*100)


print()
print('(g) The relative errors between estimated points of contra-flexure are {0}% and{1}%'.format(r_e1,r_e2))




#Question H
"""
Let the maximum bending moment be max_M and the minimum bending moment be min_M
"""

#for the maximum


max_M = max(M)
"""
When the bending moment is max_M, we get an expression x**2 - Lx + (L**2/6)+(2*max_M)/w = 0
"""


a = 1
b = -L
c = (L**2/6)+(2*max_M)/w


#Using the Almighty formula the two roots are;


discriminant = b**2 - 4*a*c
root_1 = (-b + np.sqrt(discriminant))/2*a
root_2 = (-b - np.sqrt(discriminant))/2*a
print()
print('(h(i)) The points at which the maximum bending moment occur are {0}
and{1}'.format(root_1,root_2))


#for the minimum


min_M = min(M)
"""
When the bending moment is min_M, we get an expression x**2 - Lx + (L**2//6)+(2*min_M)/w = 0
"""
a = 1
b = -L
c = (L**2//6)+(2*min_M)/w


#Using the Almighty formula the two roots are;


discriminant = b**2 - 4*a*c
root_1 = (-b - np.sqrt(discriminant))/2*a
root_2 = (-b + np.sqrt(discriminant))/2*a
print()
print('(h(ii)) The points at which the minimum bending moment occur are {0}
and{1}'.format(root_1,root_2))
