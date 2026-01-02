class Person:
    first_name: str
    last_name: str

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name


def convert_list_to_string(people: list[Person]) -> str:
    """
    Convert a list of Person objects to a string representation.

    Args:
        people (list[Person]): A list of Person objects.

    Returns:
        str | None: A string representation of the list of Person objects. Returns None if the list is empty.
    """

    if len(people) == 0:
        return "No people available."

    return ", ".join(f"{person.first_name} {person.last_name}" for person in people)


def main() -> None:
    people = [
        Person(first_name="John", last_name="Doe"),
        Person(first_name="Jane", last_name="Smith")
    ]
    print(convert_list_to_string(people))


if __name__ == "__main__":
    main()
