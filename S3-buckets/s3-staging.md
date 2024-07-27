## Data Ingestion

The initial data ingestion involves uploading raw data files in CSV format to the `staging` folder in Amazon S3. This folder serves as the landing area for raw data before it undergoes processing and transformation. Below is a screenshot of the `staging` folder containing the CSV files used in this project.

![Staging Folder](./assets/Staging-bucket-input-csv.png)

*Figure 4: S3 bucket showing the `staging` folder with CSV files for albums, artists, and tracks.*

These files contain the raw data necessary for the ETL pipeline, including information about songs, artists, and albums.
