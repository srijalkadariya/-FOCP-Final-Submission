#a program that prompts a user to enter a temperature in Celsius, and then displays the corresponding temperature in Fahrenheit,

temparature_celcius=float(input("Enter a temparature in Celcius: "))
temparature_fahrenheit=(temparature_celcius * 9/5)+32
print(f"{temparature_celcius}C is equivalent to {temparature_fahrenheit}F.")