# pip install arxiv python-dateutil
import arxiv, json, datetime
from dateutil import parser as dp

ARXIV_ID = "2508.18443"  # <-- your id

results = list(arxiv.Search(id_list=[ARXIV_ID]).results())
p = results[0]

jsonld = {
  "@context": "https://schema.org",
  "@type": "ScholarlyArticle",
  "headline": p.title,
  "description": p.summary.strip(),
  "author": [
    {"@type": "Person", "name": a.name, "affiliation": {"@type":"Organization","name":""}}
    for a in p.authors
  ],
  "datePublished": dp.parse(p.published.strftime("%Y-%m-%d")).date().isoformat(),
  "publisher": {"@type":"Organization","name": "arXiv"},
  "url": f"https://arxiv.org/abs/{ARXIV_ID}",
  "image": "https://YOUR_DOMAIN.com/images/pneugelsight_teaser.png",  # your preview
  "keywords": list(p.primary_category.split(".")) + list(p.categories),
  "abstract": p.summary.strip(),
  "isAccessibleForFree": True,
  "mainEntity": {"@type": "WebPage","@id": f"https://arxiv.org/abs/{ARXIV_ID}"}
}

print('<script type="application/ld+json">')
print(json.dumps(jsonld, ensure_ascii=False, indent=2))
print('</script>')
