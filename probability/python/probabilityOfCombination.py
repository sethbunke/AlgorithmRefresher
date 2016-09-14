import math

find_combinations = lambda N, k: math.factorial(N) /(math.factorial(k) * math.factorial(N - k))

#print(find_combinations(10, 8))

find_probability = lambda N, k, p ,q: ((p ** k) * (q ** (N - k))) * find_combinations(N,k)

print(find_probability(10, 8, 0.6, 0.4))