from unittest import TestCase

from entityshape import Result


class TestResult(TestCase):
    """TODO add more tests based on another item validation json"""

    hiking_path_with_1_missing_required_property = {
        "error": "",
        "general": {},
        "name": "hiking path",
        "properties": {
            "P10467": {
                "name": "naturkartan.se ID",
                "necessity": "optional",
                "response": "missing",
            },
            "P112": {
                "name": "founded by",
                "necessity": "optional",
                "response": "missing",
            },
            "P131": {
                "name": "located in the administrative territorial entity",
                "necessity": "required",
                "response": "present",
            },
            "P1343": {
                "name": "described by source",
                "necessity": "optional",
                "response": "missing",
            },
            "P137": {
                "name": "operator",
                "necessity": "optional",
                "response": "missing",
            },
            "P138": {
                "name": "named after",
                "necessity": "optional",
                "response": "missing",
            },
            "P1427": {
                "name": "start point",
                "necessity": "optional",
                "response": "missing",
            },
            "P1444": {
                "name": "destination point",
                "necessity": "optional",
                "response": "missing",
            },
            "P15": {
                "name": "route map",
                "necessity": "optional",
                "response": "missing",
            },
            "P1545": {
                "name": "series ordinal",
                "necessity": "optional",
                "response": "missing",
            },
            "P1552": {
                "name": "has quality",
                "necessity": "optional",
                "response": "missing",
            },
            "P1589": {
                "name": "lowest point",
                "necessity": "optional",
                "response": "missing",
            },
            "P17": {"name": "country", "necessity": "required", "response": "present"},
            "P18": {"name": "image", "necessity": "optional", "response": "missing"},
            "P1997": {
                "name": "Facebook Places ID",
                "necessity": "optional",
                "response": "missing",
            },
            "P2043": {"name": "length", "necessity": "required", "response": "missing"},
            "P206": {
                "name": "located in or next to body of water",
                "necessity": "optional",
                "response": "missing",
            },
            "P214": {"name": "VIAF ID", "necessity": "optional", "response": "missing"},
            "P2347": {"name": "YSO ID", "necessity": "optional", "response": "missing"},
            "P242": {
                "name": "locator map image",
                "necessity": "optional",
                "response": "missing",
            },
            "P2671": {
                "name": "Google Knowledge Graph ID",
                "necessity": "optional",
                "response": "missing",
            },
            "P2789": {
                "name": "connects with",
                "necessity": "optional",
                "response": "missing",
            },
            "P30": {
                "name": "continent",
                "necessity": "optional",
                "response": "missing",
            },
            "P3018": {
                "name": "located in protected area",
                "necessity": "optional",
                "response": "missing",
            },
            "P31": {
                "name": "instance of",
                "necessity": "optional",
                "response": "correct",
            },
            "P3173": {
                "name": "offers view on",
                "necessity": "optional",
                "response": "missing",
            },
            "P361": {"name": "part of", "necessity": "optional", "response": "missing"},
            "P373": {
                "name": "Commons category",
                "necessity": "optional",
                "response": "missing",
            },
            "P402": {
                "name": "OpenStreetMap relation ID",
                "necessity": "optional",
                "response": "missing",
            },
            "P4552": {
                "name": "mountain range",
                "necessity": "optional",
                "response": "missing",
            },
            "P527": {
                "name": "has part(s)",
                "necessity": "optional",
                "response": "missing",
            },
            "P559": {
                "name": "terminus",
                "necessity": "optional",
                "response": "missing",
            },
            "P571": {
                "name": "inception",
                "necessity": "optional",
                "response": "missing",
            },
            "P609": {
                "name": "terminus location",
                "necessity": "optional",
                "response": "missing",
            },
            "P610": {
                "name": "highest point",
                "necessity": "optional",
                "response": "missing",
            },
            "P6104": {
                "name": "maintained by WikiProject",
                "necessity": "optional",
                "response": "missing",
            },
            "P625": {
                "name": "coordinate location",
                "necessity": "absent",
                "response": "missing",
            },
            "P646": {
                "name": "Freebase ID",
                "necessity": "optional",
                "response": "missing",
            },
            "P691": {
                "name": "NL CR AUT ID",
                "necessity": "optional",
                "response": "missing",
            },
            "P706": {
                "name": "located in/on physical feature",
                "necessity": "optional",
                "response": "missing",
            },
            "P7127": {
                "name": "AllTrails trail ID",
                "necessity": "optional",
                "response": "missing",
            },
            "P7252": {
                "name": "degree of difficulty",
                "necessity": "optional",
                "response": "missing",
            },
            "P856": {
                "name": "official website",
                "necessity": "optional",
                "response": "missing",
            },
            "P910": {
                "name": "topic's main category",
                "necessity": "optional",
                "response": "missing",
            },
            "P973": {
                "name": "described at URL",
                "necessity": "optional",
                "response": "present",
            },
        },
        "schema": "E375",
        "statements": {
            "Q119845590$11794598-A67C-4978-8D1D-359B90E5EE15": {
                "necessity": "optional",
                "property": "P973",
                "response": "allowed",
            },
            "Q119845590$1CEFCE58-826A-4243-A9D2-CF47BF9F493E": {
                "necessity": "required",
                "property": "P131",
                "response": "allowed",
            },
            "Q119845590$72CEF06C-C5AE-40DE-AB61-D530914AFD4E": {
                "necessity": "optional",
                "property": "P31",
                "response": "correct",
            },
            "Q119845590$9C7FBBB4-7302-423F-AF51-C46A07F680CD": {
                "necessity": "required",
                "property": "P131",
                "response": "allowed",
            },
            "Q119845590$D036FE30-1DFD-461A-8AA2-AA0CB977E22D": {
                "necessity": "required",
                "property": "P17",
                "response": "allowed",
            },
        },
        "validity": {},
    }
    campsite_missing_correct_p31 = {'error': '', 'general': {}, 'name': 'campsite', 'properties': {'P10467': {'name': 'naturkartan.se ID', 'necessity': 'optional', 'response': 'missing'}, 'P11177': {'name': 'Camp Wild ID', 'necessity': 'optional', 'response': 'missing'}, 'P131': {'name': 'located in the administrative territorial entity', 'necessity': 'required', 'response': 'present'}, 'P137': {'name': 'operator', 'necessity': 'required', 'response': 'present'}, 'P138': {'name': 'named after', 'necessity': 'optional', 'response': 'missing'}, 'P1448': {'name': 'official name', 'necessity': 'optional', 'response': 'missing'}, 'P17': {'name': 'country', 'necessity': 'required', 'response': 'present'}, 'P18': {'name': 'image', 'necessity': 'optional', 'response': 'missing'}, 'P206': {'name': 'located in or next to body of water', 'necessity': 'optional', 'response': 'missing'}, 'P242': {'name': 'locator map image', 'necessity': 'optional', 'response': 'missing'}, 'P2670': {'name': 'has part(s) of the class', 'necessity': 'optional', 'response': 'missing'}, 'P276': {'name': 'location', 'necessity': 'optional', 'response': 'present'}, 'P30': {'name': 'continent', 'necessity': 'optional', 'response': 'missing'}, 'P3018': {'name': 'located in protected area', 'necessity': 'optional', 'response': 'missing'}, 'P31': {'name': 'instance of', 'necessity': 'required', 'response': 'not enough correct statements'}, 'P3173': {'name': 'offers view on', 'necessity': 'optional', 'response': 'missing'}, 'P373': {'name': 'Commons category', 'necessity': 'optional', 'response': 'missing'}, 'P402': {'name': 'OpenStreetMap relation ID', 'necessity': 'optional', 'response': 'missing'}, 'P4552': {'name': 'mountain range', 'necessity': 'optional', 'response': 'missing'}, 'P527': {'name': 'has part(s)', 'necessity': 'optional', 'response': 'missing'}, 'P571': {'name': 'inception', 'necessity': 'optional', 'response': 'missing'}, 'P5775': {'name': 'image of interior', 'necessity': 'absent', 'response': 'missing'}, 'P625': {'name': 'coordinate location', 'necessity': 'required', 'response': 'present'}, 'P706': {'name': 'located in/on physical feature', 'necessity': 'optional', 'response': 'missing'}, 'P7418': {'name': 'image of frontside', 'necessity': 'optional', 'response': 'missing'}, 'P8517': {'name': 'view', 'necessity': 'optional', 'response': 'missing'}, 'P856': {'name': 'official website', 'necessity': 'optional', 'response': 'missing'}, 'P912': {'name': 'has facility', 'necessity': 'optional', 'response': 'missing'}, 'P9676': {'name': 'Vindskyddskartan.se ID', 'necessity': 'optional', 'response': 'missing'}, 'P973': {'name': 'described at URL', 'necessity': 'optional', 'response': 'present'}}, 'schema': 'E376', 'statements': {'Q119853974$20823AE2-6F1A-43FB-9C9C-A6C2CC772446': {'necessity': 'required', 'property': 'P137', 'response': 'allowed'}, 'Q119853974$3F1F91A9-693C-41AA-A5C7-54E711D83594': {'necessity': 'required', 'property': 'P17', 'response': 'allowed'}, 'Q119853974$4A29484F-6C84-4B5A-B9E9-25344162CFCB': {'necessity': 'required', 'property': 'P625', 'response': 'allowed'}, 'Q119853974$4BCAA6A7-8857-4056-B286-7B646A2D72C9': {'necessity': 'required', 'property': 'P131', 'response': 'allowed'}, 'Q119853974$8E8612BE-78F7-463A-8E35-96F53277E3B4': {'necessity': 'optional', 'property': 'P276', 'response': 'allowed'}, 'Q119853974$AA270DBF-B117-45DD-AF68-8F1A7AFC56F1': {'necessity': 'required', 'property': 'P31', 'response': 'allowed'}, 'Q119853974$C25AF244-F0D9-4E19-8126-42092C0FA4FB': {'necessity': 'optional', 'property': 'P973', 'response': 'allowed'}, 'Q119853974$CD71CE83-F045-486B-873F-F7A8FB437E2A': {'necessity': 'required', 'property': 'P131', 'response': 'allowed'}}, 'validity': {}}


    def setUp(self) -> None:
        self.hiking_path_result = Result(
            **self.hiking_path_with_1_missing_required_property
        )
        self.hiking_path_result.analyze()
        self.campsite_result = Result(
            **self.campsite_missing_correct_p31
        )
        self.campsite_result.analyze()

    def test___find_properties_with_too_many_statements__zero(self):
        assert len(self.hiking_path_result.properties_with_too_many_statements) == 0

    def test__find_required_properties__three(self):
        assert len(self.hiking_path_result.required_properties) == 3

    def test__find_missing_properties__(self):
        assert len(self.hiking_path_result.missing_properties) == 41

    def test__find_required_properties_that_are_missing__(self):
        assert len(self.hiking_path_result.required_properties_that_are_missing) == 1

    def test__find_optional_properties_that_are_missing__(self):
        assert len(self.hiking_path_result.optional_properties_that_are_missing) == 40

    def test____find_incorrect_statements__(self):
        assert len(self.hiking_path_result.incorrect_statements) == 0

    def test__find_properties_with_not_enough_correct_statements__(self):
        assert len(self.campsite_result.properties_without_enough_correct_statements) == 1