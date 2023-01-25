# create the initial variables below
age = 28
sex = 0 # 0 if female 1 if male
bmi = 26.2
num_of_children = 3
smoker = 0 # 1 if smoker 0 if not smoker

# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 125000

# print out the insurance cost
print("This person's insurance cost is" + str(insurance_cost) + " dollars.")

# Age Factor
age += 4

# calculate new insurance cost
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 125000

# calculate change between the new insurance cost and original insurance cost
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.")

# BMI Factor
age = 28

# add 3.1 to bmi
bmi += 3.1

# calculate the new insurance cost
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
# calculate change between the new insurance cost and original insurance cost
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars.")

# rewrite bmi as original value
bmi = 26.2

# male vs. female factor
# change value of sex to 1
sex = 1

# calculate the new insurance cost
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
# calculate change between the new insurance cost and original insurance cost
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars.")


# Extra Practice