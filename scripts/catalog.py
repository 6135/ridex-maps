"""Writes catalog.json for the built regions (RideX ARCHITECTURE §9.9, step 3).

Usage: catalog.py <regions.yml> <dist dir> <release tag> <repo owner/name>
Each region needs dist/<id>.pmtiles and dist/<id>.osmdate (YYYY-MM-DD).
"""
import hashlib
import json
import os
import sys

import yaml

regions_file, dist, tag, repo = sys.argv[1:5]
regions = yaml.safe_load(open(regions_file, encoding="utf-8"))["regions"]
entries = []
for r in regions:
    src = os.path.join(dist, f"{r['id']}.pmtiles")
    if not os.path.exists(src):
        print(f"skipping {r['id']}: not built", file=sys.stderr)
        continue
    osm_date = open(os.path.join(dist, f"{r['id']}.osmdate"), encoding="utf-8").read().strip()
    name = f"{r['id']}-{osm_date}.pmtiles"
    os.replace(src, os.path.join(dist, name))
    sha = hashlib.sha256()
    with open(os.path.join(dist, name), "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            sha.update(chunk)
    entries.append({
        "id": r["id"],
        "name": r["name"],
        "bbox": r["bbox"],
        "osmDate": osm_date,
        "sizeBytes": os.path.getsize(os.path.join(dist, name)),
        "sha256": sha.hexdigest(),
        "url": f"https://github.com/{repo}/releases/download/{tag}/{name}",
        "minZoom": 0,
        "maxZoom": 14,
        "schema": "openmaptiles",
        "schemaVersion": "3.15",
    })
json.dump({"version": 1, "release": tag, "regions": entries},
          open(os.path.join(dist, "catalog.json"), "w", encoding="utf-8"), indent=2)
print(json.dumps(entries, indent=2))
