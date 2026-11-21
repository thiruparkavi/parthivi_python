fruit = ["mango","strawberry","watermelon","dragonfruit","banana"]
print("length of list:", len(fruit))
print("first element:", fruit[0])
print("last element:", fruit[-1])

fruit.append("blueberry")
print("update list :", fruit)

fruit.remove("banana")
print("update list :", fruit)

fruit.sort()
print("sorted list :", fruit)

fruit.pop()
print("update list :", fruit)

fruit.reverse()
print("update list :", fruit)

print("multiplication on list :", fruit*2)

fruit = fruit[1:5]
print("sliced list :", fruit)


fruit.clear()
print("update list :", fruit)
