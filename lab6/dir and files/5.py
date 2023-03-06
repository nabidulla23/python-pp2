#Write a Python program to write a list to a file.
disciplines = ['FEE2', 'PP2', 'DD', 'Sociology', 'Kazakh language', 'MandM']
with open('semester4.txt', "w") as f:
        for i in disciplines:
                f.write(i+'\n')
content = open('semester4.txt')
print(content.read())
content.close()