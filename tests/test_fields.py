import unittest

from okfrefresh import fields

PAYLOADS = {
    "business": {
        "@type": "AutoDealer",
        "telephone": "(352) 309-0695",
        "address": {
            "streetAddress": "17325 East Highway 50",
            "addressLocality": "Clermont",
            "addressRegion": "FL",
            "postalCode": "34711",
        },
        "aggregateRating": {"ratingValue": 4.7, "reviewCount": 1},
        "sameAs": ["https://www.google.com/maps/place/?q=place_id:XYZ"],
    },
    "gbp-context": {
        "gbp_meta": {"average_rating": 4.7, "total_reviews": 6589, "place_id": "ChIJ15"},
        "business_info": {"phone": "(352) 111-2222", "hours": "Mon-Fri 9-8"},
    },
    "vehicles": [
        {"condition": "New"},
        {"condition": "New"},
        {"condition": "Used"},
        {"condition": "Certified"},
        {"condition": ""},
    ],
}


class TestFields(unittest.TestCase):
    def test_counts(self):
        s = fields.extract_snapshot(PAYLOADS)
        self.assertEqual(s["new"], 2)
        self.assertEqual(s["used"], 3)
        self.assertEqual(s["total"], 5)

    def test_gbp_meta_preferred(self):
        s = fields.extract_snapshot(PAYLOADS)
        self.assertEqual(s["rating"], 4.7)
        self.assertEqual(s["reviews"], 6589)
        self.assertEqual(s["place_id"], "ChIJ15")
        self.assertEqual(s["phone"], "(352) 309-0695")

    def test_unknown_when_missing(self):
        s = fields.extract_snapshot({"business": {}, "gbp-context": {}, "vehicles": []})
        self.assertEqual(s["rating"], "unknown")
        self.assertEqual(s["place_id"], "unknown")
        self.assertEqual(s["address"], "unknown")

    def test_address_format(self):
        s = fields.extract_snapshot(PAYLOADS)
        self.assertEqual(s["address"], "17325 East Highway 50, Clermont, FL 34711")

    def test_place_id_from_sameas_fallback(self):
        payloads = {"business": {"sameAs": ["https://x/?q=place_id:ABC"]}, "gbp-context": {}}
        self.assertEqual(fields.extract_snapshot(payloads)["place_id"], "ABC")


if __name__ == "__main__":
    unittest.main()
