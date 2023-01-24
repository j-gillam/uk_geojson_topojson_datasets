import altair as alt

def get_la_shapefiles_2019()->alt.Data:

    geojson_la = "https://raw.githubusercontent.com/j-gillam/uk_geojson_topojson_datasets/main/la_clean_shapefiles_2019.geojson"
    geodata_la = alt.Data(
                url=geojson_la, format=alt.DataFormat(property="features", type="json")
            )
    return geodata_la
