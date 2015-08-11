# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 12 for guidance
# Please do provide function calls that test/demonstrate your function

def rotate_word(x,y):
	for i in x:
		z = ord(i)
		
		w = z+y
		print chr(w),	
	
	
def main():
	x = raw_input("enter the string:")
	y = int(raw_input("enter the count by which you want to rotate the letters"))
	rotate_word(x,y)
	
	
	
	
	
if __name__ == '__main__':
    main()