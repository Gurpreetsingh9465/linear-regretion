import numpy as py # let me import numpy
def compute_error_for_given_points(b, m, points):
    error = 0
    for i in range(len(points)):
        x = points[i, 0]
        y = points[i, 1]
        error += ( y - (m*x + b)) **2
    return error / float(len(points))

def step_gradient(b_current, m_current, points, learning_rate):
    print(compute_error_for_given_points(b_current, m_current, points))
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(int(N)):
        x = points[i][0]
        y = points[i][1]
        b_gradient += -(2/N)*(y - (m_current*x + b_current))
        m_gradient += -(2/N)*x*(y - (m_current*x + b_current))
    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)
    return [new_b, new_m]



def gradient_descent_runner(points, starting_b,starting_m, learning_rate, num_iteration):
    b = starting_b
    m = starting_m
    for i in range(num_iteration):
        [b, m] = step_gradient(b, m, points, learning_rate)
    return [b, m]


points = py.genfromtxt('data.csv', delimiter=',')
#hyperparameter how fast our machine learn
# if it is to high it will not converge
# if it is to low it will never converge


# y = mx + b
initial_b = 0
initial_m = 0
learning_rate = 0.0001

# no of iteration 1000 for small data

num_iteration = 1000
[b, m] = gradient_descent_runner(points, initial_b,initial_m,learning_rate, num_iteration)

ideal_b = b
ideal_m = m

print(ideal_b,ideal_m)

while 1:
    hour_you_study = float(input("No of hour you study"))
    print(ideal_m * hour_you_study + ideal_b)
    x = int(input("enter 0 to exit and 1 to continue"))
    if x == 0:
        exit(1)
