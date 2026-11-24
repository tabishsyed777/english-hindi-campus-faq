# English–Hindi Campus FAQ

Retrieve approved campus answers in English or Hindi, including Romanized Hindi queries. Campus staff can add new bilingual entries without training a model.

## Quick start

From this directory, run these commands with Python 3.12 or 3.13. The example corpus is fictional and runs offline with the standard library.

```sh
python3 core.py ask 'library hours'
python3 core.py build data/source.json snapshot.json
python3 core.py ask 'पुस्तकालय का समय' --snapshot snapshot.json
python3 -m unittest discover -v
python3 evaluate.py
```

## Asking questions

Enter a listed English question, Hindi topic, or Hinglish alias such as “library kab khulti hai”. Hindi and Hinglish inputs return Hindi.

## Using your own sources

Use the records in `data/source.json` as a schema example. Supply unique citation IDs and usable source locators. Build a new snapshot after additions, edits, or deletions. A successful build atomically replaces the previous snapshot. Results contain the answer, retrieval method and source locators. Unsupported queries return `insufficient_evidence`.

Retrieval uses a curated bilingual alias dictionary. New phrasing needs an alias. The demo handbook describes a fictional campus.

See [QA.md](QA.md) for measured results, review status and release limits.
