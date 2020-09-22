# дебильный калькулятор v2

from colorama import init
from colorama import Fore, Back, Style
# use Colorama to make Termcolor work on Windows too
init()
print ( Fore.BLACK )
print ( Back.GREEN )

what = input("что делаем (+,-):")
print ( Back.CYAN )

a = float ( input("первое число"))
b = float ( input("второе число"))

if what == "+":
    c = a + b
    print("результат " + str(c))

elif what == "-":
    c = a - b
    print("результат " + str(c))

else:
    print("результат не найден")
input()
    


