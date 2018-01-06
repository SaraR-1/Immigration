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
In this section the different origin territories are included in the study. 

### Origin Continent
First, a plot for each Italian zone is shown. Here an aggregation over the origin continent is performed.

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Centro.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Isole.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Nord-est.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Nord-ovest.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Sud.png)

It is interesting that, even if the continent distributions are similar across the Italian zones, there are some differences. Europe is always the continent that contributes the most to the Italy foreigners flow and the growth rate decreases from 2014 (as aforementioned). The others continent flow is less important, in terms of absolute value, BUT the growth rate is not the same for all the zones: it decreases in Centro, Nors-est and Nord-ovest and increases in Isole and Sud (which are in the "third cluster").

The flow from Pacific could be overlooked. American born population is significant only in Nord-ovest and Centro.

## 

### Africa

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAfrica_Centro.png)

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAfrica_Isole.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAfrica_Nord-es.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAfrica_Nord-ovest.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAfrica_Sud.png) 

### America

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAmerica_Centro.png)

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAmerica_Isole.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAmerica_Nord-es.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAmerica_Nord-ovest.png)

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAmerica_Sud.png) 

### Asia

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAsia_Centro.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAsia_Isole.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAsia_Nord-es.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAsia_Nord-ovest.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAsia_Sud.png) 

### Europe

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeEurope_Centro.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeEurope_Isole.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeEurope_Nord-es.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeEurope_Nord-ovest.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeEurope_Sud.png) 

### Pacific

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completePacific_Centro.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completePacific_Isole.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completePacific_Nord-es.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completePacific_Nord-ovest.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completePacific_Sud.png)
