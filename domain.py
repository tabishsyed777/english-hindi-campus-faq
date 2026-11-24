"""English–Hindi Campus FAQ domain retrieval and answer rules."""
NAME = '06-english-hindi-campus-faq'

from common import norm,require
FIELDS=("en","hi","hinglish","question","english","hindi")

def validate(rows):
    keys=[norm(r[k]).rstrip("?।") for r in rows for k in ("en","hi","hinglish","question")]
    require(len(keys)==len(set(keys)),"duplicate FAQ alias")

def solve(rows,q):
    q=q.rstrip("?।").strip()
    for r in rows:
        for key in ("hi","hinglish","en","question"):
            if q==norm(r[key]).rstrip("?।"):
                return r["hindi" if key in ("hi","hinglish") else "english"],[r],"bilingual alias"
