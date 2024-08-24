# Create a result array by adding the following two NumPy arrays. Next, modify the result array
# by calculating the square of each element
# cộng hai mảng rồi bình phương
import numpy
arrayOne = numpy.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = numpy.array([[15 ,33, 24], [4 ,7, 1]])

addition = numpy.add(arrayOne,arrayTwo)
print(addition)

square = addition**2
print(square)

