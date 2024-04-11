import os

def read_medicines(filename):
    medicines = {}
    with open(filename, 'r') as file:
        for line in file:
            med_id, name, price, expiry_date, company = line.strip().split(',')
            medicines[med_id] = {'name': name, 'price': float(price), 'expiry_date': expiry_date, 'company': company}
    return medicines

def write_medicines(filename, medicines):
    with open(filename, 'w') as file:
        for med_id, details in medicines.items():
            file.write(f"{med_id},{details['name']},{details['price']},{details['expiry_date']},{details['company']}\n")

def sort_medicines_by_price(medicines):
    return sorted(medicines.items(), key=lambda x: x[1]['price'])

def remove_duplicates(medicines):
    unique_medicines = {}
    for med_id, details in medicines.items():
        if details not in unique_medicines.values():
            unique_medicines[med_id] = details
    return unique_medicines

def top_selling_medicines(medicines):
    sorted_medicines = sorted(medicines.items(), key=lambda x: x[1]['price'], reverse=True)
    top_3 = sorted_medicines[:3]
    return top_3

def main():
    filename = "medicines.txt"

    # Check if file exists, if not create it
    if not os.path.exists(filename):
        open(filename, 'w').close()

    medicines = read_medicines(filename)

    # a) Arrange the medicine in Ascending order by price
    sorted_medicines = sort_medicines_by_price(medicines)
    print("Medicines in Ascending order by price:")
    for med_id, details in sorted_medicines:
        print(f"{med_id}: {details}")

    # b) Remove duplicate medicines
    unique_medicines = remove_duplicates(medicines)
    print("\nMedicines after removing duplicates:")
    for med_id, details in unique_medicines.items():
        print(f"{med_id}: {details}")

    # c) Display each medicine {id: name, price, expiry date, company name}
    print("\nMedicines details:")
    for med_id, details in medicines.items():
        print(f"{med_id}: {details}")

    # d) If new medicine is bought, do possible arrangements by searching the previous one
    # Assume new_medicine is a dictionary containing details of the new medicine
    # medicines[new_med_id] = new_medicine

    # e) Find out the top 3 selling medicines
    top_3 = top_selling_medicines(medicines)
    print("\nTop 3 selling medicines:")
    for med_id, details in top_3:
        print(f"{med_id}: {details}")

if __name__ == "__main__":
    main()
