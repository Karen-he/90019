# This code is written by Team 6:
# Yi Ding, 839679
# Jianying Zhang, 799672
# Feifan Zhang, 807480
# Keren He, 865255
# Jinhang Li, 867117
import boto
from boto.ec2.regioninfo import RegionInfo
import time

region = RegionInfo(name='melbourne', endpoint='nova.rc.nectar.org.au')
ec2_conn = boto.connect_ec2(aws_access_key_id='11eca0526900499093ebf6f75efc4618',
aws_secret_access_key='e18baa778e0e444a9d1b74bffaa0663e',
is_secure=True,
region=region,
port=8773,
path='/services/Cloud',
validate_certs=False)
print("Start creating new instance")
reservation =ec2_conn.run_instances(
    'ami-00003837',
    key_name='sweet-heart-pub',
    instance_type='m1.small',
    security_groups=['default','ssh'],
    placement='melbourne-qh2',
)
instance=reservation.instances[0]

print('New isntance {} has been created.'.format(instance.id))

#check if instance is runing
while instance.state!='running':
    print('instance {} is {}'.format(instance.id,instance.state))
    time.sleep(5)
    instance.update()

# write the host ip_address as a file for ansible to implement
hostPath = "playbook/inventory.ini"
with open(hostPath, 'w') as f:
    content = "[Nectarhost]\n"+instance.private_ip_address
    f.write(content)
print("server: "+instance.private_ip_address+
      " has been write in to ansible inventory.ini , please run ansible script to deploy the twiter harvester")