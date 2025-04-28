How I collected the data for the February 2025 version.
I cannot find back how I did it for the earlier version. I recall doing some steps manually as well.

This URL I could get from the dev tools when visiting https://semopenalex.s3.amazonaws.com/browse.html#authors/
https://semopenalex.s3.amazonaws.com/?list-type=1&delimiter=%2F&prefix=authors%2F


So, we use this to reconstruct the other URLS.
Note, there is a tag in the response indicating whether the result is truncated. 
When visiting, https://semopenalex.s3.amazonaws.com/ we would get ALL buckets, but the result is truncated.
So, we do a part at a time.

We want these sub-buckets

    authors/
    concepts/
    domains/
    fields/
    funders/
    institutions/
    keywords/
    publishers/
    sources/
    subfields/
    topics/
    works/

Code to get the keys out in get_relevant_bucket_ids.py

Run 
```bash
$ python get_relevant_bucket_ids.py > ttlfilesSOA_2025_02_11.txt
```
Run 
```bash
./download_parallel2025.sh
```

