import folium
map_2 = folium.Map(location=[40, -99], zoom_start=4)
map_2.geo_json(geo_path=county_geo, data_out='data2.json', data=df,
                              columns=['GEO_ID', 'Unemployment_rate_2011'],
                              key_on='feature.id',
                              threshold_scale=[0, 5, 7, 9, 11, 13],
                              fill_color='YlGnBu', line_opacity=0.3,
                              legend_name='Unemployment Rate 2011 (%)',
                              topojson='objects.us_counties_20m')
map_2.create_map(path='map_2.html')
