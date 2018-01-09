# Immigration

In this section, the [ISTAT dataset](http://stra-dati.istat.it/Index.aspx#) is analyzed. The dataset provides information on the population of both Italian-born and foreign-born citizens, split between the Italian destination territory, the foreigners country of origin, and the gender. The data are collected from 2003 on, but until 2011 the values are not the results of continuous observation, they are a statistical reconstruction between the two censures of 2001 and 2011.

Note that ISTAT organizes the Italian territories into the following five zones:
- Centro;
- Isole;
- Nord-est;
- Nord-ovest;
- Sud.

## Gender Distribution Plots

The following plot shows the gender distribution over the years, aggregated both on the destination and the origin territories.

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/gender_distribution.png)

Form this stacked barplot, the distribution across the gender seems to be quite balanced.

## Zones Distribution Plots

Here, the aim is to show the distributions of the foreign-born citizens across the five Italian zones. They are studied without distinction over the origin country.

Initially, the total foreign-born population is analyzed as follows:
- the absolute value distribution;
- the growth distribution;
- the growth rate distribution, i.e. (year - prev_year)/prev_year.

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/zone.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/zone_abs_growth.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/zone_prev_growth.png)

Based on the above figure, even if the growth rate is significantly decreasing, the immigration is still an increasing phenomenon. Observe that in 2014, the growth rate is notably reduced. A possible explanation could be that in the same year (07/10/2014) there was the first [agreement](http://www.interno.gov.it/sites/default/files/sub-allegato_n._25_-_intesa_conferenza_stato_regioni_del_10_luglio_2014.pdf) between the Italian government, the regions and local authorities on a national level to face the flow of foreign-born population.

Furthermore, between 2010 and 2011 there is a significant decrease in the growth rate. This could be justified by the fact that the data before 2011 is a statistical estimation, while from 2011 is an actual continuous observation. Thus, ISTAT may have overestimated the phenomenon.

While the growth trend is quite similar in the five zones, the absolute value is not. Three different trends could be distinguished from this analysis:
- Nord-ovest - initially between 2003 and 2011 the absolute population is higher than any other region. After 2014 the growth rate seems to stabilize;
- Nord-est and Centro - for these regions, the absolute population is at similar levels;
- Isole and Sud - these two zones have attracted less foreign-born population than the other zones. Although the absolute numbers are different, both zones experience similar growth trends.

## Regions Distribution Plots

The study computed for the Italian zones will be extended to regions level. Here, instead of Trentino-Alto Adige, Trentino and South Tyrol are considered.

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_abs.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_abs_growth.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/region_prev_growth.png)

Here the three clusters situation is highlighted. Moreover it is possible to see that most of the flow from the Nord-ovest comes from the Lombardia region (plus Piemonte, second cluster). While Lazio, Emilia-Romagna, Veneto and Toscana are those that contribute the most to the second cluster (Nord-est, Centro).

## Zones by Origin Distribution Plots
In this section the different origin territories are included in the study at two aggregation levels:
- continent;
- country. 

### Origin Continent
First, a plot for each Italian zone is shown. Here an aggregation over the origin continent is performed.

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Centro.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Isole.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Nord-est.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Nord-ovest.png)

![alt text](https://github.com/SaraR-1/Immigration/blob/master/Plots/continent_distr_Sud.png)

It is interesting that, even if the continent distributions are similar across the Italian zones, there are some differences.

Europe is always the continent that contributes the most to the Italy foreigners flow and the growth rate decreases from 2014 (as aforementioned). The five trends are quite similar even if with different absolute values, especially in Sud and Isole. All the zones report an increase in the 2007-2008 period, it is remarkable mainly in Sud and Isole.

The others continent flow is less important, in terms of absolute value, BUT the growth rate is not the same for all the zones: it decreases in Centro, Nord-est and Nord-ovest and increases in Isole and Sud (which are in the "third cluster"). This flow rate consideration holds also for Europe born foreigners.

The flow from Pacific is very similar in all the zones and could be overlooked. American born population is significant only in Nord-ovest and Centro.

## Region - top 5 countries per continent Plot

The goal of this section is to show the distribution of the origin countries that contribute the most to the Italian foreigners-born population flow.

For each couple Continent-Zone and for all the regions in the particular zone, the distributions of the top 5 origin countries of the specific continent are shown. 

An aggregating plot is also included. It represents the distribution of the top "n" countries in the zone. The top "n" countries covered all the top 5 countries found in the zone regions.

### Africa

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAfrica_Centro.png)

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAfrica_Isole.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAfrica_Nord-est.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAfrica_Nord-ovest.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAfrica_Sud.png) 

In all of the five zones, Marocco is the country that contributes the most to the total African-born population flow. 

Until 2013,  the Marocco's trend is quite similar, with different absolute values, in the Italian zones. From 2014 on, the destination territories of the Moroccan population seem to be changed. In particular, the growth rate of the zones with a higher absolute value (Centro, Nord-est, Nord-ovest) is decreasing, while it is increasing in the other zones Isole and Sud.

Others notable flows are the once from Tunisia to Sicily and from Egypt to Lombardia.

### America

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAmerica_Centro.png)

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAmerica_Isole.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAmerica_Nord-est.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAmerica_Nord-ovest.png)

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAmerica_Sud.png) 

### Asia

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAsia_Centro.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAsia_Isole.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAsia_Nord-est.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAsia_Nord-ovest.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAsia_Sud.png) 

### Europe

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeEurope_Centro.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeEurope_Isole.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeEurope_Nord-est.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeEurope_Nord-ovest.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeEurope_Sud.png) 

### Pacific

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completePacific_Centro.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completePacific_Isole.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completePacific_Nord-est.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completePacific_Nord-ovest.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completePacific_Sud.png)

## Zone - top 2 countries per continent Plot

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/zone_top2_countrie_cont_Centro.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/zone_top2_countrie_cont_Isole.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/zone_top2_countrie_cont_Nord-est.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/zone_top2_countrie_cont_Nord-ovest.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/zone_top2_countrie_cont__Sud.png)
