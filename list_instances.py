# LIST INSTANCES
# For our first script, let’s list the instances we have running in EC2. We can get this information with just a few short lines of code.
# First, we’ll import the boto3 library. Using the library, we’ll create an EC2 resource. 
# This is like a handle to the EC2 console that we can use in our script. 
# Finally, we’ll use the EC2 resource to get all of the instances and then print their instance ID and state. 
# Here’s what the script looks like:
####################################################################################################################
#!/usr/bin/env python
import boto3
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    print instance.id, instance.state
