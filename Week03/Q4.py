# Question 4 : 
mon_class = {"Loy","Joy","Roy","Simon","Zoy"}
wed_class = {"Joy","Rory","Bob","Zu"}

wed_class.add("Grace")
print("Monday Class: ", mon_class)
print("Wednesday Class: ",wed_class)

bothClasses = mon_class & wed_class
print("Attended Both Class: ", bothClasses)

allStudent = mon_class | wed_class
print("All the Student List: ",allStudent)

onlyOneCLass = mon_class ^ wed_class
print("Only One Class:", onlyOneCLass)
print("Is Monday subset of all students?", mon_class <= allStudent)