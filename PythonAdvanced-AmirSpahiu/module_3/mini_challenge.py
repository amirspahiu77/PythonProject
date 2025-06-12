members = ["jack", "bob", "john"]
def check(costumer): return "Discount" if costumer in members else "No discount"
print(check("bob"))