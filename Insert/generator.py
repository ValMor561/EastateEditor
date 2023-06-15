from russian_names import RussianNames
import random
import faker
from datetime import datetime, timedelta

def get_random_birth_date():
    start_date = datetime(1950, 1, 1)
    end_date = datetime(2005, 1, 1)
    delta = end_date - start_date
    random_days = random.randrange(delta.days)
    return start_date + timedelta(days=random_days)

def generate_contract_data():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2023, 1, 1)
    contract_date = start_date + (end_date - start_date) * random.random()

    days_until_payment = timedelta(days=random.randint(1, 60))
    payment_date = contract_date + days_until_payment

    return {
        'DateOfContract': contract_date.strftime('%Y-%m-%d'),
        'DateOfPayment': payment_date.strftime('%Y-%m-%d')
    }

def generate_company_name():
    words = ['Элегантный', 'Имперский', 'Лаконичный', 'Престижный', 
            'Надежный', 'Премиум', 'Роскошный', 'Современный', 
            'Столичный', 'Уютный', 'Эксклюзивный', 'Элитный']
    suffixes = ['район', 'дом', 'округ']
    with open('companies.txt', 'w', newline='',encoding='utf-8') as file:
        i = 0
        for word in words:
            for suffix in suffixes:
                file.write(f"{i};{word} {suffix}\n")
                i += 1

def generate_employee():
    rn = RussianNames(count=10000, patronymic=False, transliterate=False)
    with open('employee.txt', 'w', newline='',encoding='utf-8') as file:
            i = 0
            for person in rn:
                    name, surname = person.split(' ')
                    companyid = random.randint(1, 35)
                    file.write(f"{i};{surname};{name};{companyid}\n")
                    i += 1
 
def generate_passport(passlist):
    fake = faker.Faker(locale="ru_RU")
    i = 0
    with open('passports.txt', 'w', newline='',encoding='utf-8') as file:
        for passportnumber in passlist:
            name = fake.first_name()
            surname = fake.last_name()
            date_of_birth = get_random_birth_date()
            date_of_birth_str = date_of_birth.strftime('%Y-%m-%d')
            codeofice = random.randint(1000, 9999)
            family = random.choice(['в браке', 'не в браке'])
            city = fake.city()
            age = datetime.now().year - date_of_birth.year
            file.write(f"{passportnumber};{date_of_birth_str};{codeofice};{family};{name};{surname};{city};{age}\n")
            print(i)
            i += 1
        

def generate_contract(passlist):
    ownerlist = []
    i = 0
    with open('contract.txt', 'w', newline='',encoding='utf-8') as file:
        for _ in range(5000):
            date_of_contract = generate_contract_data()['DateOfContract']
            date_of_payment = generate_contract_data()['DateOfPayment']
            cost = random.randint(1000000, 100000000)
            employid = random.randint(1,9999)
            contract_type = random.choice(['аренда', 'покупка'])
            owner,client = random.sample(passlist, 2)
            ownerlist.append(owner)
            file.write(f"{i};{date_of_contract};{date_of_payment};{cost};{employid};{contract_type};{owner};{client}\n")
            i += 1
    return ownerlist

def generate_district():
    fake = faker.Faker(locale="ru_RU")
    i = 0
    with open('district.txt', 'w', newline='',encoding='utf-8') as file:
        for _ in range(1000):
            city = fake.city()
            street = fake.unique.street_name()
            file.write(f"{i};{city};{street}\n")
            i += 1

def generate_eastate(ownerlist):
    fake = faker.Faker(locale="ru_RU")
    i = 0
    with open('eastate.txt', 'w', newline='',encoding='utf-8') as file:
        for owner in ownerlist:
            addres = fake.street_address()
            square = random.randint(100,2000)
            type = random.choice(['квартира', 'торговая недвижимость', 'общественная недвижимость'])
            districtid = random.randint(1,999)
            file.write(f"{i};{addres};{square};{type};{districtid};{owner}\n")
            i += 1
def main():
    generate_company_name()
    generate_employee()
    generate_district()
    
    passportlist = []
    fake = faker.Faker(locale="ru_RU")

    for _ in range(10000):
        pasportnumber = fake.unique.random_int(10000000, 99999999)
        passportlist.append(pasportnumber)

    generate_passport(passportlist)
    ownerlist = generate_contract(passportlist)
    generate_eastate(ownerlist)
