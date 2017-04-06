from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///outdoorcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


user = User(name="Outdoor Guy", email="outdoorguy@outdoorcatalog.com",
             picture='../../../static/img/logo.png')
session.add(user)
session.commit()

kayaking = Category(user_id=1, name="Kayaking")

session.add(kayaking)
session.commit()

kayakingItem1 = Item(user_id=1, name="Tent", description="Best two person tent available", category=kayaking)

session.add(kayakingItem1)
session.commit()

camping = Category(user_id=1, name="Camping")

session.add(camping)
session.commit()

campingItem1 = Item(user_id=1, name="Tent", description="Best two person tent available", category=camping)

session.add(campingItem1)
session.commit()

rock = Category(user_id=1, name="Rock Climbing")

session.add(rock)
session.commit()

rockItem1 = Item(user_id=1, name="Tent", description="Best two person tent available", category=rock)

session.add(rockItem1)
session.commit()

fishing = Category(user_id=1, name="Fishing")

session.add(fishing)
session.commit()

fishingItem1 = Item(user_id=1, name="Tent", description="Best two person tent available", category=fishing)

session.add(fishingItem1)
session.commit()

hiking = Category(user_id=1, name="Hiking")

session.add(hiking)
session.commit()

hikingItem1 = Item(user_id=1, name="Tent", description="Best two person tent available", category=hiking)

session.add(hikingItem1)
session.commit()

biking = Category(user_id=1, name="Mountian Biking")

session.add(biking)
session.commit()

bikingItem1 = Item(user_id=1, name="Tent", description="Best two person tent available", category=biking)

session.add(bikingItem1)
session.commit()


print "added items!"
