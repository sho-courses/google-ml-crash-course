import numpy as np 

# https://numpy.org/doc/stable/reference/generated/numpy.array.html
one_dimensional_array = np.array([1.2, 2.4, 3.5, 4.7, 6.1, 7.2, 8.3, 9.5])
print(one_dimensional_array)

two_dimensional_array = np.array([[6, 5], [11, 7], [4, 8]])
print(two_dimensional_array)

# https://numpy.org/doc/stable/reference/generated/numpy.array.html
print(np.zeros((3,2), np.int8))

# https://numpy.org/doc/stable/reference/generated/numpy.ones.html
print(np.ones(3))

sequence_of_integers = np.arange(5, 12)
print(sequence_of_integers)

# https://numpy.org/doc/stable/reference/random/index.html?highlight=random#module-numpy.random
random_integers_between_50_and_100 = np.random.randint(low=50, high=101, size=(6))
print(random_integers_between_50_and_100)
random_integers_between_50_and_100_3_2_matrix = np.random.randint(low=50, high=101, size=(3,2))
print(random_integers_between_50_and_100_3_2_matrix)

random_floats_between_0_and_1 = np.random.random([6])
print(random_floats_between_0_and_1) 
random_floats_between_0_and_1_3_2_matrix = np.random.random((3,2))
print(random_floats_between_0_and_1_3_2_matrix) 

random_floats_between_2_and_3 = random_floats_between_0_and_1 + 2.0
print(random_floats_between_2_and_3)

random_integers_between_150_and_300 = random_integers_between_50_and_100 * 3
print(random_integers_between_150_and_300)

#@title Double-click to see a possible solution to Task 1.
feature = np.arange(6, 21)
print(feature)
label = (feature * 3) + 4
print(label)

#@title Double-click to see a possible solution to Task 2.
noise = (np.random.random([15]) * 4) - 2
print(noise)
label = label + noise 
print(label)