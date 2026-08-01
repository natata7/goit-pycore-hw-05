def generator_numbers(text):
    """Генератор чисел з рядка тексту"""

    for word in text.split():
        try:
            yield float(word)
        except ValueError:
            continue

def sum_profit(text, generator):
    """Обчислення загального доходу працівника"""

    return sum(generator(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")