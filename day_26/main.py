import pandas as pd

student_dict = {
    "students" : ["Luis", "Ana", "Carlos", "Fernando"],
    "scores" : [65, 96, 78, 84]
}

data_frame = pd.DataFrame(student_dict)
# for (key, value) in data_frame.items():
#     print(key, value)

for (index, row) in data_frame.iterrows():
    print(row.scores)
print(data_frame)