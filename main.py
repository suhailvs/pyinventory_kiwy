from kivy.base import runTouchApp                
import models
from modules.listwidget import List
from models import Inventory_Product as Product

models.create_tables_if_not_exist()

c = List()
products = [['ID','Name','Description','Price']]
for p in Product.select():
    products.append([str(p.id),p.name,p.description,str(p.price)])
    
c.data = products
runTouchApp(c)
