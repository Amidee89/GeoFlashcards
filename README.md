# GeoFlashcards
 
 Printable PDF flashcards of all 193 UN countries + 2 Observer states + 12 non independent regions, with flag+map in the front and important data in the back.
 If you just want the PDFs, head to the releases: https://github.com/Amidee89/GeoFlashcards/releases
 
 To render the pdf again:
 Run python renderer.py and go to http://127.0.0.1:5000/back/ or http://127.0.0.1:5000/front or http://127.0.0.1:5000/complete to re-render with the browser. 
 Only Chrome manages to cut off properly the pages, and you have to print even pages only because it adds a white page after the break (the white page also makes macOS preview render random gray stuff in the flashcards).
 Chrome also has different margins for the first page for some reason, so I added 3 extra lines to the CSV so all pages come out the same.
 Chrome will *also* put different margins on the sides of the flashcards, so you have to print with custom margin and move the right margin left by 2.5mm.
 
 Very very aggressive margins for printing on A4, you might need to scale back but be careful to do so as it might screw up horizontal alignment between front and back. 
 
 Data available here:
 https://docs.google.com/spreadsheets/d/1VADXC_0FcfDw9iflfB6tkSPC86Nlv_Qa7_EJE5hI5ps/edit?usp=sharing
 
 Flags data from flagpedia.net and maps from Wikimedia. Watch out – the entire repo is about 1.5 gigabytes because it includes a *lot* of SVGs, even for territories that are not included in the pdfs. This means, if you are looking for a place to download all 16:9 Wikipedia maps, you can do it through this repo.
 If you just want to download the PDFs, just head to the releases.

All 195 countries from [this list](https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population), with the following data:

Front:
Flag ([from Flagpedia](https://flagpedia.net/download/vector)) | Map ([16:9 locator from Wikimedia](https://commons.wikimedia.org/wiki/Category:SVG_locator_maps_of_countries_(16:9_regional_location_map_scheme))) 

Back:
- Capital
- Climate (GPT-4 generated)
- Languages
- Currency
- Area 
- Population 
- Population Growth
- GDP
- GDP per capita
- Gini coefficient
- Human development index
- Press Freedom Index
- Description (GPT-4 generated)

All numerical values present ranking # and a 1-5 scale for easier understanding of the values. 
GPT-4 generated data has been sort of triple verified, but it could use a hand being reverified and sometimes rewritten by a human. I'd love to see pull requests for the csv data with corrections on the data.
