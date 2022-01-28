centuries = int(input("Enter centuries: "))
years = centuries * 100
days = round(years * 365.2422)
hours = days * 24
minutes = hours * 60
 
print(f"{centuries} centuries = ", end = "")
print(f"{years} years = ", end = "")
print(f"{days} days = ", end = "")
print(f"{hours} hours = ", end = "")
print(f"{minutes} minutes = ", end = "")