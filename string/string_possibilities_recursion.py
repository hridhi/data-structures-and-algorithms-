#Given a list of word lists How to print all sentences possible taking one word from a list at a time via recursion?



R = 3
C = 3
def printUtil(arr, m, n, output):

	
	output[m] = arr[m][n]

	
	if m==R-1:
		for i in range(R):
			print (output[i],end=" ")
		print ("\n")
		return

	
	for i in range(C):
		if arr[m+1][i] != "":
			printUtil(arr, m+1, i, output)


def printf(arr):
	output = [""] * R

	
	for i in range(C):
		if arr[0][i] != "":
			printUtil(arr, 0, i, output)


arr = [ ["you", "we",""],
		["have", "are",""],
		["sleep", "eat", "drink"]]
printf(arr)

