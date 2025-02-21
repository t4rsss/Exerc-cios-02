a = float(input("Digite o primeiro lado do triângulo: "))
b = float(input("Digite o segundo lado do triângulo: "))
c = float(input("Digite o terceiro lado do triângulo: "))
if a + b > c and a + c > b and b + c > a:
    print("Os valores formam um triângulo válido.")
else:
    print("Os valores não formam um triângulo.")
