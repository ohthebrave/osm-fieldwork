from io import BytesIO
from osm_fieldwork.basemapper import create_basemap_file

with open("/Users/gijo/Development/Material/outreachy/osm-fieldwork/data.geojson", "rb") as geojson_file:
    boundary = geojson_file.read()  # read as a `bytes` object.
    boundary_bytesio = BytesIO(boundary)   # add to a BytesIO wrapper

# Check if boundary_bytesio is an instance of BytesIO
if isinstance(boundary_bytesio, BytesIO):
    create_basemap_file(
        verbose=True,
        boundary=boundary_bytesio,
        outfile="outreachy.mbtiles",
        zooms="12-15",
        source="esri",
    )
else:
    print("Error: boundary_bytesio is not a BytesIO object.")
