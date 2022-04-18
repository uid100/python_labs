#!/usr/bin/env python3

# lab 8 ex 5 Employee class implementation

from Person import Person

class Employee(Person):
    def __init__(self,name,address,age,job_skills,years_worked):
        super().__init__(name,address,age)
        self._skills=job_skills
        self.years=years_worked

    def get_skills(self):
        return self._skills
    def set_skills(self,job_skills):
        self._skills=job_skills

    def get_years(self):
        return self._skills
    def set_years(self,years_worked):
        self._years=years_worked

    
    def to_string(self):
        return super().to_string() + f" {self._skills} {self.years} years"


##### Unit Test #####
if __name__=="__main__":
    TestData = ('''
        {
            "Band": [
                {
                    "name": "Steve Howe",
                    "age": 74,
                    "address": "10 Downing, London, United Kingdom",
                    "roles": "guitar (Yes)",
                    "years": 10
                },
                {
                    "name": "Eddie Van Halen",
                    "address": "1600 Pennsylvania Avenue, Washington, D.C.",
                    "age": 65,
                    "roles": "guitar (Van Halen)",
                    "years": 6
                },
                {
                    "name": "Jimi Hendrix",
                    "age": 28,
                    "address": "Yasgur's Dairy Farm, Bethel, NY",
                    "roles": "guitar (Solo)",
                    "years": 12
                },
                {
                    "name": "Eric Clapton",
                    "address": "3 Abbey Rd, London, United Kingdom",
                    "age": 76,
                    "roles": "guitar (Cream)",
                    "years": 50
                },
                {
                    "name": "Stevie Ray Vaughan",
                    "address": "1 AT&T Way, Arlington, TX",
                    "age": 46,
                    "roles": "guitar (Double Trouble)",
                    "years": 10
                }
            ]
        }
    ''')

    import json
    band = json.loads(TestData)

    for x in band['Band']:
        musician = Employee(x['name'],x['address'],x['age'],x['roles'],x['years'])
        print( musician.to_string()+"\n" )
