def print_square(square):
    for row in square:
        print(" ".join(f"{num:3d}" for num in row))
    print()
    

# For odd n (3, 5, 7...)
# Start from middle of first row
# Place next number diagonally up-right
# If that cell is occupied, move down one instead
def magic_square_odd(n):
    square = [[0] * n for _ in range(n)]
    num = 1
    i, j = 0, n // 2

    while num <= n * n:
        square[i][j] = num
        num += 1
        new_i, new_j = (i - 1) % n, (j + 1) % n
        if square[new_i][new_j]:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j
    return square


# For doubly even n (like 4, 8, 12...)
# Fill the square normally from 1 to n^2
# Then invert specific cells (flip value: n*n + 1 - value) based on:
# if (i % 4 == j % 4) or (i + j) % 4 == 3
def magic_square_doubly_even(n):
    square = [[(i * n) + j + 1 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i % 4 == j % 4) or ((i + j) % 4 == 3):
                square[i][j] = n * n + 1 - square[i][j]
    return square


# For singly even n (6, 10...)
# Split the board into 4 quadrants
# Fill each quadrant with a mini magic square of order n/2
# Shift and swap specific columns between quadrants to maintain the magic properties
def magic_square_singly_even(n):
    half = n // 2
    mini_square = magic_square_odd(half)
    square = [[0] * n for _ in range(n)]

    add = [0, 2, 3, 1]
    for i in range(half):
        for j in range(half):
            for k in range(4):
                row = i + (k // 2) * half
                col = j + (k % 2) * half
                square[row][col] = mini_square[i][j] + add[k] * (half * half)

    cols = half // 2
    for i in range(n):
        for j in range(cols):
            if j == cols and i >= half:
                continue
            if i < half:
                square[i][j], square[i + half][j] = square[i + half][j], square[i][j]

    for i in range(n):
        for j in range(n - cols + 1, n):
            if i < half:
                square[i][j], square[i + half][j] = square[i + half][j], square[i][j]

    return square


def magic_square(n):
    if n % 2 == 1:
        return magic_square_odd(n)
    elif n % 4 == 0:
        return magic_square_doubly_even(n)
    else:
        return magic_square_singly_even(n)

for n in [4, 5, 6, 7, 8]:
    print(f"\nMagic Square of size {n}:")
    square = magic_square(n)
    print_square(square)
