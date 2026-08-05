
def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                name, salary = line.split(",")
                salary = int(salary)

                total += salary
                count += 1

        average = total / count
        return total, average

    except FileNotFoundError:
            print("File Not Found!")


print(total_salary("task 1/salary_file.txt"))

