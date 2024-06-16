from user1 import User1
from card import Card

alex = User1("Alex")

alex.sayName()
alex.setAge(33)
alex.sayAge()


card = Card("4353 1234 4353 4353", "11/28", "Alex F")
alex.addCard(card)
alex.getCard().pay(1000)