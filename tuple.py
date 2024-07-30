#CONCATENATING TUPLES
tuple1 = ("Geeks", "for", "Geeks")
tuple2 = (0,1,2,3.4)
tuple3 = tuple1 + tuple2
print(tuple3)


#ADDING ELENTS IN A TUPLE
fruits = ("mango","apple","pineapple")
fruitsList = list(fruits)
fruitsList[1] = "strawberry"
print(tuple(fruitsList))

#ACCESSING AN ELEMEMT IN A TUPLE
print(fruits[0])


#REMOVING ELENTS IN A TUPLE
countries = ("kenya","uganda","rwanda")
countryList = list(countries)
countryList.remove("uganda")
countries =tuple(countryList)
print(countries)

# for i in countries: print(i)



