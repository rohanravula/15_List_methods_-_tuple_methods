"""List methods"""

# a=[3,5.7,"Rohan",[10,29.83]]
# a.append(2)
# print(a) #[3,5.7,'Rohan',[10,29.83],2] #append which means it will add the element at the end of the list.
# a.append(2,6) #Error . by using append we can only add single element at the end of the list. we cant add dubble elements.

# b=[3,1.9,"python",[10,7.5]]
# b.clear()
# print(b) #[]. by using the clear method the  all elements will be cleared and the output will be empty sq. bracket i.e, []. in list we can represent the empty list also.

# x=[10,2.4,"kumar",[20,30]]
# print(x)
# b=x.copy()
# print(b) #[10,2.4,"kumar",[20,30]]. copy which means the same thing again it will be get copied in the output.

# c=[10,9,10,2.6,"Rohan",[20,30],""]
# print(c.count(9)) #1
# print(c.count(10)) #2
# print(c.count(20)) #0. coz in list another list is there naa so it shows 0.
# print(c.count("")) #1
# print(c.count(50)) #0 .the count method is used to check in the list that how many times the element repeating . if it is not repeating then it shows 0.if it is repaeating it shows ceratain number that how many times it is repeating.

# a=[1,2,3]
# b=[4,3,5]
# # a.extend(b)
# # print(a) #[1,2,3,4,3,5] .hence the the b is getting merged with a.
# b.extend(a)
# print(b) #[4,3,5,1,2,3] . Hence the a is getting merged with b. extend which means to adding multiple elements in list or merging two elements into one list.

# y=[9,5.6,78,"hello",[44]]
# print(y.index(9)) #0
# print(y.index(78)) #2
# print(y.index("hello")) #3
# print(y.index([44])) #4. Index methods tell about the postion of the element in the list.
# print(y.index(90)) #ValueError:90 is not in list. if the element is not there in the list then it shows the error.
# print(y.index([4])) #valueError: 4 is not in list.

# z=[2,3,4,"python",3.5]
# z.insert(2,"hello") #[2,3,'hello',4,'python',3.5]
# print(z)
# z.insert(-2,"world")
# print(z) #[2,3,4,'world','python',3.5]. by using the method insert we can add the element at which positon we want in the list.

# r=[10,20,30,40,50]
# r.pop()
# print(r) #[10,20,30,40]. pop is method to remove the element.if we not mention any index number in pop so then the last element will be get removed.
# r.pop(3) #[10,20,30,50]. if we mention the index number then that element will be removed.
# print(r)
# print(r.pop()) #50. to weather which element is getting removed the use this line.

# m=[50,30,20,"hello","python",66.9]
# m.remove("python")
# print(m) #[50,30,20,'hello',66.9]. this is the another method to remove the element, if we dont know the index position then use the remove method then thecertain element will get removed.

# n=[10,20,30,"python",50,60] #if we want to print the list elements in reverse order then the method is called reverse. in list we can print in reverse order by using the slicing method also.
# print(n[::-1]) #[60,50,'python',30,20,10]. this method is slicing.
# n.reverse()
# print(n)

# g=[10,40,20,60,90]
# g.sort()
# print(g) #[10,20,40,60,90]. by default the sort prints in assending order only .
# g.sort(reverse=False) #[10,20,40,60,90]. this is the another way to print in assending order
# print(g)
# g.sort(reverse=True) #[90,60,40,20,10]. by using this method we can do the decending order.for printing the decending order their is only one method.
# print(g)
"if they give the alpalbets words to sort. then first it will print upper case alaphebets aand then it will  print lower case alpehebets as assending order coz of ASCI vlaues"
# h=['HD','SM','G','K','FD','n','z','A']
# h.sort()
# print(h) #['A', 'FD', 'G', 'HD', 'K', 'SM', 'n', 'z']



"""Methods in Tuple"""
# a=(1,)
# print(a,type(a))# (1,) tuple. a value with a comma (,) then it is called as tuple.

# pr=('rohan','mohan','dhanveet','manoj')
# pr[1]='vamshi' #TypeError:'tuple' object doesnot support item assignment. coz the tuple cant be modified.

# n="hello","rohan"
# print(n,type(n)) #('hello','rohan') , tuple
# print(n[1]) #rohan . coz at the index postion 1 rohan is there so it shows rohan.
# print(n[2]) #IndexError:tuple index out of range.

# a=(4,5,8,"python",[7.8,7],7,8)
# print(a.count(7)) #1
# print(a.count(8)) #2. this method is known as count which tell the how many times the element is repeating


b=("mohan",3,45,5.7,"rohan")
print(b.index("rohan")) #4