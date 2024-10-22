import geopandas as gpd

def testing_geometry(gdf):
    """
    Verifica y analiza las geometrías de un GeoDataFrame dado. Realiza las siguientes comprobaciones:
    
    1. Geometrías inválidas.
    2. Geometrías con áreas extremadamente pequeñas.
    3. Geometrías auto-intersectantes.
    4. Tipos de geometrías en el GeoDataFrame.
    5. Cantidad de MultiPolygons.
    6. Coordenadas mínimas y máximas (extensión de las geometrías).
    
    Args:
        gdf (geopandas.GeoDataFrame): El GeoDataFrame que contiene las geometrías a verificar.
        
    Returns:
        None: Imprime los resultados de las verificaciones directamente.
    """
    
    # Verificar geometrías inválidas
    gdf_invalid = gdf[~gdf.is_valid]
    print(f"Geometrías inválidas: {len(gdf_invalid)}")
    
    # Verificar geometrías con áreas extremadamente pequeñas
    small_geometries = gdf[gdf['geometry'].area < 1e-10]
    print(f"Geometrías con áreas pequeñas: {len(small_geometries)}")
    
    # Verificar geometrías auto-intersectantes
    auto_intersecting = gdf[gdf['geometry'].apply(lambda geom: geom.is_valid and geom.is_simple is False)]
    print(f"Geometrías auto-intersectantes: {len(auto_intersecting)}")
    
    # Verificar los tipos de geometrías
    geometry_types = gdf['geometry'].geom_type.value_counts()
    print(f"Tipos de geometrías en el GeoDataFrame:\n{geometry_types}")
    
    # Verificar la cantidad de multipolígonos
    multipolygons = gdf[gdf['geometry'].geom_type == 'MultiPolygon']
    print(f"Cantidad de MultiPolygons: {len(multipolygons)}")
    
    # Revisar coordenadas mínimas y máximas (extensión)
    bounds = gdf.total_bounds
    print(f"Extensión de las coordenadas: {bounds}")
