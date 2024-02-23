from alchemyClasses.Renta import Renta
from alchemyClasses import db
import datetime

def get_rents():
    for rent in Renta.query.all():
        print(f'{rent}\n')


def get_rent_by_id(rent_id):
    return Renta.query.filter(Renta.idRentar == rent_id).first()


def get_new_date():
    year = 0
    while year < 1950 or year > 2024:
        try:
            year = int(input("Ingresa el nuevo año: "))
            if year < 1950 or year > 2024:
                print("Ingresa un año válido: ")
        except ValueError:
            print("Ingresa un año válido")
    month = 0
    while month < 1 or month > 12:
        try:
            month = int(input("Ingresa el nuevo mes: "))
            if month < 1 or month > 12:
                print("Ingresa un mes válido: ")
        except ValueError:
            print("Ingresa un mes válido")
    day = 0
    while day < 1 or (day > 29 and month == 2) or (day > 31 and month != 2):
        try:
            day = int(input("Ingresa el nuevo día: "))
            if day < 1 or day > 12:
                print("Ingresa un día válido: ")
        except ValueError:
            print("Ingresa un día válido")
    
    return datetime.date(year=year,month=month,day=day)
    
    


        

def change_rent_date(rent_id, new_date):
    rent = get_rent_by_id(rent_id)
    if rent:
        rent.fecha_renta = new_date
        db.session.commit()
        return True
    else:
        return False