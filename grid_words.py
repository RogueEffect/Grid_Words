
import sys

def get_words(grid, size):
    words = []
    for i in range(size):
        words.append(''.join(grid[i * size: i * size + size]))
        words.append(''.join(grid[i::size]))
    return words + [word[::-1] for word in words]

def check_word(word, words):
    for w in words:
        if word in w: return True
    return False

def run_test(grid, size, words):
    grid_words = get_words(grid, size)
    for word in words:
        if check_word(word, grid_words):
            print("Yes", end=' ')
        else:
            print("No", end=' ')



if len(sys.argv) < 2:
    print("usage: grid_words input_file")
    exit()

with open(sys.argv[1]) as f:
    data = f.read().split('\n')

size = int(data.pop(0))
grid = ""

for i in range(size):
    grid += data.pop(0).replace(' ','')
data.pop(0)

run_test(grid, size, data)
