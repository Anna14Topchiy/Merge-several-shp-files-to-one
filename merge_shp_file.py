import geopandas as gpd
import pandas as pd

# Пути к 12 файлам Shapefile
shapefile_paths = [
    r'C:\Users\annat\OneDrive\kasko\source_preparation_for_each_country\NL\drenthe-latest-free.shp\gis_osm_roads_free_1.shp',
    r'C:\Users\annat\OneDrive\kasko\source_preparation_for_each_country\NL\flevoland-latest-free.shp\gis_osm_roads_free_1.shp',
    r'C:\Users\annat\OneDrive\kasko\source_preparation_for_each_country\NL\friesland-latest-free.shp\gis_osm_roads_free_1.shp',
    r'C:\Users\annat\OneDrive\kasko\source_preparation_for_each_country\NL\gelderland-latest-free.shp\gis_osm_roads_free_1.shp',
    r'C:\Users\annat\OneDrive\kasko\source_preparation_for_each_country\NL\groningen-latest-free.shp\gis_osm_roads_free_1.shp',
    r'C:\Users\annat\OneDrive\kasko\source_preparation_for_each_country\NL\limburg-latest-free.shp\gis_osm_roads_free_1.shp',
    r'C:\Users\annat\OneDrive\kasko\source_preparation_for_each_country\NL\noord-brabant-latest-free.shp\gis_osm_roads_free_1.shp',
    r'C:\Users\annat\OneDrive\kasko\source_preparation_for_each_country\NL\noord-holland-latest-free.shp\gis_osm_roads_free_1.shp',
    r'C:\Users\annat\OneDrive\kasko\source_preparation_for_each_country\NL\overijssel-latest-free.shp\gis_osm_roads_free_1.shp',
    r'C:\Users\annat\OneDrive\kasko\source_preparation_for_each_country\NL\utrecht-latest-free.shp\gis_osm_roads_free_1.shp',
    r'C:\Users\annat\OneDrive\kasko\source_preparation_for_each_country\NL\zeeland-latest-free.shp\gis_osm_roads_free_1.shp',
    r'C:\Users\annat\OneDrive\kasko\source_preparation_for_each_country\NL\zuid-holland-latest-free.shp\gis_osm_roads_free_1.shp',
]

# Создаем GeoDataFrame для каждого Shapefile и добавляем их в список
gdfs = [gpd.read_file(shapefile) for shapefile in shapefile_paths]

# Объединяем GeoDataFrame
merged_gdf = gpd.GeoDataFrame(pd.concat(gdfs, ignore_index=True))

# Путь к файлу, в который будет сохранен объединенный Shapefile
output_path = r'C:\Users\annat\OneDrive\kasko\source_preparation_for_each_country\NL\scripts_for_git\merged_shapefile.shp'

# Сохраняем объединенный Shapefile
merged_gdf.to_file(output_path)

print(f'Объединенный Shapefile сохранен по пути: {output_path}')
