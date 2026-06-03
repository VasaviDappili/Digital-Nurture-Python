# Exercise 36 - Set Intersection

def common_skills(set1, set2):

    common = set1 & set2

    print("Common Skills:", common)


skills1 = {"Python", "Java", "SQL"}
skills2 = {"Python", "C++", "SQL"}

common_skills(skills1, skills2)