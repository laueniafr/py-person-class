class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None

        Person.people[name] = self


def create_person_list(data_list: list) -> list:
    # Cria todas as pessoas
    [Person(data.get("name"), data.get("age")) for data in data_list]

    # Relaciona cônjuges
    for data in data_list:
        person = Person.people.get(data.get("name"))
        wife_name = data.get("wife")
        husband_name = data.get("husband")

        if wife_name:
            person.wife = Person.people.get(wife_name)
        if husband_name:
            person.husband = Person.people.get(husband_name)

    # Retorna a lista de objetos Person na mesma ordem
    return [Person.people.get(data.get("name")) for data in data_list]
