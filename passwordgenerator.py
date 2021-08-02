import random

def shuffle(string):
    temporarylist = list(string)
    random.shuffle(temporarylist)
    return ''.join(temporarylist)

uppercaseLetter1=chr(random.randint(65,90))
lowercaseLetter1=chr(random.randint(ord('a'), ord('z')))   
uppercaseLetter2=chr(random.randint(65,90))
lowercaseLetter2=chr(random.randint(ord('a'), ord('z')))
uppercaseLetter3=chr(random.randint(65,90))
lowercaseLetter3=chr(random.randint(ord('a'), ord('z')))
uppercaseLetter4=chr(random.randint(65,90))
lowercaseLetter4=chr(random.randint(ord('a'), ord('z')))
uppercaseLetter5=chr(random.randint(65,90))
lowercaseLetter5=chr(random.randint(ord('a'), ord('z')))
uppercaseLetter6=chr(random.randint(65,90))
lowercaseLetter6=chr(random.randint(ord('a'), ord('z')))
uppercaseLetter7=chr(random.randint(65,90))
lowercaseLetter7=chr(random.randint(ord('a'), ord('z')))

number_1 = random.randint(0,9)
number_2 = random.randint(0,9)
number_3 = random.randint(0,9)
number_4 = random.randint(0,9)
number_5 = random.randint(0,9)

password = uppercaseLetter7+lowercaseLetter1+uppercaseLetter1+lowercaseLetter2+uppercaseLetter2+lowercaseLetter3+uppercaseLetter3+lowercaseLetter4+uppercaseLetter4+lowercaseLetter5+uppercaseLetter5+lowercaseLetter6+uppercaseLetter6+lowercaseLetter7+str(number_1)+str(number_2)+str(number_3)+str(number_4)+str(number_5)
password = shuffle(password)

print(password)