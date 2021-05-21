from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.job import Job 
import sys
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame 

glueContext = GlueContext(SparkContext.getOrCreate())
glueJob = Job(glueContext)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

glueJob.init(args['JOB_NAME'], args)
sparkSession = glueContext.sparkSession

## ETL
users_spark_df = sparkSession.read.format("jdbc") \
	.option("url", "jdbc:mysql://www.db4free.net:3306/glue_test") \
	.option("driver", "com.mysql.jdbc.Driver") \
	.option("dbtable", "users") \
	.option("user", "Yingquan") \
	.option("password", "1234") \
	.load()

print ("Users count", users_spark_df.count())

## SPARK DF -> DYNAMIC DF
users_dynamic_df = DynamicFrame.fromDF(
	users_spark_df, 
	glueContext,
	"convert_ctx"
)

## S3 WRITE
glueContext.write_dynamic_frame.from_options(
	frame = users_dynamic_df,
	connection_type = "s3",
	connection_options = ("path", "s3://z-celcey-glue/job_extracts/mysql/"),
	format = "parquet",
	transformation_ctx = "transformation_ctx"
)

glueJob.commit()
