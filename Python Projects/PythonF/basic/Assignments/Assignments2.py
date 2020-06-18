#Name = Eugene Parker
#Task : Created a list with three Countries in it.
        # 1. Update the list
        # 2. Remove any element using the indexing approach
        # 3. Add a country in the middle of the list.

        # * Do the same of set *

#Creating a country list
country_list = ["Algeria","Canada","Morocco"]
print("Country List :",country_list)

#Updating the list
country_list.append("Ghana")
print("Updated list: ",country_list)

#Removing an element from the list
# 1.  country_list.remove("Algeria")
del(country_list[0])
print(country_list)

#Adding a country element in the middle of the list
country_list.insert(2,"USA")
print(country_list)


#Creating a Country Set
country_set = {"Algeria","Canada","Morocco"}
print(country_set)

#Updating the set
country_set.update(["Italy"])
print(country_set)

#Removing an element from the set
country_set.remove("Morocco")
print(country_set)

#Adding a country element in the middle of the set
country_set.insert(1,"Belgium")
print(country_set)

#Freeze Current Set
frozen = frozenset(country_set)
print(frozen)
