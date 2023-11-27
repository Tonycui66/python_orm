from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':

	# database_url = "postgresql://postgresql:postgresql@10.14.40.151:5432/postgresql?sslmode=disable"
	database_url = "postgresql://qbadmin:qianbase@10.14.40.152:26287/qianbase?sslmode=disable"
	engine  = create_engine(database_url)
	Base = declarative_base()
	class User(Base):
		__tablename__ = "t1"
		id = Column(Integer,primary_key=True)
		name = Column(String)
		age = Column(Integer)

	Session = sessionmaker(bind=engine)
	session = Session()
	users = session.query(User).all()
	for user in users:
		print(user.id,user.name,user.age)
