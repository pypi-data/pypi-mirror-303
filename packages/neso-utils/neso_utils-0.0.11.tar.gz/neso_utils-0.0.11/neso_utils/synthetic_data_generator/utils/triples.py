# auxiliar operations on triples

import random
import randomname

from rdflib import URIRef, Literal
from rdflib.namespace import FOAF


def generate_unique_values(triples_num: int = 1) -> list[tuple[str, str, str]]:
    """
    Generate a list of 3 unique triples.

    Args:
        triples_num (int): the number of triples to generate

    Returns:
        list[tuple[str, str, str]]: a list of tuples with unique values
    """

    triples_lst = []

    for _ in range(triples_num):
        name = randomname.get_name().replace("-", "_")
        gender = random.choice(["male", "female"])
        age = random.randint(18, 60)

        triples_lst.append((URIRef(name), FOAF.nick, FOAF.Person))
        triples_lst.append((URIRef(name), FOAF.gender, URIRef(gender)))
        triples_lst.append((URIRef(name), FOAF.age, Literal(age)))

    return triples_lst
