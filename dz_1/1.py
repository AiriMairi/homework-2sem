from abc import ABC


class Human(ABC):
    def __init__(self, age, disabled_person, participant_in_the_war, name):

        self.age = age
        self.disabled_person = disabled_person
        self.participant_in_the_war = participant_in_the_war
        self.name = name

print('Вам больше 65 лет?: 1-да, 2-нет')
age = int(input())

print('У вас есть инвалидность?: 1-да, 2-нет')
disabled_person = int(input())

print('Вы участвовали в войне?: 1-да, 2-нет')
participant_in_the_war = int(input())

print('Введите Ваше имя.')
name = input()

go_to_queue = []
lenght = 1

if age == 1 or disabled_person == 1 or participant_in_the_war == 1 or name == 'Нияз' or name == 'нияз':
    print(f'{name}, Вы проходите без очереди!')
    go_to_queue.insert(0, name)
    lenght += 1
else:
    go_to_queue.append(name)
    print(f'{name}, Ваш номер {lenght}')
    lenght += 1


class Queue(ABC):
    def service_selection(self):
        print('Выберите услугу: 1-Карта, 2-Кредит/Ипотека, 3-Снять/положить наличные, 4-Открать вклад')
        service_selection = int(input())
        if service_selection == 1:
            print('Ваше окно: 1')
        elif service_selection == 2:
            print('Ваше окно: 2')
        elif service_selection == 3:
            print('Ваше окно: 3')
        elif service_selection == 4:
            print('Ваше окно: 4')
        else:
            print('Введите номер существующей услуги.')






queue = Queue()
queue.service_selection()
