class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    [Person(data["name"], data["age"]) for data in people]

    for data in people:
        person = Person.people[data["name"]]
        spouse_name = data.get("wife") or data.get("husband")
        if spouse_name:
            if data.get("wife"):
                person.wife = Person.people.get(spouse_name)
            else:
                person.husband = Person.people.get(spouse_name)

    return list(Person.people.values())
