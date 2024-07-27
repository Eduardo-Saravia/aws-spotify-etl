# aws-spotify-etl
Spotify Data ETL Pipeline with AWS

## Project Overview: Spotify Data ETL Pipeline using AWS

This project showcases an ETL (Extract, Transform, Load) pipeline built using Amazon Web Services (AWS) technologies, designed to process and analyze data from Spotify. The dataset, sourced from [Kaggle](https://www.kaggle.com/datasets/tonygordonjr/spotify-dataset-2023), contains comprehensive information about Spotify tracks and is used to demonstrate various data engineering skills and cloud services integration.

### Data Source
The Spotify dataset used in this project is publicly available on Kaggle and includes detailed information about songs, artists, and their popularity metrics. This dataset is ideal for exploring patterns in music data, conducting trend analysis, and deriving insights into the music industry.

### AWS Services Utilized
- **Amazon S3**: Used for data storage, staging, and as a data warehouse.
- **AWS Glue**: Implemented for the ETL process, transforming raw data into a structured format.
- **AWS Glue Crawler**: Automates the cataloging of data, making it easily accessible for querying.
- **Amazon Athena**: Facilitates SQL queries on the data stored in S3, enabling analysis without the need for complex ETL pipelines.
- **Amazon QuickSight**: Used for data visualization and creating interactive dashboards to provide insights from the data.

This project not only highlights the practical application of AWS services in data engineering but also serves as a template for building scalable and efficient data processing pipelines in the cloud.
