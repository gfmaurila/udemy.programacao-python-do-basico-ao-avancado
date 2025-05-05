# Backup programado de EC2 (simulado)
import boto3

def criar_snapshot(instancia_id):
    ec2 = boto3.client('ec2')
    volumes = ec2.describe_instances(InstanceIds=[instancia_id])
    print("Backup simulado para instância:", instancia_id)

# criar_snapshot('i-1234567890abcdef0')