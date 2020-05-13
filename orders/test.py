from orders.models import Category, Dish
    
mycat = Category(name='mycat')
mycat.save()
mydish = Dish(name='mydish', max_allowed_extras=0)
mydish.save()

mydish.category.add(mycat)
print(mydish)
