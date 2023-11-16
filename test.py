from sqlalchemy import func
from example import Customer, CreditCard, Order
from example import engine
from sqlalchemy.orm import Session

with Session(engine) as session:
    ## Question 1: print all user name with credit card
    # users = session.query(Customer).all()
    # for user in users:
    #     print(user.name, user.credit_card.number)

    ## Quesiton 2: print the credit card number of the first user
    # user = session.query(Customer).filter_by(id=1).first()
    # print(user.credit_card)

    ## Question 3: print the name of the user with credit card
    # user = (
    #     session.query(Customer)
    #     .join(Customer.credit_card)
    #     .filter(CreditCard.number == "2294999131880001")
    #     .first()
    # )
    # print(user.name)

    ## Question 4: Print all the orders of user 1
    # orders = (
    #     session.query(Order)
    #     .join(Order.customer)
    #     .filter(
    #         Customer.name == "Ritvik Soni",
    #     )
    #     .all()
    # )

    # for order in orders:
    #     print(order)

    ## Question 5: Print the user with order number 15
    # customer = session.query(Customer).join(Order).filter(Order.id == 15).first()

    # print(customer.name, customer.credit_card.number)

    ## Question 6: Find the credit card of the user which purchaged the order no 15
    # credit_card = (
    #     session.query(CreditCard)
    #     .join(CreditCard.customer)
    #     .join(Customer.orders)
    #     .filter(Order.id == 15)
    #     .first()
    # )

    # print(credit_card.number)

    ## Question 7: Find the orders made using the credit card 378039855191088
    # orders = (
    #     session.query(Order)
    #     .join(Order.customer)
    #     .join(Customer.credit_card)
    #     .filter(CreditCard.number == "378039855191088")
    #     .all()
    # )

    # for order in orders:
    #     print(order)

    ## Quesion 8: Find the sum of all items purchanged by user 15
    customer_id = 15
    total_quantity = (
        session.query(func.sum(Order.quantity))
        .join(Order.customer)
        .filter(
            Customer.id == customer_id,
        )
        .first()
    )[0]

    print(f"Total Quantity Purchanged by Customer {customer_id} is {total_quantity}")
