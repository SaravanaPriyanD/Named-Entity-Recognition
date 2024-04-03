# Test GCLOUD connectivity by importing the zip file from GCP bucket to the test folder 
#(create test folder before running this test.py)
from ner.configuration.gcloud import GCloud

obj = GCloud()

obj.sync_folder_from_gcloud(gcp_bucket_url ="sara-ner-using-bert", filename="archive.zip", destination="test")
