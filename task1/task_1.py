ln=list(input("Введіть рядок: "))
numbers=[]
numbers2=[]
l = len(ln)
integ = []
i = 0
while i < l:
    ln_int = ''
    a = ln[i]
    while '0' <= a <= '9':
        ln_int += a
        i += 1
        if i < l:
            a = ln[i]
        else:
            break
    i += 1
    if ln_int != '':
        numbers.append(int(ln_int))
for i in range(len(ln)):
    if '1' in ln:
        ln.remove('1')
    elif '2' in ln:
        ln.remove('2')
    elif '3' in ln:
        ln.remove('3')
    elif '4' in ln:
        ln.remove('4')
    elif '5' in ln:
        ln.remove('5')
    elif '6' in ln:
        ln.remove('6')
    elif '7' in ln:
        ln.remove('7')
    elif '8' in ln:
        ln.remove('8')
    elif '9' in ln:
        ln.remove('9')
    elif '0' in ln:
        ln.remove('0')
ln = ''.join(ln)
print('Рядок без чисел:',ln)
print("Масив чисел:\n", numbers)
def capitalize(s):
     s, result = s.title(), ""
     for word in s.split():
        result += word[:-1] + word[-1].upper() + " "
     return result[:-1]     
print("Рядок, кожне слово якого починається та закінчується великою буквою:\n",capitalize(ln))
print("Максимальне число:",max(numbers))
max_index=numbers.index(max(numbers))
i=0
for i in range(len(numbers)):
    if i==max_index:
        continue
    temp = numbers[i] ** i
    numbers2.append(temp)
print("Масив чисел, які піднесені до степеню по їх індексу:\n",numbers2)












