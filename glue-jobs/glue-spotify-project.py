import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Parse the arguments passed to the script
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Initialize Spark and Glue contexts
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Initialize the Glue job
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Extract data from the artists CSV file in S3
artist_node = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": "\"", "withHeader": True, "separator": ","},
    connection_type="s3",
    format="csv",
    connection_options={"paths": ["s3://project-spotify-datewhitdata/staging/artists.csv"], "recurse": True},
    transformation_ctx="artist_node"
)

# Extract data from the albums CSV file in S3
album_node = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": "\"", "withHeader": True, "separator": ","},
    connection_type="s3",
    format="csv",
    connection_options={"paths": ["s3://project-spotify-datewhitdata/staging/albums.csv"], "recurse": True},
    transformation_ctx="album_node"
)

# Extract data from the tracks CSV file in S3
tracks_node = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": "\"", "withHeader": True, "separator": ","},
    connection_type="s3",
    format="csv",
    connection_options={"paths": ["s3://project-spotify-datewhitdata/staging/track.csv"], "recurse": True},
    transformation_ctx="tracks_node"
)

# Join albums and artists data
join_album_artist = Join.apply(
    frame1=album_node,
    frame2=artist_node,
    keys1=["artist_id"],
    keys2=["id"],
    transformation_ctx="join_album_artist"
)

# Join with tracks data
join_with_tracks = Join.apply(
    frame1=tracks_node,
    frame2=join_album_artist,
    keys1=["track_id"],
    keys2=["track_id"],
    transformation_ctx="join_with_tracks"
)

# Drop unnecessary fields
drop_fields = DropFields.apply(
    frame=join_with_tracks,
    paths=["track_id", "id"],
    transformation_ctx="drop_fields"
)

# Write the transformed data back to S3 in Parquet format
glueContext.write_dynamic_frame.from_options(
    frame=drop_fields,
    connection_type="s3",
    format="glueparquet",
    connection_options={"path": "s3://project-spotify-datewhitdata/datawarehouse/", "partitionKeys": []},
    format_options={"compression": "snappy"},
    transformation_ctx="destination"
)

# Commit the Glue job
job.commit()
