def generate_squares(n):
    squares = [i**2 for i in range(1, n + 1)]
    return squares[:5] + squares[-5:]


print(generate_squares(30))
