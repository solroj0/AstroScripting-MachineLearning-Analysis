from astroquery.nasa_exoplanet_archive import NasaExoplanetArchive

def query_multi_star_systems_and_write_to_file(filename):
    # Query the database for systems with more than one star
    query_result = NasaExoplanetArchive.query_criteria(table="ps", select="*", where="sy_snum > 1")

    # Check if there are any results
    if len(query_result) == 0:
        print("No multi-star systems found.")
        return

    # Open the file for writing
    with open(filename, "w") as file:
        # Write column headers
        file.write("\t".join(query_result.columns) + "\n")
        
        # Write each row to the file
        for row in query_result:
            file.write("\t".join(map(str, row)) + "\n")

if __name__ == "__main__":
    output_filename = "multi_star_systems.txt"
    query_multi_star_systems_and_write_to_file(output_filename)
    print(f"Query results written to {output_filename}")
