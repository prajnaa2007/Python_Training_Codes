# tuple and set

#adding elements to tuples but as they are immutable we convert them

my_tuple =(1,2,3,4)
temp_list = list(my_tuple)
temp_list.append(6)
my_tuple = tuple(temp_list)
print(my_tuple)

#creating a set from the list of duplicates
my_list= [1,2,3,3,4,5,5,6]
my_set= set(my_list)
print(my_set)

# two sets to perform union and function
set1 = {1,2,3,4}
set2 = {4,5,6,7}
union_result = set1.union(set2)
intersection_result = set1.intersection(set2)
print(f"union_result : {union_result}")
print(f"intersection_result : {intersection_result}")

# creating a dict for students and adding a new elements
student_details = {
    "Name" : "kris",
    "Age"  :  "25",
    "subjects" : ["maths, science, english"]
}

student_details["grade"] = "A"


#replacing a element in the dict
info_dict={
    "Name" : "krish",
    "age" : "20"
 }

info_dict["age"]=18
print(info_dict)

#deleting a key from dict

student_dict ={
    "name" : "rika",
    "age"  : "26",
    "city" : "chennai"
}
del student_dict["city"]
print(student_dict)

#string formatting
str_fr={"name": "alice","age":26}
message=f"My name is {str_fr["name"]}, and I am {str_fr["age"]} years old."
print(message)
