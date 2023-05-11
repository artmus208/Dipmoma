from os import path
p =  "D:\\semester8\\Diploma\\app\\static/data/uploads\\data\\time_value_3.txt"
abs_path = path.abspath(p)
base_name = path.basename(p)
dirname = path.dirname(p)
splited_path = path.split(p)
print(f"p: {p}")
print(f"abs_path: {abs_path}")
print(f"basename: {base_name}")
print(f"dirname: {dirname}")
print(f"splited_path:\n{splited_path}")

