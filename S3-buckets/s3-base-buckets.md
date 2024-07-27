## Data Storage Structure

The project uses an Amazon S3 bucket organized into two main folders: `staging` and `datawarehouse`. The `staging` folder holds raw CSV data files, while the `datawarehouse` folder stores the transformed data output in Parquet format.

![S3 Bucket Structure](../assets/s3_initial_buckets.png)

*Figure 1: S3 bucket structure showing folders for staging and data warehouse.*

The `staging` folder contains the initial data uploads, and after processing through AWS Glue, the cleaned and transformed data is saved in the `datawarehouse` folder.
