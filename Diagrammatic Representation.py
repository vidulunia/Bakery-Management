import matplotlib.pyplot as pl
item=['RED VELVET','COFFEE CARAMEL','HAZELNUT','BLUEBERRY CHEESECAKE','BANOFFEE PIE']
sales=[250,170,176,198,205]
pl.bar(item,sales,color=['red','brown','black','blue','yellow'])
pl.xlabel("CAKE FLAVOUR --->")
pl.ylabel("QUANTITY --->")
pl.title("SALES ON 17-03-2022")
pl.show()
