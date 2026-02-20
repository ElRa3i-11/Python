from tabulate import tabulate

# assign data
a = [
    ["d","Nikhil", "Delhi"],
    ["a","Ravi", "Kanpur"],
    ["b","Manish", "Ahmedabad"],
    ["c","Prince", "Bangalore"]
]

# create header
headers = ["Name", "City",]

print(tabulate(a, headers=headers, tablefmt="simple"))
