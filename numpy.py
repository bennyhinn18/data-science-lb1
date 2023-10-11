import numpy as np
array = np.arange(20).reshape(5, 4)
print(array)
print()
print(np.argmax(array))
print(np.argmax(array, axis=1))
print(np.argmax(array, axis=0))
