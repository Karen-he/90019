import fiona
from shapely.geometry import Point, shape

# read shape file
melb_surburbs = fiona.open("Output__spatialise-dataset_Oct-01_23_05/shp/055ec0bd-7e70-4046-b030-125507584bd2.shp", 'r')

print("Origin_Total:", len(melb_surburbs))

# build suburb dictionary
melb_sub_Dict = {}
for i in range(len(melb_surburbs)):
    subBoundary = shape(melb_surburbs[i]['geometry'])
    melb_sub_Dict[melb_surburbs[i]['properties']['lga_name']] = subBoundary

print("Total", len(melb_sub_Dict))
# print("Dictionary: ", melb_sub_Dict)

# give label of suburb
def give_suburb(coordinates):
    if coordinates:
        point = Point(coordinates)
        for item in melb_sub_Dict:
            if point.within(melb_sub_Dict[item]):
                suburb = item
                return suburb
