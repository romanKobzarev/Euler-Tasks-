fibonacci_numbers = [1, 2]
while fibonacci_numbers[-1] < 4_000_000:
    temp = fibonacci_numbers[-1] + fibonacci_numbers[-2]
    if temp >= 4_000_000:
        break
    fibonacci_numbers.append(temp)
print(fibonacci_numbers)
even_summ = 0
for number in fibonacci_numbers:
    if number % 2 == 0:
        even_summ += number
print(even_summ)
