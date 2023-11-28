class Counter:
    def __init__(self, initial_value):
        self.value = initial_value

    def inc(self):
        self.value += 1
        return self.value

    def dec(self):
        self.value -= 1
        return self.value

class ReverseCounter(Counter):
    def inc(self):
        self.value -= 1
        return self.value

    def dec(self):
        self.value += 1
        return self.value

def get_counter(number):
    if number >= 0:
        return Counter(number)
    else:
        return ReverseCounter(number)


counter1 = get_counter(5)
a = counter1.inc()
b = counter1.inc()
c = counter1.inc()
d = counter1.dec()
print(a, b, c, d)

counter2 = get_counter(-1)
a = counter2.inc()
b = counter2.inc()
c = counter2.inc()
d = counter2.dec()
print(a, b, c, d)
