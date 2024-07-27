import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node artist
artist_node1722034642076 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ","}, connection_type="s3", format="csv", connection_options={"paths": ["s3://project-spotify-datewhitdata/staging/artists.csv"], "recurse": True}, transformation_ctx="artist_node1722034642076")

# Script generated for node album
album_node1722034642773 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ","}, connection_type="s3", format="csv", connection_options={"paths": ["s3://project-spotify-datewhitdata/staging/albums.csv"], "recurse": True}, transformation_ctx="album_node1722034642773")

# Script generated for node tracks
tracks_node1722034643438 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ","}, connection_type="s3", format="csv", connection_options={"paths": ["s3://project-spotify-datewhitdata/staging/track.csv"], "recurse": True}, transformation_ctx="tracks_node1722034643438")

# Script generated for node Join Album & Artist
JoinAlbumArtist_node1722034836808 = Join.apply(frame1=album_node1722034642773, frame2=artist_node1722034642076, keys1=["artist_id"], keys2=["id"], transformation_ctx="JoinAlbumArtist_node1722034836808")

# Script generated for node Join with tracks
Joinwithtracks_node1722035013519 = Join.apply(frame1=tracks_node1722034643438, frame2=JoinAlbumArtist_node1722034836808, keys1=["track_id"], keys2=["track_id"], transformation_ctx="Joinwithtracks_node1722035013519")

# Script generated for node Drop Fields
DropFields_node1722035052452 = DropFields.apply(frame=Joinwithtracks_node1722035013519, paths=["`.track_id`", "id"], transformation_ctx="DropFields_node1722035052452")

# Script generated for node Destination
Destination_node1722035112736 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1722035052452, connection_type="s3", format="glueparquet", connection_options={"path": "s3://project-spotify-datewhitdata/datawarehouse/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="Destination_node1722035112736")

job.commit()
