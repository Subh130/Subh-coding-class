test_dict = {
    "id1" : {"name": ["Sara"],
             "class" : ["V"], 
             "subject_integration" : ["english, maths, science"] 
             },

    "id2" : {"name": ["David"],
             "class" : ["X"], 
             "subject_integration" : ["english, maths, science"] 
             },

    "id3" : {"name": ["Sara"],
             "class" : ["IV"], 
             "subject_integration" : ["english, maths, science"] 
             },

    "id4" : {"name": ["Surya"],
             "class" : ["V"], 
             "subject_integration" : ["english, maths, science"] 
             },

    "id5" : {"name": ["Sara"],
             "class" : ["VI"], 
             "subject_integration" : ["english, maths, science"] 
             },
    "id6" : {"name": ["Sara"],
             "class" : ["X"], 
             "subject_integration" : ["english, maths, science"] 
             },
}

print("The original dictionary : "+ str(test_dict))

K = "Sara"

res = 0 

for key in test_dict:
    if K in test_dict[key]["name"]:
        res = res + 1

print(f"Frequency of {K} is : {res}")