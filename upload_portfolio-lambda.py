import boto3
from botocore.client import Config
import zipfile
import StringIO
import mimetypes

s3 = boto3.resource('s3')

portfolio_bucket = s3.Bucket('content.colinw.pro')
build_bucket =s3.Bucket('build.colinw.pro')



portfolio_zip = StringIO.StringIO()
build_bucket.download_fileobj('portfoliobuild.zip', portfolio_zip)

with zipfile.ZipFile(portfolio_zip ) as myzip:
    for nm in myzip.namelist():
       obj = myzip.open(nm)
       portfolio_bucket.upload_fileobj(obj, nm,
       ExtraArgs={'ContentType': mimetypes.guess_type(nm)[1]})
       portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
