# edcrop

Evapotranspiration is one of the major components of Earth’s water balance, being the sum of evaporation 
and plant transpiration from the land and ocean surface. 

Edcrop is a Python package that, using climate input, simulates field-scale evapotranspiration 
and drainage from the root zone of an area covered with a crop, a wetland, or a forest. 

The conceptual model implemented in edcrop is a modification of the Evacrop model by Olesen and Heidmann (2002), 
which itself builds on the Watcros model by Aslyng and Hansen (1982). The edcrop conceptualization is based on 
considerations regarding the physical processes that are important for turning precipitation and irrigation 
into either evaporation, transpiration, or drainage from the root zone: Temperature determines whether 
precipitation falls as rain or snow, and it determines when snow thaws and infiltrates. The vegetation intercepts 
a part of precipitation, while the rest infiltrates into the ground. The infiltrated water will either evaporate, 
be absorbed by plant roots, be stored in the soil, or drain from the root zone. Potential evaporation is 
distributed between vegetation and soil, where the former part drives evaporation of intercepted water and plant 
transpiration from the green leaf area, while the latter part drives evaporation from the soil. The soil’s ability 
to store water depends on its field capacity; when the water content exceeds field capacity, water will gradually 
drain downwards. Furthermore, it is assumed that the annual life cycle of crops and wetland vegetation can be 
described by growing degree-days alone, while for forests the life cycle is described by a calendar. For irrigation, 
either (i) date and amount are input, or (ii) they are determined automatically by edcrop using certain criteria.

There are two alternative soil water balance functions to choose between in edcrop. The first alternative is an 
almost straight copy of the function used in the original Evacrop code by Olesen and Heidmann (2002), simulating 
flow through the soil profile as flow through two linear reservoirs using daily time steps. However, it can simulate 
macro-pore drainage, which the original Evacrop cannot. The second alternative simulates flow through the soil profile 
as flow through four linear or nonlinear reservoirs using daily or sub-daily time steps. For nonlinear reservoirs, 
edcrop.py uses Mualem – van Genuchten like functions. It also simulates gravity driven macro-pore flow as well as 
surface runoff. 

As input, given in text files, edcrop requires daily temperature, precipitation, and reference evapotranspiration. It also 
requires information about combination(s) of soil type and vegetation type to simulate. One can choose between seven 
default soil types and fifteen default vegetation types, or one can manually input information for other types of soil 
or vegetation. In a single model run, edcrop.py can loop through lists of climate files, soils, and vegetation.

Edcrop can be imported and used in own script, or it can be executed from the command line as a script.
