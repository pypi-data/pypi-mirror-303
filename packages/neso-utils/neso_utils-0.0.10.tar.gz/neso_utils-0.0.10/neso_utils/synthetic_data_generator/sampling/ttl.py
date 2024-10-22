# script responsible for the sampling of ttl files

from typing import Union

from rdflib import Graph
from rdflib import Literal
from rdflib import URIRef
from rdflib import BNode

from ..utils.triples import generate_unique_values


class TTLSampling:

    @staticmethod
    def _check_triples_lst(triples_lst: list[tuple]) -> Union[bool, Exception]:
        """
        Check if the provided list of triples is valid.

        Args:
            triples_lst (list[tuple]): a list of tuples representing the triplets

        Returns:
            bool: True if the list of triples is valid, False otherwise
        """

        if all(
            isinstance(s, URIRef) and isinstance(p, URIRef) and isinstance(o, (URIRef, Literal, BNode))
            for s, p, o in triples_lst
        ):

            return True

        else:
            raise Exception("Invalid list of triples! Check the provided list of triples.")

    @staticmethod
    def scale_ttl_file(graph: Graph, current_size_mb: float, target_size_mb: float) -> Graph:
        """
        Scale out a ttl file with a specific size.

        This method will concatenate the ttl file provided until the target size is reached.

        Args:
            graph (Graph): a rdflib Graph object with the ttl file that will be scaled
            current_size_mb (float): the current size of the file in MB
            target_size_mb (float): the target size of the file in MB

        Returns:
            Graph: a rdflib Graph object with the concatenated ttl file
        """

        for triple in generate_unique_values(int(target_size_mb // current_size_mb)):
            graph.add(triple)

        return graph

    @staticmethod
    def sample_ttl_file(records_num: int):
        """
        Create a sample ttl file from a list of triplets.

        Args:
            records_num (int): the number of records that will be sampled

        Returns:
            ttl file stored in the provided path
        """

        graph = Graph()

        for s, p, o in generate_unique_values(records_num):
            graph.add((URIRef(s), URIRef(p), URIRef(o)))

        return graph

    @staticmethod
    def load_ttl_file(file_path: str) -> Graph:
        """
        Load a ttl file.

        Args:
            file_path (str): path to the file that will be loaded

        Returns:
            Graph: a rdflib Graph object with the loaded ttl file
        """

        return Graph().parse(file_path, format="turtle")
