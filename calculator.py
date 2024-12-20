def text_to_number(word):
    # Словарь для перевода слов в числа
    numbers = {
        "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5,
        "шесть": 6, "семь": 7, "восемь": 8, "девять": 9, "десять": 10,
        "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14,
        "пятнадцать": 15, "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18,
        "девятнадцать": 19, "двадцать": 20, "тридцать": 30, "сорок": 40,
        "пятьдесят": 50, "шестьдесят": 60, "семьдесят": 70, "восемьдесят": 80,
        "девяносто": 90
    }
    return numbers.get(word.lower(), None)

def number_to_text(number):
    # Словарь для перевода чисел в текст
    units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
             "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]

    if number < 10:
        return units[number]
    elif number < 20:
        return teens[number - 10]
    else:
        ten_part = tens[number // 10]
        unit_part = units[number % 10]
        return ten_part + (unit_part if number % 10 > 0 else "")

def calc(expression):
    parts = expression.split()
    if len(parts) != 3:
        return "Некорректный ввод"

    num1_text, operation, num2_text = parts
    num1 = text_to_number(num1_text)
    num2 = text_to_number(num2_text)

    if num1 is None or num2 is None:
        return "Некорректный ввод чисел"

    if operation == "плюс":
        result = num1 + num2
    elif operation == "минус":
        result = num1 - num2
    elif operation == "умножить":
        result = num1 * num2
    else:
        return "Некорректная операция"

    return number_to_text(result)

# Пример использования
print(calc("пятьдесят минус сорок"))  # "десять"
print(calc("два умножить три"))  # "шесть"
