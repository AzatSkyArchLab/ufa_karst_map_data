Ufa Karst Sinkholes Map.
Interactive web map of karst sinkholes and karst-prone areas in Ufa and the Republic of Bashkortostan, Russia.

Features.
1) Real sinkhole data — Database from the Institute of Geology UFRC RAS (A.I. Smirnov)
2) Historical data — Digitized maps from "Karst of Bashkortostan" (Martin & Abdrakhmanov)
3) Photo gallery — 70+ photos of actual sinkholes with bottom panel viewer
4) Multiple map styles — Light, Satellite, and Dark themes
5) 3D buildings — Toggle 3D building extrusions
6) Responsive design — Works on desktop and mobile devices

Data Sources
IG UFRC RAS Database - 201 Verified sinkhole locations with dates, descriptions, and photos Karst of Bashkortostan
~ 500 Historical karst zones and sinkhole approximations. Made from the book source.

Technology Stack

- Mapbox GL JS v3.0.1
- Vanilla JavaScript
- GeoJSON data format
- Google Photos CDN for images

Repository Structure
├── index.html                            # Main map application
├── karst_sinkholes_with_photos.geojson   # Real sinkholes with photo links
├── UfaKarstAreaKarstPoint_merged.geojson # Historical karst data
└── README.md

Deployment
- Tilda html custom code
- See map at https://mapufa.ru

Configuration
- Replace Mapbox access token in index.html:
- javascriptmapboxgl.accessToken = 'your_mapbox_token_here';
- Photo Gallery
- The map features an interactive photo gallery:

How to use?
- Click on a blue marker with photos
- Bottom panel slides up with horizontal photo scroll
- Click any photo for fullscreen lightbox view
- Navigate with arrow keys or swipe

Live Demo
[mapufa.ru](https://mapufa.ru)

References
- Smirnov A.I. "Modern karst sinkholes in the Southern Urals and Cis-Urals (within the Republic of Bashkortostan)" // Engineering Geology, 2020
- Martin V.I., Abdrakhmanov R.F. "Karst of Bashkortostan" — Ufa, 1997

License
Data provided by the Institute of Geology UFRC RAS. Map visualization is open source.

Contributing
Contributions are welcome! If you have additional sinkhole data or corrections:
- Open an issue with location details
- Submit a pull request with GeoJSON updates

Built for mapufa.ru — Urban mapping projects for Ufa
