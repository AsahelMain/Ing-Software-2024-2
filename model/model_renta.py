from alchemyClasses.Renta import Renta
from alchemyClasses import db

def get_rents():
    for rent in Renta.query.all():
        print(f'{rent}\n')


def get_rent_by_id(rent_id):
    print(f'{Renta.query.filter(Renta.idRentar == rent_id).first()}\n')