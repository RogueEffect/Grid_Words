
import sys

def get_words(grid, size):
    # grid is just a string of characters as they appear in the grid
    # using size we can extract the horizontal and vertical words
    # from the grid and append them to the list
    words = []
    for i in range(size):
        # take horizontal slices of strings
        words.append(grid[i * size: i * size + size])
        # take vertical slices of strings
        words.append(grid[i::size])
    # finally return all the words plus all their reversed counterparts
    return words + [word[::-1] for word in words] # "str"[::-1] is reversed

def check_word(word, words):
    # check to see if the substring word appears in any string in words
    for w in words:
        if word in w: return True
    return False

def run_test(grid, size, words):
    # use grid and size to get all possible words in the grid
    grid_words = get_words(grid, size)
    # for each string in words check if it appears in the grid
    for word in words:
        if check_word(word, grid_words):
            print("Yes", end=' ')
        else:
            print("No", end=' ')



if len(sys.argv) < 2:
    print("usage: grid_words input_file")
    exit()

with open(sys.argv[1]) as f:
    # input file is broken into a list of strings seperated by newline
    data = f.read().split('\n')

# out first line tells us the size of grid
size = int(data.pop(0)) # popping data out of the list to easily get
grid = ""               # the word list at the end

for i in range(size):
    # the grid is inputted with space seperated chars, we'll remove the spaces
    grid += data.pop(0).replace(' ','')
# this next line in data gives the number of words to expect, but its useless
data.pop(0) # yeet

# by this point all thats left in the data array is the word list
# we can run the test now
run_test(grid, size, data)
