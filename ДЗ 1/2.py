# Задание 2

def nn(names):
    count = {}

    for name in names:
        if name not in count:
            count[name] =1
        else:
            count[name] += 1

        return count


names = (' Динар', 'Пётр', 'Саша', 'Динар', 'Динар', 'Саша')
r = nn(names)

print(r)
