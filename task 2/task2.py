
def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            cats = []
            for line in file:
                line = line.strip()
                cat_id, cat_name, cat_age = line.split(",") 
            
                cats_info = {"id": cat_id, "name": cat_name, "age": cat_age}
                cats.append(cats_info)
        return cats
    except FileNotFoundError:
        print("File Not Found!")

cats = get_cats_info("task 2/info_cat_file.txt")
for cat in cats:
    print(cat)