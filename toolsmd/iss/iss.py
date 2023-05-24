import requests
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import time


#%% FIRST API UTILISATION: FIND THE ISS


def show_iss_position():
    """Show where the ISS lies
    """
    ISS_now = requests.get('http://api.open-notify.org/iss-now.json')
    dic_ret = ISS_now.json()
    
    lat = float(dic_ret["iss_position"]["latitude"])
    lon = float(dic_ret["iss_position"]["longitude"])
    
    pt = gpd.GeoSeries(Point(lon,lat),crs="EPSG:4326")
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    
    ax = world.boundary.plot(color="black")
    pt.plot(ax=ax,color='blue')



#%% FIRST API UTILISATION: COMPUTE THE SPEED OF THE ISS


def get_iss_speed(approx = 5):
    """Compute the ISS speed

    Parameters
    ----------
    approx : int, optional
        Time interval to compute the speed, by default 5
    """
    iss_position = pd.DataFrame(columns = ["t","lat","lon"])
    
    for _ in range(2):
        
        ISS_now = requests.get('http://api.open-notify.org/iss-now.json')
        dic_ret = ISS_now.json()
        
        t = int(dic_ret["timestamp"])
        lat = float(dic_ret["iss_position"]["latitude"])
        lon = float(dic_ret["iss_position"]["longitude"])
        
        iss_position.loc[len(iss_position)] = [t,lat,lon]
    
        time.sleep(approx)
    
    iss_position["Point"] = [Point(coord) for coord in zip(
        iss_position["lon"],iss_position["lat"]
        )]
    
    geo = gpd.GeoDataFrame(iss_position,geometry="Point")
    geo = geo.set_crs("EPSG:4326")
    geo.to_crs(epsg=32663 ,inplace=True)
    
    time_span = geo.iloc[1,0]-geo.iloc[0,0]
    distance = geo.distance(geo.iloc[0,3])[1]
    
    print(f"The ISS has a speed of {round(distance/time_span,2)}m/s.")
    