from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import enlace

engine = create_engine(enlace)

from app import Docente, Matricula

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objetos de tipo Docente
vehiculo1 = Matricula(nombrePropietario="Tony", placa="García", \
        anio="Loja", costo=25.3)

vehiculo2 = Matricula(nombrePropietario="Luis", placa="Borrero", \
        anio="Loja", costo=25.3)

vehiculo3 = Matricula(nombrePropietario="Ana", placa="Salcedo", \
        anio="Zamora", costo=25.3)

vehiculo4 = Matricula(nombrePropietario="Monica", placa="Valenzuela", \
        anio="Zamora", costo=25.3)

# se agrega los objetos
# a la sesión
# a la espera de un commit
# para agregar un registro a la base de
# datos
session.add(vehiculo1)
session.add(vehiculo2)
session.add(vehiculo3)
session.add(vehiculo4)

# se confirma las transacciones
session.commit()
