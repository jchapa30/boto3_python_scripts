import boto3
import pprint

from boto3.session import Session 

sess =Session(region_name ='us-west-2')

ec2 = sess.client("ec2")

newvpc =ec2.create_vpc(CidrBlock="10.8.0.0/16")
pprint.pprint(newvpc)



