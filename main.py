from halo import Halo
from register_spartans import  RegisterSpartans

halo = Halo()

counter = 0
for item in ['Test','Example']:
    halo.add_company(item)
    for s_name in ['Red', 'Blue','Purple']:
        halo.add_spartan_to_company(
            halo.companies[counter].get_name(),
            s_name
            )
    counter+=1

halo.add_spartan_to_company('Example','Grean')

company =  halo.find_company_by_name('Example')

if(company): # True|False -- AlgoDeclarado|None
    company.get_name()
else:
    print('No existe')

for spartan in halo.find_spartans_by_company('Example'):
    print(spartan.get_name())

for company in halo.companies:
    register = RegisterSpartans(
        company,
        "files/companies/"+company.get_name()
    )
    register.save()