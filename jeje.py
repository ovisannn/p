data = [5,3,1,2]

for x in range (1, len (data)):
	print("Ketika x = ", x)
	print("Proses", x)
	print("Sebelum sorting: ", data)
	print(" ")
	for y in range (x, 0, -1):
		print("Ketika y = ", y)
		if data[y] < data[y-1]:
			tmp = data[y]
			data[y] = data[y-1]
			data[y-1] = tmp
		print ("Tmp = ", tmp)
		print ("Data[y] = ", data[y])
		print ("Data[y-1] = ", data[y-1])
		print(" ")
		print(data)
		print(" ")