# База даних користувачів зі списками оцінок
users = {
    "pedro": {"password": "123", "grades": [10, 11, 8, 4, 3, 12, 5]},
    "sashak": {"password": "456", "grades": [3, 2, 4, 7, 8, 1, 4]},
    "lemyr": {"password": "789", "grades": [12, 11, 10, 9, 12, 11]},
    "romashka": {"password": "000", "grades": [2, 5, 6, 8, 3, 4, 10]}
}

# Введення даних з клавіатури через термінал
login = input("Введіть логін: ")
password = input("Введіть пароль: ")

# Перевірка логіна та пароля
if login in users and users[login]["password"] == password:
    grades = users[login]["grades"]

    print("Вхід успішний!")
    print("Всі виставлені оцінки:", grades)

    # Лічильники для категорій оцінок
    zadovilno = 0
    nezadovilno = 0

    # Цикл перебору списку оцінок
    for grade in grades:
        if grade >= 5 and grade <= 12:
            zadovilno = zadovilno + 1
        elif grade >= 1 and grade <= 4:
            nezadovilno = nezadovilno + 1

    # Виведення результатів підрахунку
    print("Кількість оцінок від 5 до 12 (задовільно):", zadovilno)
    print("Кількість оцінок від 1 до 4 (незадовільно):", nezadovilno)
else:
    print("Невірний логін або пароль.")
