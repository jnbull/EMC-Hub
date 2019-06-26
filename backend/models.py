from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Equipment(Base):
    __tablename__ = 'equipment'

    id = Column('id', Integer, primary_key=True, unique=True)
    name = Column('name', String)
    type_ = Column('type', String)
    manufacturer = Column('manufacturer', String)
    calDate = Column('calDate', String)
    calDue = Column('calDue', String)


engine = create_engine('sqlite:///equipment.db')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


def addEquipment(id, name, type_, manufacturer, calDate, calDue):

    session = Session()

    equipment = Equipment()
    equipment.id = id
    equipment.name = name
    equipment.type_ = type_
    equipment.manufacturer = manufacturer
    equipment.calDate = calDate
    equipment.calDue = calDue

    session.add(equipment)
    session.commit()

    session.close()


def queryEquipment(filters):

    session = Session()
    equipmentList = []

    if 'id' in filters and filters['id'] != '':
        equipments = session.query(Equipment).filter(Equipment.id == filters['id'])
        for equipment in equipments:
            equipmentDict = {}
            equipmentDict.update([('id', equipment.id), ('manufacturer', equipment.manufacturer), ('type_', equipment.type_)])
            equipmentList.append(equipmentDict)
            print(str(equipment.id) + ' - ' + equipment.name + ' - ' + equipment.type_ + ' - ' + equipment.manufacturer + ' - ' + equipment.calDate + ' - ' + equipment.calDue)

    elif 'manufacturer' in filters and filters['manufacturer'] != '':
        equipments = session.query(Equipment).filter(Equipment.manufacturer == filters['manufacturer'])
        for equipment in equipments:
            equipmentDict = {}
            equipmentDict.update([('id', equipment.id), ('manufacturer', equipment.manufacturer), ('type_', equipment.type_)])
            equipmentList.append(equipmentDict)
            print(str(equipment.id) + ' - ' + equipment.name + ' - ' + equipment.type_ + ' - ' + equipment.manufacturer + ' - ' + equipment.calDate + ' - ' + equipment.calDue)

    elif 'type_' in filters and filters['type_'] != '':
        equipments = session.query(Equipment).filter(Equipment.type_ == filters['type_'])
        for equipment in equipments:
            equipmentDict = {}
            equipmentDict.update([('id', equipment.id), ('manufacturer', equipment.manufacturer), ('type_', equipment.type_)])
            equipmentList.append(equipmentDict)
            print(str(equipment.id) + ' - ' + equipment.name + ' - ' + equipment.type_ + ' - ' + equipment.manufacturer + ' - ' + equipment.calDate + ' - ' + equipment.calDue)

    session.close()
    return equipmentList


# print(queryEquipment({'id': '', 'manufacturer': '', 'type_': 'Spectrum Analyzer'}))