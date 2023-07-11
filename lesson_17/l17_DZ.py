class DZ:

    def __init__(self):
        self.data = input('Enter somewhere: ')

    def processing(self):
        string = []
        integer = []
        default_glas = ['a', 'e', 'i', 'y', 'u', 'o']
        glas = []
        soglas = []
        summ = 0
        try:
            self.data = int(self.data)
            for i in str(self.data):
                integer.append(int(i))
        except ValueError:
            for i in self.data:
                string.append(i.lower())
        if string:
            for i in string:
                if i in default_glas:
                    glas.append(i)
                else:
                    soglas.append(i)
            if len(glas) * len(soglas) <= self.length():
                return glas
            else:
                return soglas
        else:
            for i in integer:
                if int(i) % 2 == 0:
                    summ += int(i)
            return summ * self.length()

    def length(self):
        return len(str(self.data))


task = DZ()
print(task.processing)
