
import boto3 # importing boto3 module



dynamodb = boto3.resource('dynamodb',
    aws_access_key_id='AKIAZAH5VPJWGKJQL2MQ', #insert your aws_access_key_id
    aws_secret_access_key='PxMIO/XRzurmOm/BifkW3lhIJRNAmg4A/RwCCJjb') #insert your aws_secret_access_key
    

table = dynamodb.Table('Mascots') #variable to hold table name

with table.batch_writer() as batch: #batch writing 10 items
    
    batch.put_item(
        Item={
            'team_name': 'Atlanta Hawks',
            'mascot': 'Harry the Hawk'
            }
        )
    batch.put_item(
        Item={
           'team_name': 'Brooklyn Nets',
            'mascot': 'None'
            }
        )
    batch.put_item(
        Item={
            'team_name': 'Charlotte Hornets',
            'mascot': 'Hugo the Hornet'
            }
        )
    batch.put_item(
        Item={
            'team_name': 'Chicago Bulls',
            'mascot': 'Benny the Bull'
            }
        )
    batch.put_item(
        Item={
            'team_name': 'Cleveland Cavaliers',
            'mascot':  'Sir CC'
            }
        )
    batch.put_item(
        Item={
            'team_name': 'Dallas Mavericks',
            'mascot': 'Denver Nuggets'
            }
        )
    batch.put_item(
        Item={
            'team_name': 'Denver Nuggets',
            'mascot': 'Rocky the Mountain Lion'
            }
        )
    batch.put_item(
        Item={
            'team_name': 'Boston Celtics',
            'mascot': 'Lucky the Leprechaun'
            }
        )
    batch.put_item(
        Item={
            'team_name': 'Detroit Pistons',
            'mascot': 'Thunder'
            }
        )
    batch.put_item(
        Item={
            'team_name': 'Golden State Warriors',
            'mascot': 'Thunder'
            }
        ) 