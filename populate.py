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

kayakingItem1 = Item(user_id=1, name="Kayak", description="Can't go kayaking if you forget your boat.", category=kayaking)

session.add(kayakingItem1)
session.commit()

kayakingItem2 = Item(user_id=1, name="Paddle", description="You're not going to be moving without a paddle", category=kayaking)

session.add(kayakingItem2)
session.commit()

kayakingItem3 = Item(user_id=1, name="Life Jacket", description="Even the best swimmers need to wear life jackets. Kayaking can be dangerous.", category=kayaking)

session.add(kayakingItem3)
session.commit()

camping = Category(user_id=1, name="Camping")

session.add(camping)
session.commit()

campingItem1 = Item(user_id=1, name="Tent", description="Tents come in all different sizes so make sure to bring the right size for your trip.", category=camping)

session.add(campingItem1)
session.commit()

campingItem2 = Item(user_id=1, name="Hachet", description="You have to have a fire when camping. A hachet is the perfect tool to cut up small firewood.", category=camping)

session.add(campingItem2)
session.commit()

campingItem3 = Item(user_id=1, name="First Aid Kit", description="When you're off the grid, you always want to make sure you have a first aid kit.", category=camping)

session.add(campingItem3)
session.commit()

campingItem4 = Item(user_id=1, name="Sleeping Bag", description="Sometimes it can get cold at night so make sure you bring a well insulated sleeping bag.", category=camping)

session.add(campingItem4)
session.commit()

campingItem5 = Item(user_id=1, name="Water", description="Always make sure to have plenty of drinkable water with you.", category=camping)

session.add(campingItem5)
session.commit()

campingItem6 = Item(user_id=1, name="Flashlight", description="You don't want to have to wake up in the middle of the night and realize you forgot your flashlight.", category=camping)

session.add(campingItem6)
session.commit()

rock = Category(user_id=1, name="Rock Climbing")

session.add(rock)
session.commit()

rockItem1 = Item(user_id=1, name="Climbing Shoes", description="Grip is important so make sure you have the right shoes to get you to the top.", category=rock)

session.add(rockItem1)
session.commit()

rockItem2 = Item(user_id=1, name="Safety Harness", description="Nothing ruins a trip like a fifty foot fall, always make sure to be safe when climbing.", category=rock)

session.add(rockItem2)
session.commit()

fishing = Category(user_id=1, name="Fishing")

session.add(fishing)
session.commit()

fishingItem1 = Item(user_id=1, name="Pole", description="You can't go fishing if you forget your pole.", category=fishing)

session.add(fishingItem1)
session.commit()

fishingItem2 = Item(user_id=1, name="Bait", description="Wether you prefer live bait or lures, you have to have the right bait.", category=fishing)

session.add(fishingItem2)
session.commit()

fishingItem3 = Item(user_id=1, name="Fishing Line", description="Even the best of us get stuck in the tress sometimes, best to always have extra fishing line.", category=fishing)

session.add(fishingItem3)
session.commit()

hiking = Category(user_id=1, name="Hiking")

session.add(hiking)
session.commit()

hikingItem1 = Item(user_id=1, name="Hiking Boots", description="It sounds obvious but you never want to hike without the perfect pair of boots. I reccommend something light and waterproof.", category=hiking)

session.add(hikingItem1)
session.commit()

hikingItem2 = Item(user_id=1, name="Walking Sticks", description="When you have a heavy pack, nothing beats a good set of walking sticks.", category=hiking)

session.add(hikingItem2)
session.commit()

hikingItem3 = Item(user_id=1, name="Compass", description="You never know when you'll take a wrong turn, make sure to bring your compass.", category=hiking)

session.add(hikingItem3)
session.commit()

hikingItem4 = Item(user_id=1, name="Map", description="Cell phones die or don't have service, always make sure to bring a map.", category=hiking)

session.add(hikingItem4)
session.commit()

hikingItem5 = Item(user_id=1, name="Water", description="Staying hydrated will make your hike much more enjoyable.", category=hiking)

session.add(hikingItem5)
session.commit()

biking = Category(user_id=1, name="Mountian Biking")

session.add(biking)
session.commit()

bikingItem1 = Item(user_id=1, name="Helmet", description="Safety first! Never ride without a helmet.", category=biking)

session.add(bikingItem1)
session.commit()

bikingItem2 = Item(user_id=1, name="Tire Pump", description="Having a compact tire pump with you at all times is a great idea.", category=biking)

session.add(bikingItem2)
session.commit()

bikingItem3 = Item(user_id=1, name="Tire Patch", description="This is a must. You don't want to be stuck in the mountians with a flat tire.", category=biking)

session.add(bikingItem3)
session.commit()

bikingItem4 = Item(user_id=1, name="Camelback", description="Best two person tent available", category=biking)

session.add(bikingItem4)
session.commit()


print "outdoor items added!"
