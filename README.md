# Immigration

## Gender Distribution Plots
![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/gender_distribution.png)

This is the gender distribution over the years, aggregated both on the destination and the origin territories.

Form this stacked barplot, the distribution across the gender seems to be quite balanced.

## Zones Distribution Plots

In this section, the [ISTAT dataset](http://stra-dati.istat.it/Index.aspx#) is analyzed. The dataset provides information on the population of both Italian-born and foreign-born citizens, split between the Italian destination territory, the foreigners country of origin, and the gender. The data are collected from 2003 on, but until 2011 the values are not the results of continuous observation, they are a statistical reconstruction between the two censures of 2001 and 2011.

Note that ISTAT organizes the Italian territories into the following five zones:
- Centro;
- Isole;
- Nord-est;
- Nord-ovest;
- Sud.

Initially, the total foreign-born population (without distinction over the origin country) is analyzed as follows:
- the absolute value distribution;
- the growth distribution;
- the growth rate distribution, i.e. (year - prev_year)/prev_year.

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/zone.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/zone_abs_growth.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/zone_prev_growth.png)

Based on the above figure, even if the growth rate is significantly decreasing, the immigration is still an increasing phenomenon. Observe that in 2014, the growth rate is significantly reduced. A possible explanation could be that in the same year (07/10/2014) there was the first [agreement](http://www.interno.gov.it/sites/default/files/sub-allegato_n._25_-_intesa_conferenza_stato_regioni_del_10_luglio_2014.pdf) between the Italian government, the regions and local authorities on a national level to face the flow of foreign-born population.

Furthermore, between 2010 and 2011 there is a significant decrease in the growth rate. This could be justified by the fact that the data before 2011 is a statistical estimation, while from 2011 is an actual continuous observation. Thus, ISTAT may have overestimated the phenomenon.

While the growth trend is quite similar to the five zones, the absolute value is not. Three different trends could be distinguished from this analysis:
- Nord-ovest - initially between 2003 ... 2011 the absolute population is higher than any other region while after 2014 the growth rate seems to stabilize.;
- Nord-est and Centro - for these regions, the absolute population is at similar levels;
- Isole and Sud - these two zones have attracted less foreign-born population than the other zones. Although the absolute numbers are different, both zones experience similar growth trends.

## Regions Distribution Plots
Same distributions computed for the zones will be analyzed for the Italian regions. Here, instead of Trentino-Alto Adige, Trentino and South Tyrol are considered.

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_abs.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_abs_growth.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_prev_growth.png)

Here the three clusters situation is highlighted. Moreover it is possible to see that most of the flow from the Nord-ovest comes from the Lombardia region (plus Piemonte, second cluster). While Lazio, Emilia-Romagna, Veneto and Toscana are those that contribute the most to the second cluster (Nord-est, Centro).

## Zones by Origin Distribution Plots
I want to include in the study also the different origin territories. 

### Origin Continent
First I will consider only the origin continent performing again an aggregation over the countries. Thus, I have a plot for each Italian zone.

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Centro.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Isole.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Nord-est.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Nord-ovest.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Sud.png)

It is interesting that, even if the continent distributions are similar across the Italian zones, there are some differences. Europe is always the more influent continent and the growth rate decreases from 2014 (as aforementioned). The others continent flow is less important, BUT the growth rate is not the same for all the zones: it decreases in Centro, Nors-est and Nord-ovest and increases in Isole and Sud (which are in the "third cluster").

The flow from Pacific could be overlooked. American born population is significant only in Nord-ovest and Centro.

## Top 5 countries per Continent
Let's see the distibution of the 5 countries more "influent" for each continent.

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/zone_top5_countrie_cont_Centro.png)
Notable components: Romania, Albania.

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/zone_top5_countrie_cont_Isole.png)
Notable components: Romania, Tunisia, Marocco.

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/zone_top5_countrie_cont_Nord-est.png)
Notable components: Romania, Marocco, Albania.

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/zone_top5_countrie_cont_Nord-ovest.png)
Notable components: Romania, Marocco, Albania.

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/zone_top5_countrie_cont_Sud.png)
Notable components: Romania, Albania, Ukraine, Marocco, Tunisia.

## Countries per Continent
Here I can analyze all the countries-component for each continent.

### Africa
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_Africa_countries_Centro.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_Africa_countries_Isole.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_Africa_countries_Nord-est.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_Africa_countries_Nord-ovest.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_Africa_countries_Sud.png)

As from the "top 5 countrie" plots, it is clear that the relevant country in Africa is Marocco. Only in Isole, Tunisia is important as Marocco. 

### Asia
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_Asia_countries_Centro.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_Asia_countries_Isole.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_Asia_countries_Nord-est.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_Asia_countries_Nord-ovest.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_Asia_countries_Sud.png)

### Europe
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_Europe_countries_Centro.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_Europe_countries_Isole.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_Europe_countries_Nord-est.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_Europe_countries_Nord-ovest.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_Europe_countries_Sud.png)

### America
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_America_countries_Centro.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_America_countries_Isole.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_America_countries_Nord-est.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_America_countries_Nord-ovest.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_America_countries_Sud.png)

### Pacific
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_Pacific_countries_Centro.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_Pacific_countries_Isole.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_Pacific_countries_Nord-est.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_Pacific_countries_Nord-ovest.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_zone_Pacific_countries_Sud.png)

## Regions by Origin Distribution Plots

