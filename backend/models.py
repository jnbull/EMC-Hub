from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
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


class User(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, unique=True)
    initial = Column('initial', String)
    email = Column('email', String)
    admin = Column('admin', Boolean)
    sender = relationship('Request', backref='sender', foreign_keys='Request.sender_id')
    receiver = relationship('Request', backref='receiver', foreign_keys='Request.receiver_id')


class Request(Base):
    __tablename__ = 'request'

    id = Column('id', Integer, primary_key=True)
    item = Column('item', String)
    sender_id = Column('senderID', Integer, ForeignKey('users.id'))
    receiver_id = Column('receiverID', Integer, ForeignKey('users.id'))


class Todos(Base):
    __tablename__ = 'todos'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, unique=True)
    category = Column('category', String)
    type_ = Column('type', String)


# Equipment DB Setup
engine = create_engine('sqlite:///tuv.db')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

# # User & Request DB Setup
# engine2 = create_engine('sqlite:///users.db')
# Base.metadata.create_all(bind=engine2)
# Session2 = sessionmaker(bind=engine2)


def addTodo(name, category, type_):

    session = Session()

    todo = Todos()
    todo.name = name
    todo.category = category
    todo.type_ = type_

    session.add(todo)
    session.commit()

    session.close()

    return(todo)

def addUser(name, initial, email, admin):

    session = Session()

    user = User()
    user.name = name
    user.initial = initial
    user.email = email
    user.admin = admin

    session.add(user)
    session.commit()

    session.close()

    return(user)


def queryUser(name):
    session = Session()

    user = session.query(User).filter_by(name=name).first()

    session.close()
    return(user)


def removeUser(name):

    session = Session()

    user = queryUser(name)
    session.delete(user)
    session.commit()
    session.close()


def addRequest(item, sender, receiver):

    session = Session()

    request = Request()
    request.item = item
    request.sender = queryUser(sender)
    request.receiver = queryUser(receiver)

    session.add(request)
    session.commit()

    session.close()


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
