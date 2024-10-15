import boto3
import sys

ssm_client = boto3.client('ssm')

def update_ssm_parameter(parameter_name, new_value, parameter_type='String'):
    """Updates an SSM parameter value."""

    try:
        ssm_client.put_parameter(
            Name=parameter_name,
            Value=new_value,
            Type=parameter_type,
            Overwrite=True  # Set to True to overwrite the existing value
        )
        print(f"Parameter '{parameter_name}' updated successfully.")
    except Exception as e:
        print(f"Error updating parameter '{parameter_name}': {e}")

# Example usage
parameter_name = "/2020wa15340/DEBUG"
new_value = sys.argv[1]

update_ssm_parameter(parameter_name, new_value)

DjangoSecret = ssm_client.get_parameter(Name='/2020wa15340/blog_app_secret', WithDecryption=True)
DEBUG=ssm_client.get_parameter(Name='/2020wa15340/DEBUG', WithDecryption=True)

BS = f'SECRET={DjangoSecret["Parameter"]["Value"]}'
D = f"DEBUG={DEBUG['Parameter']['Value']}"

env_file = open("g2020wa15340/.env", "a")

data = "\n"+BS+"\n"+D

env_file.write(data)
env_file.close()
