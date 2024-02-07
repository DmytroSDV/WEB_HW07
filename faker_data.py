from faker import Faker
from faker.providers import BaseProvider
import random


class MedicalProfessionsProvider(BaseProvider):
    def __init__(self, generator):
        super().__init__(generator)
        self.all_subjects = ["Мистецтво", "Комп'ютерні науки",
                             "Хімія", "Економіка", "Юриспруденція", "Маркетинг і менеджмент",
                             'Математика', "Археологія", "Палеотологія", "Фізика", "Астрологія", "Біологія",
                             "Планета земля", "Архітектура", "Українська мова", "Література",
                             "Психологія", "Англійска мова", "Машинобудівництво", "Електроніка",
                             "Музика", "Фізична культура", "Антропологія"]

        self.all_groups = ["Піонери Науки", "Зорепад", "Творча Спільнота", "Інтелектуальний Фронт",
                           "Знавці Знань", "Академічний Компас", "Елітні Мислителі", "Інноваційний Альянс",
                           "Лабораторія Мрійників", "Генії Природи", "Відкриті Горизонти"]

        self.all_professors = [
            "Професор Аркадій Петренко", "Доктор Лідія Васильчук", "Професор Віктор Михайлюк", "Доктор Юлія Ковальчук",
            "Професор Олексій Шевченко", "Доктор Анастасія Кравчук", "Професор Максим Сидоренко", "Доктор Ольга Данилюк",
            "Професор Володимир Павлюк", "Доктор Наталія Коваленко", "Професор Василь Лисенко", "Доктор Ірина Гриценко",
            "Професор Марина Черненко", "Доктор Сергій Кузьменко", "Професор Оксана Литвиненко",
            "Доктор Ігор Петров", "Професор Тетяна Іванова", "Доктор Вікторія Мельник", "Професор Андрій Гринь",
            "Доктор Назарій Зінченко"
        ]

        self.subject = self.all_subjects[:]
        self.group = self.all_groups[:]
        self.professor = self.all_professors[:]

    def subjects(self):
        if not self.subject:
            self.subject = self.all_subjects[:]
        random.shuffle(self.subject)
        return self.subject.pop()

    def groups(self):
        if not self.group:
            self.group = self.all_groups[:]
        random.shuffle(self.group)
        return self.group.pop()

    def professors(self):
        if not self.professor:
            self.professor = self.all_professors[:]
        random.shuffle(self.professor)
        return self.professor.pop()


class CustomFaker(Faker):
    def __init__(self, locale='en-US'):
        super().__init__(locale)
        self.add_provider(MedicalProfessionsProvider)


if __name__ == "__main__":
    print("Hello, this is custom faker!")
