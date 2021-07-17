counties = ["Saf" , "Olar" , "Pitu"]
 
for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Saf": 422829, "Olar": 463353, "Pitu": 432438}

for voters in counties_dict.values():
    print(voters)

for county, voters in counties_dict.items():
    print(county, voters)

for county in counties_dict.keys():

    print (county + "county has" + counties_dict.get(county) + "registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:

     print(county_dict['registered_voters'])


