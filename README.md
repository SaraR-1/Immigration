# Immigration
Working on it!

Dataset Structure:
- geo and population data, keep only the countries in cittadinanza (only the countries whose immigration flow to Italy is recorded);
coherence between tables is neede.. country names are not always in the same language. To translate them, first use babel (does not have limit issues), then (if some matching is not found) use translate (google "unusual traffic" issue);
- drop the age information from the resident tabel 'cause it is not available in the foreigners table;
- from population and gpd drop not informative years (all nan);

Statistics - issues:
- what if we have missing values in the resident_foreigners table? E.g. Alessandria - Andorra information available only for 2017
some countries have more than one "main" city (not just the capital) --> distances between countries computed from all the main cities. What about to keep just the most populated one? It should be a better representer of the distance as weight.
- how to handle missing data is gdp table? E.g. 1) Andorra, all nan; 2) Aruba only 2011

Statistics - to do:
- abs frequencies for each:
	- year - singular and aggregate trend;
	- zona - regione - provincia;
	- maschio - femmina - totale --> sex distribution over the italian territory;
- rel frequencies (same as abs), relativized by:
	- num pop origin;
	- num pop destination;
	- countries distances;
 
    
