names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul", "Priscilla"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0, 8320.0]

medical_records = list(zip(insurance_costs, names))

num_medical_records = len(medical_records)

first_medical_record = medical_records[0]

medical_records.sort()

cheapest_three = medical_records[:3]

priciest_three = medical_records[-3:]

occurances_paul = names.count("Paul")

print("There are " + str(num_medical_records) + " medical records.")

print("Here is the first medical record: " + str(first_medical_record) + ".")

print("Here are the medical records sorted by insurance cost: " + str(medical_records) + ".")

print("Here are the three cheapest insurance costs in our medical records: " + str(cheapest_three) + ".")

print("Here are the three most expensive insurance costs in our medical records: " + str(priciest_three) + ".")

print("There are " + str(occurances_paul) + " individuals with the name Paul in our medical records.")