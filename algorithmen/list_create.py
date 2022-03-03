## how to create a list in python []


thislist= ["apple", "banane", "cherry"]
print(thislist)
# we cann print it in for schleife
# with nummerieren wir die list
i=1
for x in thislist:
    print(i,".",x)
    i=i+1
print("_________________________________")



# how to access the list items by referring to index nummber
mylist = ["zakaria", "nabhan", "student"]
# print nachname
print("nachname:",mylist[1])

# negative Indexing also rückwärts print
mylist_noten = ["4", "2", "3"]
print(mylist_noten[-1])


print("_________________________________")


#Rang of indexes
# we cann specify a rang of indexes by specifying where to start and where to end

thislist =["note1","note2", "note3", "note4", "note5"]
print(thislist[1:3])



#this example returns the itemms from the beginning to note3
thislist =["note1","note2", "note3", "note4", "note5"]
print(thislist[:3])


#in this example we start from note 4 to ende the list
thislist =["note1","note2", "note3", "note4", "note5"]
print(thislist[3:])

print("_________________________________")


# how to change a value in in the list
# to change the value of a specific item, refer to the index number

thislist =["note1","note2", "note3", "note4", "note5"]
thislist[0]="note1000"
print(thislist)

#check if item exists

thislist =["note1","note2", "note3", "note4", "note5"]
if "note1" in thislist:
    print("note existiert")
    #dann change the value
    thislist[0]="note99"
    #print the new list
    print(thislist)
    # print the lenght of the list
    print("Länge: ",len(thislist))
else:
    print("note exisiert nicht")




print("_________________________________")

# add a new item to the list
# using the append() method to append an item
thislist =["note1","note2", "note3", "note4", "note5"]
thislist.append("note6")
print(thislist)

# to add a item at the specified index, ue the insert() method:
# using the insert() methode insert(index, object)
thislist =["note1","note2", "note3", "note4", "note5"]
thislist.insert(0, "noten0")
print(thislist)

# remove item in the list using remove() method
thislist =["note1","note2", "note3", "note4", "note5"]
thislist.remove("note5")
print(thislist)
print("_________________________________")

#using pop() method to removes last item or remove the specified index
thislist =["note1","note2", "note3", "note4", "note5"]
thislist.pop()
print(thislist)

#using del method to delete  a spcified index or delete compeltey
thislist =["note1","note2", "note3", "note4", "note5"]
del thislist[0]
print(thislist)

thislist =["note1","note2", "note3", "note4", "note5"]
del thislist
print("liste wurde gelöscht")

# to clear the list we use clear() methode

thislist =["note1","note2", "note3", "note4", "note5"]
thislist.clear()
print("list ist leer", thislist)

print("_________________________________")



# how to make a copy of the list
# using copy() method or list()
thislist =["note1","note2", "note3", "note4", "note5"]
new_copy=thislist.copy()
list_copy=list(thislist)
print(new_copy)
print(list_copy)

print("_________________________________")

# join two lists

thislist =["a","b", "c", "d", "e"]
thislist2 =["1","2", "3", "4", "5"]

list3= thislist+ thislist2
print(list3)

# another way to join

thislist =["a","b", "c", "d", "e"]
thislist2 =["1","2", "3", "4", "5"]
for x in thislist2:
    thislist.append(x)
print(thislist)


# print the same value in tow list

thislist =[3,6,9,12,155,49,90,23]
thislist2 =[28,12,5,6,34,23,43,23]
thislist3=[]
for x in thislist:
    if x in thislist2:
        thislist3.append(x)
print(thislist3)


