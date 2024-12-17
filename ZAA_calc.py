from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sys


def trig_test(x, function_type):
    """
    Вычисляет значение тригонометрической функции для заданного угла.

    :param x: Угол в градусах.
    :type x: float
    :param function_type: Тип тригонометрической функции ('sin', 'cos', 'tg', 'ctg').
    :type function_type: str
    :returns: Значение тригонометрической функции.
    :rtype: float
    :raises ZeroDivisionError: Если тангенс или котангенс не определены.
    :raises ValueError: Если указан неизвестный тип тригонометрической функции.
    """
    x = x / 180 * 3.1415
    q = x
    s = 0
    for i in range(1, 1000):
        s += q
        q = q * (-1) * (x * x) / ((2 * i + 1) * (2 * i))
    try:
        if function_type == "sin":
            return round(s, 3)
        g = round(s, 3)
        cos_x = (1 - g**2) ** 0.5
        if function_type == "cos":
            return round(cos_x, 3)
        if function_type == "tg":
            if cos_x == 0:
                raise ZeroDivisionError("Тангенс не определён для данного угла.")
            return round(g / cos_x, 3)
        if function_type == "ctg":
            if g == 0:
                raise ZeroDivisionError("Котангенс не определён для данного угла.")
            return round(cos_x / g, 3)
    except ZeroDivisionError as e:
        return str(e)


def convert_test(num, base):
    """
    Преобразует число в строку, представляющую его в заданной системе счисления.

    :param num: Число для преобразования.
    :type num: int
    :param base: Основание системы счисления (от 2 до 36).
    :type base: int
    :returns: Строка, представляющая число в заданной системе счисления.
    :rtype: str
    :raises ValueError: Если основание системы счисления не в диапазоне от 2 до 36.
    """
    if num == 0:
        return "0"
    if num < 0:
        raise ValueError
    if base == 16:
        return hex(num)[2:].upper()
    digits = []
    while num > 0:
        digits.append(str(num % base))
        num //= base
    return ''.join(digits[::-1])


def factorial_test(x):
    """
    Вычисляет факториал заданного неотрицательного целого числа.

    :param x: Целое неотрицательное число, для которого нужно вычислить факториал.
    :type x: int
    :returns: Факториал числа x.
    :rtype: int
    :raises ValueError: Если x не является неотрицательным целым числом.
    """
    if not isinstance(x, int):
        raise ValueError
    if x < 0:
        raise ValueError
    result_fact = 1
    for h in range(2, x + 1):
        result_fact *= h
    return result_fact


def evaluate_expression_test(expression):
    """
    Оценивает арифметическое выражение и возвращает результат.

    :param expression: Арифметическое выражение в виде строки.
    :type expression: str
    :returns: Результат вычисления выражения.
    :rtype: float
    :raises ZeroDivisionError: Если в выражении происходит деление на ноль.
    """
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Данное выражение не определено"


def process_key(key, entry_text):
    """
    Обрабатывает нажатие клавиши и возвращает новый текст для ввода.

    :param key: Нажатая клавиша.
    :type key: str
    :param entry_text: Текущий текст в поле ввода.
    :type entry_text: str
    :param abs_value: Абсолютное значение (по умолчанию 0).
    :type abs_value: float
    :returns: Новый текст для ввода и абсолютное значение.
    :rtype: str
    """
    try:
        if key == "=":
            str_1 = "0123456789*)(/."
            if not entry_text or entry_text[0] not in str_1:
                return "Ошибка: неверный ввод"
            result = evaluate_expression_test(entry_text)
            if isinstance(result, str):
                return "Данное выражение не определено"
            return str(result)
        elif key == "Del":
            return ""
        elif key == "±":
            if not entry_text:
                return "-"
            return entry_text[1:] if entry_text[0] == "-" else "-" + entry_text
        elif key == "Exit":
            root.destroy()
            sys.exit()
        elif key in ["sin", "cos", "tg", "ctg"]:
            return str(trig_test(float(entry_text), key))
        elif key == "x!":
            return str(factorial_test(int(entry_text)))
        elif key in ["+", "-", "*", "/", ")", "("]:
            return entry_text + key
        elif key in ["2-ная", "3-ная", "4-ная", "5-ная", "6-ная", "7-ная", "8-ная", "9-ная", "16-ная"]:
            base = int(key.split('-')[0])
            return str(convert_test(int(entry_text), base))
        elif key == "xⁿ":
            return entry_text + "**"
        else:
            return entry_text + key
    except Exception as e:
        return f"Ошибка: {str(e)}"


def calc(key):
    """
    Обрабатывает нажатие клавиши калькулятора и обновляет текст в поле ввода.

    :param key: Нажатая клавиша.
    :type key: str
    """
    entry_text = calc_entry.get()
    new_text = process_key(key, entry_text)
    calc_entry.delete(0, END)
    calc_entry.insert(END, new_text)


root = Tk()
root.title("Calculator")
calc_entry = Entry(root, width=50, font=("Times New Roman", 12, "bold"))
calc_entry.grid(row=0, column=0, columnspan=5)
calc_icons = [
    "7", "8", "9", "+", "*", "4", "5", "6", "-", "/",
    "1", "2", "3", "=", "xⁿ", "0", ".", "Del", "ctg",
    "sin", "cos", "tg", "2-ная", "3-ная", "4-ная",
    "5-ная", "6-ная", "7-ная", "8-ная", "9-ная",
    "16-ная", "x!", "(", ")", "Exit", "±"
]
r, c = 1, 0
for item in calc_icons:
    cmd = lambda x=item: calc(x)
    button = ttk.Button(root, text=item, command=cmd, width=10, style="TButton")
    style = ttk.Style()
    style.configure("TButton", font=("Times New Roman", 12, "bold"))
    button.grid(row=r, column=c)
    c += 1
    if c > 4:
        c = 0
        r += 1

root.mainloop()