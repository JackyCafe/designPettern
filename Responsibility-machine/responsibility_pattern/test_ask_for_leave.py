'''
# Create Date: 2021/7/16 
# File Name : test_ask_for_leave.py	
# Project NamedesignPettern	
# File Name : test_ask_for_leave	
# Writer by :yhlin	
'''
from responsibility_pattern import *


def main():
    supervisor = Supervisor("姚紹貿","製造部經理")
    department_manager = DepartmentManager("JOE","廠長")
    ceo = CEO("Andy","副總")
    administrator = Administrator("Judy","HR")
    supervisor.setNextHandler(department_manager)
    department_manager.setNextHandler(ceo)
    ceo.setNextHandler(administrator)

    Jacky = Person("Jacky",3,"一時耍廢一時爽")
    Jacky.setLeader(supervisor)
    Jacky.request()

    BoBo = Person("BoBo", 10, "一直時耍廢一直爽")
    BoBo.setLeader(supervisor)
    BoBo.request()


if __name__ == '__main__':
    main()