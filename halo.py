from spartan import Spartan
from company import Company

class Halo:

    def __init__(self):
        self.vehicules = []
        self.companies = []

    def add_spartan_to_company(self,company_name, spartan_name):
      for company in self.companies:
        if(company.get_name() == company_name):
          company.add_spartan(
            Spartan(
                spartan_name
            )
          )
          return True
      return False
    
    def add_company(self,name):
      self.companies.append(
            Company(
                name
            )
        )
    
    def find_spartans_by_company(self,company_name):
      company = self.find_company_by_name(company_name)
      if(company):
        return company.get_spartans()
      return None

    def find_company_by_name(self,name):
      for company in self.companies:
        if(company.get_name() == name):
          return company
      return None
