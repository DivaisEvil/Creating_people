import file_operations
from faker import Faker
import random

MIN_SKILL_LEVEL = 3
MAX_SKILL_LEVEL = 18
NUMBER_OF_PROFILES = 10

RUNES = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}

SKILLS = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд"
]


def creat_profile_content(num, runic_skills, fake):
    hero_skill_1, hero_skill_2, hero_skill_3 = random.sample(runic_skills, 3)
    context = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "job": fake.job(),
        "town": fake.city(),
        "strength": random.randint(MIN_SKILL_LEVEL, MAX_SKILL_LEVEL),
        "agility": random.randint(MIN_SKILL_LEVEL, MAX_SKILL_LEVEL),
        "endurance": random.randint(MIN_SKILL_LEVEL, MAX_SKILL_LEVEL),
        "intelligence": random.randint(MIN_SKILL_LEVEL, MAX_SKILL_LEVEL),
        "luck": random.randint(MIN_SKILL_LEVEL, MAX_SKILL_LEVEL),
        "skill_1": hero_skill_1,
        "skill_2": hero_skill_2,
        "skill_3": hero_skill_3
    }
    return context


def main():
    fake = Faker("ru_RU")
    runic_skills = []
    for skill in SKILLS:
        new_skill = skill
        for letter in skill:
            new_skill = new_skill.replace(letter, RUNES[letter])
        runic_skills.append(new_skill)

    for num in range(NUMBER_OF_PROFILES):
        context = creat_profile_content(num, runic_skills, fake)
        file_operations.render_template("charsheet.svg", "Card_Hero/result{}.svg".format(num), context)


if __name__ == '__main__':
    main()
