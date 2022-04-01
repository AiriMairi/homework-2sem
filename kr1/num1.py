from random import randint

class Machine:
    def __init__(self, caliber, weight, power):
        self.caliber = caliber
        self.weight = weight
        self.power = power

    def get_in(self, name_queue):
        name_queue.list.insert((randint(0, name_queue.length - 1)), (self))
        name_queue.length += 1

    def takeaqueue(self, queue_obj):
        return Queue.static_add_machine(queue_obj, self)

    def repr(self):
        return f'Снаряд 1: {self.caliber}, {self.weight}, {self.power}'

class Queue:
    def __init__(self):
        self.queue: list = []
        self.lenght: int = 0

    @staticmethod
    def static_add_machine(queue_obj, person):
        return queue_obj.add_item(person)

    def add_item(self, machine):
        self.queue.append(machine)
        self.lenght += 1

    def delete(self):
        if self.length == 0:
            raise ValueError('Список пуст')
        else:
            self.queue.remove()
            self.length -= 1

    def len(self):
        return self.length

    def output(self):
        print(self.queue)

    def repr(self):
        return self.queue

    def txt(self):
        n = len(self.queue)
        f = open('num1.txt', 'w')
        f.writelines(f'В обойме {n} снарядов:')
        for i in len(self.queue):
            f.writelines(f'Снаряд {i + 1}: {self.caliber}, {self.weight}, {self.power}')
        f.close()
que = Queue()
g = Machine(randint(6, 20), randint(34, 36), randint(7, 13))
h = Machine(randint(6, 20), randint(34, 36), randint(7, 13))
que.add_item(g)
que.add_item(h)
b = Machine(randint(6, 20), randint(34, 36), randint(7, 13))
que.output()
que.txt()





        # caliber = randint(6, 20)
        # weight = randint(34, 36)
        # power = caliber*weight
        # n = randint(1, 30)
        # que = []
        # for i in n:
        #     que.append(i)
        # print(que)
        #
        # with open('num1.txt', 'w') as f:
        #     f.write(f'В обойме {n} снарядов:')
        #     for i in n:
        #         f.write(f'Снаряд {i+1}: {caliber}, {weight}, {power}')




