# Python program to calculate Simple Interest, Compound Interest, and Annuity Plan

# Function to calculate Simple Interest
def simple_interest(P, R, T):
    A = P * (1 + (R / 100) * T)
    return A

# Function to calculate Compound Interest
def compound_interest(P, R, n, t):
    A = P * (1 + R / n) ** (n * t)
    return A

# Function to calculate Annuity Plan
def annuity_plan(PMT, R, n, t):
    A = PMT * (((1 + R / n) ** (n * t) - 1) / (R / n))
    return A

# Display results
print("Simple Interest Amount:", simple_interest)
print("Compound Interest Amount:", compound_interest)
print("Annuity Plan Amount:", annuity_plan)
