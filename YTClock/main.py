import random
import webbrowser
from time import sleep


h = input("Enter Number of Hours:")
m = input("Enter Number of Minutes:")

print("A random Youtube Video will play from the collection in " + h + " - Hours and " + m + " - Minutes.")
total_min = int((h * 60) + m)
while total_min > 0:
    sleep(60)
    total_min -= 1

file_path = 'links.txt'
try:
    fp = open(file_path)
except IOError:
    # If not exists, create the file
    fp = open(file_path, 'w+')
    fp.write("https://www.youtube.com/watch?v=JGwWNGJdvx8")
    fp.close()

num_lines = sum(1 for line in open('links.txt'))
rand_selec = random.randint(1, num_lines)
file = open(file_path)

url = file.readlines()[rand_selec-1]
webbrowser.open(url)
