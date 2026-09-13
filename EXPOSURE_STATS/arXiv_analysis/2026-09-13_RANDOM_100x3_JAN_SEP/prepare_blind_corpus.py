#!/usr/bin/env python3
import csv, json, random
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'arxiv_random_100_2024_2025_2026_combined.csv'
BLIND_CSV = ROOT / 'BLIND_300_title_abstract.csv'
KEY_CSV = ROOT / 'BLIND_KEY_DO_NOT_USE_FOR_SCORING.csv'
SEED = 918273

rows = list(csv.DictReader(SRC.open(encoding='utf-8')))
assert len(rows) == 300, len(rows)

rng = random.Random(SEED)
order = list(range(len(rows)))
rng.shuffle(order)

with BLIND_CSV.open('w', newline='', encoding='utf-8') as fblind, KEY_CSV.open('w', newline='', encoding='utf-8') as fkey:
    bw = csv.DictWriter(fblind, fieldnames=['blind_id', 'title', 'abstract'])
    kw = csv.DictWriter(fkey, fieldnames=['blind_id','year','arxiv_id','created','updated','authors','categories','link'])
    bw.writeheader(); kw.writeheader()
    for rank, idx in enumerate(order, 1):
        r = rows[idx]
        bid = f'XR{rank:03d}'
        bw.writerow({'blind_id': bid, 'title': r['title'], 'abstract': r['abstract']})
        kw.writerow({k: (bid if k=='blind_id' else r[k]) for k in kw.fieldnames})

meta = {
    'blind_seed': SEED,
    'records': len(rows),
    'scoring_view': ['blind_id','title','abstract'],
    'withheld_until_scores_frozen': ['year','arxiv_id','created','updated','authors','categories','link'],
    'source': SRC.name,
}
(ROOT / 'BLINDING_METADATA.json').write_text(json.dumps(meta, indent=2) + '\n', encoding='utf-8')
print(f'wrote {BLIND_CSV.name}, {KEY_CSV.name}, BLINDING_METADATA.json')
