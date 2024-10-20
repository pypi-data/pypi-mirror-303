"""
Database queries for Mega Pack PBF Parser project.
"""

get_product_pbf_name_dict_query = """
select pbf_name, product from packs_pbf_type where pbf_name IS NOT NULL;
"""

get_total_song_count = """
SELECT count(song_name) as song_count
FROM songs
WHERE pbf_name NOT IN (?,?,?);
"""

insert_songs_query = """INSERT OR IGNORE INTO songs (pbf_name, song_name, product_name, type) VALUES(?,?,?,?);"""

song_names_query = """
SELECT product_name, song_name FROM songs
WHERE pbf_name NOT IN (
'GM_Ballads_Brushes', 'GM_Ballads_Crashes', 'GM_Classic_Rock_OPP', 
'GM_Country_Outlaws_OPP', 'GM_Funk_HH_RB_DanceKit', 'GM_Garage_Rock_OPP',
'GM_Police_OPP', 'GM_Southern_Rock_OPP'
);
"""

songs_per_pbf_query = """
SELECT product_name, pbf_name, COUNT(song_name)
FROM songs
GROUP BY pbf_name;
"""

song_count_by_product = """
WITH s1 AS (
SELECT product_name, song_name FROM songs
WHERE pbf_name NOT IN (
'GM_Ballads_Brushes', 'GM_Ballads_Crashes',  
 'GM_Funk_HH_RB_DanceKit')
)

SELECT product_name as Product, COUNT(song_name) as Songs
FROM s1
GROUP BY product_name;
"""