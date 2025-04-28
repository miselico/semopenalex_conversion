import urllib.request
import xml.etree.ElementTree as ET

bucket_prefix = map(lambda a: a.strip(),
                    """ \
        authors
        concepts
        domains
        fields
        funders
        institutions
        keywords
        publishers
        sources
        subfields
        topics
        works""".split("\n")
                    )


for prefix in bucket_prefix:
    url = "https://semopenalex.s3.amazonaws.com/?list-type=2&delimiter=%2F&prefix=" + prefix + "%2F"
    contents = urllib.request.urlopen(url).read()
    # print(contents)
    tree = ET.fromstring(contents)
    truncateds = tree.findall(
        './/{http://s3.amazonaws.com/doc/2006-03-01/}IsTruncated')
    for truncated_el in truncateds:
        assert truncated_el.text == "false"
    keys = tree.findall(
        './/{http://s3.amazonaws.com/doc/2006-03-01/}Contents/{http://s3.amazonaws.com/doc/2006-03-01/}Key')
    for key in keys:
        assert key.text is not None
        if key.text.endswith("trig.gz"):
            print(f"http://semopenalex.s3.amazonaws.com/{key.text}")


