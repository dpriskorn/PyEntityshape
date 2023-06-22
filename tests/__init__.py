from unittest import TestCase

from entityshape import EntityShape


class TestEntityShape(TestCase):
    def test_get_result_invalid_eid(self):
        e = EntityShape(eid="eeeE1", lang="en", qid="Q1")
        e.get_result()
        print(e.result)
        # assert e.result != {}

    def test_get_result_invalid_lang(self):
        e = EntityShape(eid="E1", lang="eeeeen", qid="Q1")
        e.get_result()
        print(e.result)
        # assert e.result != {}

    def test_get_result_invalid_qid(self):
        e = EntityShape(eid="E1", lang="en", qid="qqqqQ1")
        e.get_result()
        print(e.result)
        # assert e.result != {}

    def test_get_result_valid(self):
        e = EntityShape(eid="E1", lang="en", qid="Q1")
        e.get_result()
        assert e.result != {}
        assert e.result["properties"] == {
            "P10": {"name": "video", "necessity": "absent"},
            "P10242": {"name": "Lur Encyclopedic Dictionary ID", "necessity": "absent"},
            "P10283": {"name": "OpenAlex ID", "necessity": "absent"},
            "P1036": {"name": "Dewey Decimal Classification", "necessity": "absent"},
            "P1051": {"name": "PSH ID", "necessity": "absent"},
            "P10757": {
                "name": "Personality Database profile ID",
                "necessity": "absent",
            },
            "P11196": {"name": "Baidu Tieba name", "necessity": "absent"},
            "P11408": {"name": "Pixiv Encyclopedia ID", "necessity": "absent"},
            "P1245": {"name": "OmegaWiki Defined Meaning", "necessity": "absent"},
            "P1256": {"name": "Iconclass notation", "necessity": "absent"},
            "P1296": {"name": "Gran Enciclopèdia Catalana ID", "necessity": "absent"},
            "P1343": {"name": "described by source", "necessity": "absent"},
            "P1417": {
                "name": "Encyclopædia Britannica Online ID",
                "necessity": "absent",
            },
            "P1419": {"name": "shape", "necessity": "absent"},
            "P1424": {"name": "topic's main template", "necessity": "absent"},
            "P1482": {"name": "Stack Exchange tag", "necessity": "absent"},
            "P1552": {"name": "has quality", "necessity": "absent"},
            "P1617": {"name": "BBC Things ID", "necessity": "absent"},
            "P1711": {
                "name": "British Museum person or institution ID",
                "necessity": "absent",
            },
            "P18": {"name": "image", "necessity": "absent"},
            "P1889": {"name": "different from", "necessity": "absent"},
            "P1953": {"name": "Discogs artist ID", "necessity": "absent"},
            "P2163": {"name": "FAST ID", "necessity": "absent"},
            "P2184": {"name": "history of topic", "necessity": "absent"},
            "P227": {"name": "GND ID", "necessity": "absent"},
            "P2347": {"name": "YSO ID", "necessity": "absent"},
            "P2386": {"name": "diameter", "necessity": "absent"},
            "P244": {"name": "Library of Congress authority ID", "necessity": "absent"},
            "P2579": {"name": "studied by", "necessity": "absent"},
            "P2581": {"name": "BabelNet ID", "necessity": "absent"},
            "P2612": {"name": "TED topic ID", "necessity": "absent"},
            "P2670": {"name": "has part(s) of the class", "necessity": "absent"},
            "P268": {
                "name": "Bibliothèque nationale de France ID",
                "necessity": "absent",
            },
            "P2924": {
                "name": "Great Russian Encyclopedia Online ID (old " "version)",
                "necessity": "absent",
            },
            "P31": {"name": "instance of", "necessity": "absent"},
            "P3113": {"name": "does not have part", "necessity": "absent"},
            "P3219": {"name": "Encyclopædia Universalis ID", "necessity": "absent"},
            "P3222": {"name": "NE.se ID", "necessity": "absent"},
            "P3365": {"name": "Treccani ID", "necessity": "absent"},
            "P3417": {"name": "Quora topic ID", "necessity": "absent"},
            "P349": {"name": "NDL Authority ID", "necessity": "absent"},
            "P3553": {"name": "Zhihu topic ID", "necessity": "absent"},
            "P3569": {"name": "Cultureel Woordenboek ID", "necessity": "absent"},
            "P361": {"name": "part of", "necessity": "absent"},
            "P373": {"name": "Commons category", "necessity": "absent"},
            "P3847": {"name": "Open Library subject ID", "necessity": "absent"},
            "P3916": {"name": "UNESCO Thesaurus ID", "necessity": "absent"},
            "P3938": {"name": "named by", "necessity": "absent"},
            "P4342": {"name": "Store norske leksikon ID", "necessity": "absent"},
            "P443": {"name": "pronunciation audio", "necessity": "absent"},
            "P461": {"name": "opposite of", "necessity": "absent"},
            "P4613": {
                "name": "Encyclopedia of Modern Ukraine ID",
                "necessity": "absent",
            },
            "P5008": {
                "name": "on focus list of Wikimedia project",
                "necessity": "absent",
            },
            "P5019": {
                "name": "Brockhaus Enzyklopädie online ID",
                "necessity": "absent",
            },
            "P5034": {"name": "National Library of Korea ID", "necessity": "absent"},
            "P508": {"name": "BNCF Thesaurus ID", "necessity": "absent"},
            "P527": {"name": "has part(s)", "necessity": "absent"},
            "P5337": {"name": "Google News topics ID", "necessity": "absent"},
            "P5357": {
                "name": "The Encyclopedia of Science Fiction ID",
                "necessity": "absent",
            },
            "P580": {"name": "start time", "necessity": "absent"},
            "P6200": {"name": "BBC News topic ID", "necessity": "absent"},
            "P6262": {"name": "Fandom article ID", "necessity": "absent"},
            "P6366": {"name": "Microsoft Academic ID", "necessity": "absent"},
            "P646": {"name": "Freebase ID", "necessity": "absent"},
            "P6573": {"name": "Klexikon article ID", "necessity": "absent"},
            "P6706": {"name": "De Agostini ID", "necessity": "absent"},
            "P6900": {"name": "NicoNicoPedia ID", "necessity": "absent"},
            "P691": {"name": "NL CR AUT ID", "necessity": "absent"},
            "P7033": {
                "name": "Australian Educational Vocabulary ID",
                "necessity": "absent",
            },
            "P7305": {"name": "Online PWN Encyclopedia ID", "necessity": "absent"},
            "P7314": {"name": "TDV İslam Ansiklopedisi ID", "necessity": "absent"},
            "P7502": {"name": "Golden ID", "necessity": "absent"},
            "P7775": {"name": "RationalWiki ID", "necessity": "absent"},
            "P7818": {"name": "French Vikidia ID", "necessity": "absent"},
            "P7827": {"name": "Spanish Vikidia ID", "necessity": "absent"},
            "P7832": {"name": "Basque Vikidia ID", "necessity": "absent"},
            "P793": {"name": "significant event", "necessity": "absent"},
            "P8189": {
                "name": "National Library of Israel J9U ID",
                "necessity": "absent",
            },
            "P828": {"name": "has cause", "necessity": "absent"},
            "P8313": {"name": "Den Store Danske ID", "necessity": "absent"},
            "P8408": {"name": "KBpedia ID", "necessity": "absent"},
            "P8814": {"name": "WordNet 3.1 Synset ID", "necessity": "absent"},
            "P8885": {"name": "Namuwiki ID", "necessity": "absent"},
            "P9084": {"name": "ABC News topic ID", "necessity": "absent"},
            "P910": {"name": "topic's main category", "necessity": "absent"},
            "P920": {"name": "LEM ID", "necessity": "absent"},
            "P949": {
                "name": "National Library of Israel ID (old)",
                "necessity": "absent",
            },
            "P9807": {"name": "SNK ID", "necessity": "absent"},
            "P9885": {"name": "Bing entity ID", "necessity": "absent"},
        }
