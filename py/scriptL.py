import csv

with open('../lib/insurance.csv', 'r') as insurance:
    reader = csv.reader(insurance)
    # Get the headers (first row of the CSV)
    headers = next(reader)
    # Initialize empty lists for each column
    age = []
    sex = []
    bmi = []
    children = []
    smoker = []
    region = []
    charges = []
    # Iterate over each row
    for row in reader:
        # Append each column to the respective list
        age.append(row[0])
        sex.append(row[1])
        bmi.append(row[2])
        children.append(row[3])
        smoker.append(row[4])
        region.append(row[5])
        charges.append(row[6])

def avg_age(age):
    """Calculate the average age."""
    total_age = sum(int(a) for a in age)
    return round(total_age / len(age), 2)

def majority_location(region):
    """Find the location with the most people."""
    from collections import Counter
    location_counts = Counter(region)
    most_common_location = location_counts.most_common(1)[0][0]
    return most_common_location.capitalize()

def charges_smokers_vs_nonsmokers(charges, smoker):
    """Compare charges between smokers and non-smokers."""
    smoker_charges = [float(c) for c, s in zip(charges, smoker) if s == 'yes']
    nonsmoker_charges = [float(c) for c, s in zip(charges, smoker) if s == 'no']
    avg_smoker_charges = round(sum(smoker_charges) / len(smoker_charges), 2)
    avg_nonsmoker_charges = round(sum(nonsmoker_charges) / len(nonsmoker_charges), 2)
    return avg_smoker_charges, avg_nonsmoker_charges

def avg_age_with_at_least_one_child(age, children):
    """Calculate the average age of people with at least one child."""
    ages_with_children = [int(a) for a, c in zip(age, children) if int(c) >= 1]
    return round(sum(ages_with_children) / len(ages_with_children), 2)
    
# Organize the output into dictionaries
results = {}

results['Average age'] = avg_age(age)
results['Majority location'] = majority_location(region)
results['Average charges (smokers vs non-smokers)'] = charges_smokers_vs_nonsmokers(charges, smoker)
results['Average age of people with at least one child'] = avg_age_with_at_least_one_child(age, children)

# Print the results
for key, value in results.items():
    print(key + ':', value)