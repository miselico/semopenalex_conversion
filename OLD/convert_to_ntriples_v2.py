import sys

import rdflib
import gzip

import rdflib.parser
import rdflib.plugin

replacements = {
    "https://semopenalex.org/authorship/": "sas/",
    "https://semopenalex.org/author/": "sa/",
    "https://semopenalex.org/work/": "sw/",
    "https://semopenalex.org/ontology/": "so/",
    "https://semopenalex.org/openaccess/": "soo/",
    "https://semopenalex.org/location/": "sl/",
    "https://semopenalex.org/source/": "ss/",
    "https://semopenalex.org/articleProcessingCharge": "sapc/",
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#type": "rdf:type",
    "https://makg.org/entity/": "me/",
    "https://semopenalex.org/countsByYear/": "sc/",
    "https://semopenalex.org/institution/": "si/",
    "http://purl.org/dc/terms/": "dc/",
    "http://prismstandard.org/namespaces/basic/2.0": "ps/",
    "https://dbpedia.org/property/": "dp/",
    "http://purl.org/spar/": "ps/",
    "http://www.w3.org/2002/07/owl#sameAs": "same",
    "http://id.nlm.nih.gov/mesh": "mesh/",
    "http://xmlns.com/foaf/0.1/": "foaf/",
    "http://www.w3.org/ns/org#memberOf": "member",
    "https://dbpedia.org/ontology/orcidId": "orid",
}


def replace_frequent(URI: str):
    for original, replacement in replacements.items():
        if URI.startswith(original):
            return replacement + URI[len(original):]
    return URI


# for file in pathlib.Path('.').glob("*.trig.gz"):
file = sys.argv[1]

assert file.endswith(".trig.gz")


class FakeStore:
    def __init__(self) -> None:
        self.context_aware = True


class TripleHandler:
    def __init__(self) -> None:
        self.store = FakeStore()
        self.identifier = "The triple handler"
    
    # The method that is called by the parser for each triple
    def triple(self, s: str, p: str, o: str):
        s_str, p_str = replace_frequent(str(s)), replace_frequent(str(p)),
        if isinstance(o, rdflib.Literal):
            print(f'<{s_str}> <{p_str}> "" .')
        else:
            o_str = replace_frequent(str(o))
            print(f"<{s_str}> <{p_str}> <{o_str}> .")
    


# output = file.parent / pathlib.Path(pathlib.Path(file.stem).stem + ".ntriples")
with gzip.open(file) as decompressed_file:

    parser = rdflib.plugin.get("trig", rdflib.parser.Parser)()

    handler = TripleHandler()
    parser.parse(decompressed_file, handler)
