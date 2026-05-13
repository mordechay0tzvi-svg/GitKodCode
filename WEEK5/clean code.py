#targil1
def f(original_names_list):
    above18_active = []
    for name in original_names_list:
        if name[1] >= 18 and name[2]:
            above18_active.append(name[0])
    return above18_active

d = [
    ["Dan", 25, True],
    ["Noa", 16, True],
    ["Yael", 30, False],
]

print(f(d))


#targil2
def check_email(user_email):
    return user_email

def is_invalid_quantity(quantity, stock):
    return quantity <= 0 or quantity > stock

def price_definer(product_price, quantity):
    price = product_price * quantity
    if quantity >= 10:
        price *= 0.9
    if quantity >= 50:
        price *= 0.85
    return price

def print_invoice(order_user, order_product, order_quantity, order_total, order_status):
    print(f"Order {order_status}: {order_user} bought {order_quantity}x {order_product} for ${order_total}")

def handle_purchase(user_email, product_name, product_price, stock, quantity):
    if not check_email(user_email):
        print("Invalid user")
        return None

    if is_invalid_quantity(quantity, stock):
        print("Invalid quantity")
        return None

    price = price_definer(product_price, quantity)
    stock -= quantity
    order_user = user_email
    order_product = product_name
    order_quantity = quantity
    order_total = price
    order_status = "confirmed"
    print_invoice(order_user, order_product, order_quantity, order_total, order_status)
    return order_user, order_product, order_quantity, order_total, order_status


#targil3
def check_name(new_name):
    return not new_name or len(new_name) < 2

def check_grade(new_grade):
    return new_grade >= 0 or new_grade <= 100

def print_report(names, grades, top_count, failing_count, average):
    print("=== Student Report ===")
    for index in range(len(names)):
        print(f"  {names[index]}: {grades[index]}")
    print(f"Average: {average:.1f}")
    print(f"Top students: {top_count}")
    print(f"Failing: {failing_count}")

def save_to_file(names, grades):
    with open("students.txt", "w") as file:
        for i in range(len(names)):
            file.write(f"{names[i]},{grades[i]}\n")

def manage_students(names, grades, new_name, new_grade):
    # validation
    if check_name(new_name):
        print("Error: invalid name")
        return students

    if not check_grade(new_grade):
        print("Error: grade must be 0-100")
        return students

    # add student
    grades.append(new_grade)

    # calculate stats
    total = sum(grades)
    average = total / len(grades)
    top_count = sum(1 for grade in grades if grade >= 90)
    failing_count = sum(1 for grade in grades if grade < 56)

    # print report
    print_report(names, grades, top_count, failing_count, average)

    # save to file
    save_to_file(names, grades)

    return names, grades


#targil4
def not_valid_name(name):
    return not name or len(name) < 2

def not_valid_email(email):
    return "@" not in email

def get_date():
    return datetime.date.today()

def create_user(name, email, permission_level):
    if not_valid_name(name):
        raise ValueError("Invalid name")

    if  not_valid_email(email):
        raise ValueError("Invalid email")

    date_of_log = get_date()

    return f"{name}, {email}, {permission_level}, {date_of_log}, {True}"



#targil5
def get_status(score):
    if score >= 90:
        status = "excellent"
    elif score >= 70:
        status = "good"
    elif score >= 55:
        status = "average"
    else:
        status = "fail"
    return status


def is_valid_age(age):
    if isinstance(age, int) and 0 < age < 120:
        return True
    return False


def get_greeting(hour):
    greeting = greeting = "Good morning"
    if 17 > hour >= 12 :
        greeting = "Good afternoon"
    if 21 > hour >= 17 :
        greeting = "Good evening"
    if 5 > hour >= 21:
        greeting = "Good night"
    return greeting



#targil6
def print_processed_report(result_names, result_averages, result_statuses, result_lows, result_highs):
    print("=" * 40)
    print("Student Grade Report")
    print("=" * 40)
    for i in range(len(result_names)):
        print(f"Name: {result_names[i]}")
        print(f"  Average: {result_averages[i]}")
        print(f"  Status: {result_statuses[i]}")
        print(f"  Range: {result_lows[i]} - {result_highs[i]}")
        print()

def is_valid_name(name):
    return name and len(name) > 2

def is_valid_garde(grade):
    return 100 >= grade >= 0


def calculate_students_stats(names, all_grades):
    result_names = []
    result_averages = []
    result_statuses = []
    result_highs = []
    result_lows = []
    for i in range(len(names)):
        name = names[i]
        grades = all_grades[i]
        if not is_valid_name(name):
            print(f"Error: missing name")
            continue
        if not is_valid_garde(grade):
            print(f"Error: {name} has no grades")
            continue
        total = sum(grades)
        average = total / len(grades)
        status = "pass" if average >= 56 else "fail"
        highest = max(grades)
        lowest = min(grades)

        result_names.append(name)
        result_averages.append(round(average, 1))
        result_statuses.append(status)
        result_highs.append(highest)
        result_lows.append(lowest)
    return result_names, result_averages, result_statuses, result_highs, result_lows


def process_grades(names, all_grades):
    result_names, result_averages, result_statuses,result_highs, result_lows  = calculate_students_stats(names, all_grades)
    print_report(result_names, result_averages, result_statuses, result_lows, result_highs)
    passing_count = sum(1 for s in result_statuses if s == "pass")
    print(f"Total passing: {passing_count}/{len(result_names)}")
    return result_names, result_averages, result_statuses



#targil7
TAX = 0.17

def process_cart(prices, quantities, user_type):
  total = 0

  for i in range(len(prices)):
    price = prices[i]
    quantity = quantities[i]
    total = total + price * quantity
  # add tax
  total = total + total * TAX
  if user_type == 'premium':
    total = total * 0.9
  elif user_type == 'vip':
    total = total * 0.8
  if total > 500:
    shipping = 0
  elif total > 200:
    shipping = 25
  else:
    shipping = 50
  total = total + shipping
  return total

