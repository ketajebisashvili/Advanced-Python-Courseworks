import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime as dt


base = declarative_base()

#create table canteens
class canteen(base):
    __tablename__ = 'canteens'
    id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, db.ForeignKey('providers.id'))
    name = db.Column(db.String)
    location = db.Column(db.String)
    time_open = db.Column(db.types.Time)
    time_closed = db.Column(db.types.Time)

    def __repr__(self):
        return "<canteen(name='%s', location='%s', time_open='%s', time_closed='%s')>" % (
                self.name, self.location, self.time_open, self.time_closed)

#create table providers
class provider(base):
    __tablename__ = 'providers'
    id = db.Column(db.Integer, primary_key=True)
    provider_name = db.Column(db.String)

    def __repr__(self):
        return "<provider(name='%s')>" % self.provider_name

#insert data to providers 
providers = [
             provider(id=1, provider_name="Rahva Toit"),
             provider(id=2, provider_name="Baltic Restaurants Estonia AS"),
             provider(id=3, provider_name="TTU Sport")
             ]

#insert data to canteens
canteens = [
            canteen(id=1, name='Economics - and social science building canteen', provider_id=1, location='Akadeemia tee 3 SOC-building',
                    time_open=dt.time(8, 30), time_closed=dt.time(18, 30)),
            canteen(id=2, name='Library canteen', provider_id=1, location='Akadeemoia tee 1/Ehitajate tee 7',
                    time_open=dt.time(8, 30), time_closed=dt.time(19)),
            canteen(id=3, name='Main building Deli cafe', provider_id=2, location='Ehitajate tee 5 U01 building',
                    time_open=dt.time(9), time_closed=dt.time(16, 30)),
            canteen(id=4, name='Main building Daily lunch restaurant', provider_id=2,
                    location='Ehitajate tee 5 U01 building', time_open=dt.time(9), time_closed=dt.time(16,30)),
            canteen(id=5, name='U06 building canteen', provider_id=1, location='U06 building', time_open=dt.time(9),
                    time_closed=dt.time(16)),
            canteen(id=6, name='Natural science buiding canteen', provider_id=2,
                    location='Akadeemia tee 15 SCI building', time_open=dt.time(9), time_closed=dt.time(16)),
            canteen(id=7, name='ICT building canteen', provider_id=2, location='Raja 15/Mäepealse 1',
                    time_open=dt.time(9), time_closed=dt.time(16)),
            canteen(id=8, name='Sports building canteen', provider_id=3, location='Männiliiva 7 S01 building',
                    time_open=dt.time(11), time_closed=dt.time(20))
            ]


engine = db.create_engine('sqlite:///./diners_b.db', echo=False)
base.metadata.create_all(engine)


if __name__ == "__main__":
    # add data to tables
    session_maker = sessionmaker(bind=engine)
    session = session_maker()
    session.add_all(canteens)
    session.add_all(providers)


    # add itc provider
    itcp = provider(id=4, provider_name="BitStop Kohvik OU")
    session.add(itcp)
    session.commit()


    # add itc canteen
    itcc = canteen(name='bitStop KOHVIK', provider_id=4, location="Raja 4C", 
    time_open=dt.time(9, 30), time_closed=dt.time(16));
    session.add(itcc)
    session.commit()

    
  


    # canteens which are open 16.15-18.00
    print("\nDiners which are open between 16:15-18:00:")
    for row in session.query(canteen).filter(canteen.time_open <= dt.time(16,15)).filter(canteen.time_closed >= dt.time(18)).all():
        print("name: ", row.name)
        print("Closing time: ", row.time_closed, "\n")


    # canteens which are serviced by Rahva Toit
    print("\nDiners which provider is Rahva Toit:")
    for row in session.query(canteen).join(provider).filter(provider.provider_name == "Rahva Toit").all():
        print("name: ", row.name, "\n")


   
    
  
	

    # close database
    session.close()

