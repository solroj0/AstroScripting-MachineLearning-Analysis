from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive


def query_multi_star_systems():
    # Query the database for systems with more than one star
    query_result = NasaExoplanetArchive.query_criteria(table="ps", select="*", where="sy_snum > 1")

    # Check if there are any results
    if len(query_result) == 0:
        print("No multi-star systems found.")
        return

    # Get the column names and print them
    column_names = query_result.columns
    print("Column Headers:")
    for column_name in column_names:
        print(column_name)

if __name__ == "__main__":
    query_multi_star_systems()
