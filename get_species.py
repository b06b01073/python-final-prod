
from importlib_metadata import install
import geopandas as gpd
import geohash as gh
import shapely.geometry as sp


def get_area_data(filename, lat, lon):

    ### get the species data that intersects with the entered lat/lon
    ### takes latitude and longitude coordinates and a filename with the data to search from
    ### returns a geodataframe with the species in this area and their ranges

    prec = 6    ## set the precision - how tight is the bounding box

    # make a bounding box based on location
    geocode = gh.encode(lat, lon, prec)
    gh_bbox = gh.bbox(geocode)
    bounds = (gh_bbox['w'], gh_bbox['s'], gh_bbox['e'], gh_bbox['n'])
    # get the records that intersect with bounding box
    my_area = gpd.read_file(filename, bbox=bounds)

    return(my_area)

def get_url(area, lat, lon):

    ### get the urls and species names from the species area data
    ### filters the area to make sure all the species are actually present and there are no repeats
    ### takes a geodataframe with species information + the latitude and longitude location
    ### returns a list of lists in format [[url1, name1], [url2,name2],...]

    point = sp.Point(lon, lat)

    base_url = 'https://www.iucnredlist.org/species/'
    info = []
    for i in range(len(area)):
        try:
            # check if species range actually overlaps with the location
            if point.within(area['geometry'][i]):
                url = base_url + str(int(area['ID_NO'][i])) + '/' + str(int(area['ASSESSMENT'][i]))
                name = area['BINOMIAL'][i]
                info.append([url,name])
        except:
            fixed = area['geometry'][i].buffer(0) # fix the 'invalid shape' error
            if point.within(fixed):
                url = base_url + str(int(area['ID_NO'][i])) + '/' + str(int(area['ASSESSMENT'][i]))
                name = area['BINOMIAL'][i]
                info.append([url,name])
    no_rep_info = []
    [no_rep_info.append(i) for i in info if i not in no_rep_info] # get rid of repeats
    return(no_rep_info)
    
def loop_files(files, lat, lon):

    ### run the functions for multiple status - vulnerable, endangered, etc.
    ### files - a list of filenames based on the statuses the user selects
    ### takes list of filenames and a latitude and longitude location
    ### returns a list of lists in format [[url1, name1], [url2,name2],...]

    info = []
    for i in range(len(files)):
        area = get_area_data(files[i],lat,lon)
        [info.append(j) for j in get_url(area,lat,lon)]
    return(info)
