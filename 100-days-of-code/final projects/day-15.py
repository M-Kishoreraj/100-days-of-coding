
# from turtle import Turtle, Screen
# #tim is the object and Turtle is the class
# tim=Turtle()
# print(tim)
# tim.shape("turtle")
# tim.color("red")
# tim.forward(100)
# tim.circle(25)

# #screen is the object and Screen is the class
# screen=Screen()
# #scree is the object and exitonclick is the method
# screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Countries_name" , ["India","Japan","Uk","Norway"])
table.add_column("Capital_name" , ["Delhi","Tokyo","London","Oslo"])
print(table.align)
print(table)
