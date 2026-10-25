# ridex-maps

Offline region maps for the [RideX](https://github.com/6135/Moto-Ride-X) motorcycle app.

Every month a GitHub Actions workflow downloads OpenStreetMap extracts from Geofabrik, turns them into vector tiles with [Planetiler](https://github.com/onthegomap/planetiler) (OpenMapTiles schema, max zoom 14), and publishes one `.pmtiles` file per region plus a `catalog.json` as a release (`maps-YYYY-MM`). The app reads `releases/latest/download/catalog.json`.

- Regions: [regions.yml](regions.yml) (Portugal, Spain, Azores, Canary Islands, Andorra, Morocco, Italy, Great Britain, Ireland, Netherlands, Belgium, Switzerland, Austria).
- Workflow: [.github/workflows/build-regions.yml](.github/workflows/build-regions.yml), monthly and on demand.
- The last 2 releases are kept.

This repo contains only OpenStreetMap-derived data, never personal data.

## Licence and attribution

Map data © [OpenStreetMap contributors](https://www.openstreetmap.org/copyright), available under the Open Database Licence (ODbL). Schema © [OpenMapTiles](https://openmaptiles.org). Apps showing these maps must display "© OpenMapTiles © OpenStreetMap contributors".
