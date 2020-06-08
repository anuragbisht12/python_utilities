# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 23:06:41 2020

@author: anurag
"""


#import libraries
import boto3
import pandas as pd
from nltk.corpus import stopwords


bucket='BUCKETLINK'
key='FOLDER/newfile.txt'
def download_from_s3():
#    resource = boto3.resource('s3') #high-level object-oriented API
#    my_bucket = resource.Bucket('my-bucket') #subsitute this for your s3 bucket name.
    client = boto3.client('s3')
    obj = client.get_object(Bucket=bucket, Key=key)
    df = pd.read_csv(obj['Body'])
    print(df)
    
#upload the file to s3 bucket

def upload_to_s3(file):
    s3 = boto3.resource('s3')
    data = open(file, "rb")
    key = file
    s3.Bucket(bucket).put_object(Key=key, Body=data)

if __name__ == '__main__':
    download_from_s3()
