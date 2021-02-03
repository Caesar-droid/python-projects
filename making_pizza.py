#using module to call specific function
from pizzas import make_pizza
make_pizza(16,'pepperoni')
make_pizza(12,'pepperoni','extra cheese','green pepper')
#using as to give a function an alias
from pizzas import make_pizza as mp
mp(16,'pepperoni')
mp(12,'pepperoni','extra cheese','green pepper')
#using as to give a module an alias
import pizzas as p
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'pepperoni','extra cheese','green pepper')
#importing all functions from a module
from pizzas import *
make_pizza(16,'pepperoni')
make_pizza(12,'pepperoni','extra cheese','green pepper')