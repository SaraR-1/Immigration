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

### Regions Distribution Plots - Map Visualization

[prova](https://github.com/SaraR-1/Immigration/blob/master/Plots/resident_foreigners_2017.html)

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

The American flow is pretty different in the observed zones.

In Centro and Nord-ovest the countries giving the most to the aggregate flow are Peru and Ecuador. More in detail, the most common destination regions are Lazio and Lombardia for both Peruvians and Ecuadorians, then Toscana and Liguria for Peruvians and Ecuadorians respectively.  
Once again, looking at the plots, it is possible to say that the absolute values are significantly different: the once from Pure and Ecuador are about double and quadruple respectively in the Nord-ovest with respect to the Centro. Both the growth rates start decreasing having negative values from 2014.

In Nord-est, Isole, and Sud it is possible to notice that Brazil is the most common origin country. In Nord-est the growth rate seems to be stable from 2014 on, while in Isole and Sud it is still increasing. 

### Asia

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAsia_Centro.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAsia_Isole.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAsia_Nord-est.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAsia_Nord-ovest.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeAsia_Sud.png) 

Concerning the Asian-born population flow distributions, the plots show a similar trend at the zone level. That is: all the countries have a comparable behavior even if with significantly different scale (in absolute values). 

Here is evident, more than in the others continent flows, that just one or two (in Centro and Nord-est) regions contributes to the aggregate distribution.

The Chinese-born flow is always the highest but in Lazio and Sicily, where the highest values correspond to the Philippines and Sri Lanka. 

### Europe

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeEurope_Centro.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeEurope_Isole.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeEurope_Nord-est.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeEurope_Nord-ovest.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completeEurope_Sud.png) 

Romania is the country that contributes the most to the total European-born population flow. Even if the growth rate seems to decrease, it still has an increasing trend.

In regions like Tuscany, Lombardy, Puglia, and Abruzzo the Albanian flow is remarkable even if from 2014 it looks like to have a negative growth rate.

In Campania, there may be an important Ukrainian community.

### Pacific

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completePacific_Centro.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completePacific_Isole.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completePacific_Nord-est.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completePacific_Nord-ovest.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/completePacific_Sud.png)

It is possible to see that here the scales are very different from the once in the above plots. As aforementioned, the Pacific flow could be overlooked.

At the end of this section, it is also possible to come up with some comments about the zone-regions relation.

Lazio and partially Tuscany represent most of the Centro total distribution.

Sardinia's data could be overlooked with respect to the Sicily once.

Lombardy constitutes almost the entire Nord-ovest flow. In specific case also Piedmont and Liguria contribute to the aggregate values.

Emilia Romagna and Veneto seem to split up all the Nord-est flow.

In Sud, it is not possible to point out a significant difference between the regional trends.  However, it is shown that Molise and Basilicata may be ignored in the analysis.

## Zone - top 2 countries per continent Plot

In the following plots, it is shown for each of the five Italian zones top two countries per continent. Top two countries per continent represent the two countries, for each continent, contributing the most to the zone flow.

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/zone_top2_countrie_cont_Centro.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/zone_top2_countrie_cont_Isole.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/zone_top2_countrie_cont_Nord-est.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/zone_top2_countrie_cont_Nord-ovest.png) 

![](https://github.com/SaraR-1/Immigration/blob/master/Plots/zone_top2_countrie_cont__Sud.png)

These plots seem to confirm what came out from the previous section. 

Moreover, it is highlighted the difference between the Romanian flow and all the other flows. 

To conclude that it would be possible to say that these two last sections confirm what assumed before about the three different behavior of the five zones.
