#6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input("Со скольки км начнем пробежки в первый день?"))
b = int(input("Какую цель ставим перед собой?"))
day = 1
while a < b:
    a *= 1.1
    day += 1
print("Результат может быть достигнут через: ", day, "дней")