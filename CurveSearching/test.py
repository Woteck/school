import matplotlib.pyplot as plt
import numpy as np

# set of multiple points
# P = (x, y)
pA = (-2, -6)
pB = (0, 5)
pC = (10, -3)

# here we have 3 points called A, B, and C.
# y = ax^2 + bx + c
# thus, we can write the system of equations :
# {a * -11^2 + b * -11 + c = 4         {121a - 11b + c = 4
# {a *   3^2 + b *   3 + c = 5    <=>  {  9a +  3b + c = 5
# {a *   7^2 + b *   7 + c = 10        { 49a +  7b + c= 10

# search for X in A*X = B <=> X = A^(-1)*B
# we can express this system of equation into a equation of matrix such as AX = B, so :
#     | 121  -11    1 |        | a |        |  4 |
# A = |   9    3    1 |  ; X = | b |  ; B = |  5 |
#     |  49    7    1 |        | c |        | 10 |
A = np.array([
    [pA[0]**2, pA[0],  1],
    [pB[0]**2, pB[0],  1],
    [pC[0]**2, pC[0],  1]
])

B = np.array([
    [pA[1]],
    [pB[1]],
    [pC[1]]
])

# Then we will need to calculate A^(-1) :
A_inv = np.linalg.inv(A)

# And resolve the equation by doing A^(-1)*B :
X = np.matrix.dot(A_inv, B)

# The equation according to the curve is :
a = float(X[0])
b = float(X[1])
c = float(X[2])
print(f'y = {a}x² + {b}x + {c}')

x = np.linspace(-5,10,100)
y = a*x**2 + b*x + c

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x, y, 'y', label=f'y = {a}x² + {b}x + {c}')
plt.legend(loc='upper left')

# plot A, B, and C points.
plt.scatter(pA[0], pA[1])
plt.scatter(pB[0], pB[1])
plt.scatter(pC[0], pC[1])

# show the plot
plt.show()