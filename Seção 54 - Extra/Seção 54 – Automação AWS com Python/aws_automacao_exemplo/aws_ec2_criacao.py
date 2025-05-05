
# Exemplo: Criando uma instância EC2 com boto3 (simulado)

import boto3

def criar_instancia_ec2():
    # Crie um cliente EC2 com suas credenciais (reais ou via perfil configurado)
    ec2 = boto3.resource('ec2', region_name='us-east-1')

    print("Criando instância EC2...")

    # Simulação de chamada real
    instancia = ec2.create_instances(
        ImageId='ami-0c55b159cbfafe1f0',  # Exemplo Amazon Linux 2
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='sua-chave-ec2',  # Substitua pelo nome de sua key pair
        TagSpecifications=[{
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'InstanciaPythonGPT'}]
        }]
    )

    print("Instância criada. ID:", instancia[0].id)

# descomente para executar:
# criar_instancia_ec2()
