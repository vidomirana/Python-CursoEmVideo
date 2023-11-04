## alguns testes de string

n = (input('Digite algo: '))
print(type(n))
print('é alfanumérico? /', n.isalnum())
print('é alfabético? /', n.isalpha())
print('está somente com maiúsculas? /', n.isupper())
print('está somente em minúsculas? /', n.islower())
print('pode ser impresso? /', n.isprintable())
print('é um decimal? /', n.isdecimal())
print('isdigit /', n.isdigit())
print('isidentifier /', n.isidentifier())
print('isspace /', n.isspace())
print('istitle /', n.istitle())
print('------------------------------------------')
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())