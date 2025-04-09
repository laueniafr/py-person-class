class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    for data in people:
        Person(data["name"], data["age"])

    for data in people:
        person = Person.people[data["name"]]
        if "wife" in data and data["wife"]:
            person.wife = Person.people.get(data["wife"])
        elif "husband" in data and data["husband"]:
            person.husband = Person.people.get(data["husband"])

    return list(Person.people.values())
