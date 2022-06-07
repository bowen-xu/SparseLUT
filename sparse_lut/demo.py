from sparse_lut import SparseLUT

# initialization
lut = SparseLUT((3, 3, 3, 3, 3))

# adding feature-lists
lut.add([[0,1,2], [0,1,2], [0,1,2], [0,1,2], [0,1,2]], "A")
lut.add([[1,2], [0], [0,1,2], [0,1,2], [0,1,2]], "B")
lut.add([[1,2], [1], [0,1,2], [0,1,2], [0,1,2]], "C")

# building the sparse-lut
lut.build(False) # set True is visualization is not required 

# visualization
lut.draw()

# accessing the value
result = lut[0,1,0,0,0]
print(result)

print('done.')