### Origin Continent
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Abruzzo.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Basilicata.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Calabria.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Campania.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Emilia-Romagna.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Friuli-VeneziaGiulia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Lazio.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Liguria.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Lombardia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Marche.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Molise.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Piemonte.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_ProvinciaAutonomadiBolzano.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_ProvinciaAutonomadiTrento.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Puglia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Sardegna.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Sicilia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Toscana.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Umbria.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Valled'Aosta.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Veneto.png)

## Top 5 countries per Continent
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_top5_countrie_cont_Abruzzo.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_top5_countrie_cont_Basilicata.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_top5_countrie_cont_Calabria.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_top5_countrie_cont_Campania.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_top5_countrie_cont_Emilia-Romagna.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_top5_countrie_cont_Friuli-VeneziaGiulia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_top5_countrie_cont_Lazio.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_top5_countrie_cont_Liguria.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_top5_countrie_cont_Lombardia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_top5_countrie_cont_Marche.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_top5_countrie_cont_Molise.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_top5_countrie_cont_Piemonte.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_top5_countrie_cont_ProvinciaAutonomadiBolzano.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_top5_countrie_cont_ProvinciaAutonomadiTrento.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_top5_countrie_cont_Puglia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_top5_countrie_cont_Sardegna.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_top5_countrie_cont_Sicilia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_top5_countrie_cont_Toscana.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_top5_countrie_cont_Umbria.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_top5_countrie_cont_Valled'Aosta.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_top5_countrie_cont_Veneto.png)


## Countries per Continent

### Africa
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Africa_countries_Abruzzo.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Africa_countries_Basilicata.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Africa_countries_Calabria.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Africa_countries_Campania.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Africa_countries_Emilia-Romagna.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Africa_countries_Friuli-VeneziaGiulia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Africa_countries_Lazio.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Africa_countries_Liguria.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Africa_countries_Lombardia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Africa_countries_Marche.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Africa_countries_Molise.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Africa_countries_Piemonte.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Africa_countries_ProvinciaAutonomadiBolzano.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Africa_countries_ProvinciaAutonomadiTrento.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Africa_countries_Puglia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Africa_countries_Sardegna.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Africa_countries_Sicilia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Africa_countries_Toscana.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Africa_countries_Umbria.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Africa_countries_Valled'Aosta.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Africa_countries_Veneto.png)

### Asia
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Asia_countries_Abruzzo.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Asia_countries_Basilicata.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Asia_countries_Calabria.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Asia_countries_Campania.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Asia_countries_Emilia-Romagna.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Asia_countries_Friuli-VeneziaGiulia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Asia_countries_Lazio.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Asia_countries_Liguria.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Asia_countries_Lombardia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Asia_countries_Marche.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Asia_countries_Molise.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Asia_countries_Piemonte.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Asia_countries_ProvinciaAutonomadiBolzano.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Asia_countries_ProvinciaAutonomadiTrento.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Asia_countries_Puglia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Asia_countries_Sardegna.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Asia_countries_Sicilia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Asia_countries_Toscana.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Asia_countries_Umbria.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Asia_countries_Valled'Aosta.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Asia_countries_Veneto.png)

### Europe
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Europe_countries_Abruzzo.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Europe_countries_Basilicata.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Europe_countries_Calabria.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Europe_countries_Campania.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Europe_countries_Emilia-Romagna.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Europe_countries_Friuli-VeneziaGiulia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Europe_countries_Lazio.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Europe_countries_Liguria.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Europe_countries_Lombardia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Europe_countries_Marche.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Europe_countries_Molise.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Europe_countries_Piemonte.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Europe_countries_ProvinciaAutonomadiBolzano.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Europe_countries_ProvinciaAutonomadiTrento.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Europe_countries_Puglia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Europe_countries_Sardegna.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Europe_countries_Sicilia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Europe_countries_Toscana.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Europe_countries_Umbria.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Europe_countries_Valled'Aosta.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Europe_countries_Veneto.png)

### America
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_America_countries_Abruzzo.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_America_countries_Basilicata.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_America_countries_Calabria.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_America_countries_Campania.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_America_countries_Emilia-Romagna.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_America_countries_Friuli-VeneziaGiulia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_America_countries_Lazio.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_America_countries_Liguria.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_America_countries_Lombardia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_America_countries_Marche.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_America_countries_Molise.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_America_countries_Piemonte.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_America_countries_ProvinciaAutonomadiBolzano.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_America_countries_ProvinciaAutonomadiTrento.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_America_countries_Puglia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_America_countries_Sardegna.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_America_countries_Sicilia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_America_countries_Toscana.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_America_countries_Umbria.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_America_countries_Valled'Aosta.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_America_countries_Veneto.png)

### Pacific
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Pacific_countries_Abruzzo.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Pacific_countries_Basilicata.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Pacific_countries_Calabria.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Pacific_countries_Campania.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Pacific_countries_Emilia-Romagna.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Pacific_countries_Friuli-VeneziaGiulia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Pacific_countries_Lazio.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Pacific_countries_Liguria.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Pacific_countries_Lombardia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Pacific_countries_Marche.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Pacific_countries_Molise.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Pacific_countries_Piemonte.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Pacific_countries_ProvinciaAutonomadiBolzano.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Pacific_countries_ProvinciaAutonomadiTrento.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Pacific_countries_Puglia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Pacific_countries_Sardegna.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Pacific_countries_Sicilia.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Pacific_countries_Toscana.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Pacific_countries_Umbria.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Pacific_countries_Valled'Aosta.png)
![](https://github.com/SaraR-1/Immigration/blob/master/Plots/py_region_Pacific_countries_Veneto.png)
