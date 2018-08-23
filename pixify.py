import sys, cv2, numpy

def replace(a, b, x, y):
	res = a
	for i in range(x, x + len(b)):
		for j in range(y, y + len(b[0])):
			res[i][j] = b[i - x][j - y]
	return res

split_size = int(sys.argv[2])
input_img = cv2.imread(sys.argv[1])

x_size = len(input_img) // split_size
y_size = len(input_img[0]) // split_size

print("split by = ", int(sys.argv[2]))
print("width, height = ", len(input_img), ", ", len(input_img[0]))
print("x_size, y_size = ", x_size, ", ", y_size)

output_img = input_img

for x in range(0, len(input_img), 2 * x_size):
	if x >= len(output_img): 
		break
	for y in range(0, len(input_img[0]), 2 * y_size):
		if y >= len(output_img[0]): 
			break
		output_img = replace(output_img, [i[y : y + y_size] for i in input_img[x : x + x_size]], int(x/2), int(y/2))

cv2.imwrite("output.jpg", numpy.array([i[:int(len(output_img[0])/2)] for i in output_img[:int(len(output_img)/2)]]))