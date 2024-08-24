""" Initialize dictionary with default values """
""" Given:

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
Expected output:

{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}"""

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

thisdict = dict.fromkeys(employees, defaults)
print(thisdict)
print(thisdict['Kelly'])
