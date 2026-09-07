The Haversine distance is a distance measure used for calculating the shortest distance between two points on the surface of a sphere, given their latitudes and longitudes.

Let:
* $\phi_1$, $\phi_2$ = latitudes of the two points (in radians)
* $\lambda_1$, $\lambda_2$ = longitudes of the two points (in radians)
* $R$ = radius of the sphere
	* Earth $\approx$ 6378 km = 3963 mi 
* $\Delta \phi = \phi_2 - \phi_1$
* $\Delta \lambda = \lambda_2 - \lambda_1$

The Haversine distance $d$ is given by:
$$d = 2R\arcsin(\sqrt{\sin^2(\frac{\Delta \phi}{2})+\cos(\phi_1)cos(\phi_2)\sin^2(\frac{\Delta \lambda}{2})})$$

---

> [!example]
> Coordinates of Denver Union Station (39.7528°N, -105°E)
> Coordinates of Eiffel Tower (48.8579°N, 2.2947°E)
> 
> What is the Haversine distance between the two?
> 
> In Radians:
> * $\phi_1 = 0.69382$
> * $\phi_2 = 0.85273$
> * $\lambda_1 = -1.83259$
> * $\lambda_2 = 0.04005$
> * $\Delta \phi = 0.15891$
> * $\Delta \lambda = 1.87265$
> 
> Using Radius $R=6378$ km. Plugging into the Haversine distance equation gives
> $$d = 7865.46 \text{ km}$$