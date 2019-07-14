## CREATE AN INSTANCE

# One of the key pieces of information we need for scripting EC2 is an Amazon Machine Image (AMI) ID. 
# This will let us tell our script what type of EC2 instance to create. 
# While getting an AMI ID can be done programmatically, that's an advanced topic beyond the scope of this tutorial. 
# For now, let’s go back to the AWS console and get an ID from there.
# In the AWS console, go the the EC2 service and click the “Launch Instance” button. 
# On the next screen, you’re presented with a list of AMIs you can use to create instances. 
# Let’s focus on the Amazon Linux AMI at the very top of the list. Make a note of the AMI ID to the right of the name. 
# In this example, its “ami-1e299d7e." That’s the value we need for our script. 
# Note that AMI IDs differ across regions and are updated often so the latest ID for the Amazon Linux AMI may be different for you.

# After Chosing an Amazon machine Image from AWS console Management, let's proceed with the following.
# Now with the AMI ID, we can complete our script. 
# Following the pattern from the previous script, we’ll import the boto3 library and use it to create an EC2 resource. 
# Then we’ll call the create_instances() function, passing in the image ID, max and min counts, and the instance type. 
# We can capture the output of the function call which is an instance object. 
# For reference, we can print the instance’s ID.
########################################################################################################################
vi create_instances.py
#!/usr/bin/env python
import boto3
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId='ami-1e299d7e',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro')
print instance[0].id

########################################################################################################################
# While the command will finish quickly, it will take some time for the instance to be created. 
# Run the list_instances.py script several times to see the state of the instance change from pending to running.
