file = open("sample.txt", 'a+')

content = file.readlines()

print(content)

file.writelines("\nThis line is from python code  when you do it... and it is succesfull it feels awsome")

final= content = file.readlines()
print(final)