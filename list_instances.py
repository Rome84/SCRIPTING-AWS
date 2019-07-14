# LIST INSTANCES
# For our first script, let’s list the instances we have running in EC2. We can get this information with just a few short lines of code.
# First, we’ll import the boto3 library. Using the library, we’ll create an EC2 resource. 
# This is like a handle to the EC2 console that we can use in our script. 
# Finally, we’ll use the EC2 resource to get all of the instances and then print their instance ID and state. 
# Here’s what the script looks like:
####################################################################################################################
vi list_instances.py
#!/usr/bin/env python
import boto3
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    print instance.id, instance.state
    
##########################################################################################################3
# Save the lines above into a file named list_instances.py and change the mode to executable. 
# That will allow you to run the script directly from the command line. 
# Also note that you’ll need to edit and chmod +x the remaining scripts to get them running as well. 
# In this case, the procedure looks like this:
#########################################################################################################
$ vi list_instances.py
$ chmod +x list_instances.py
$ ./list_instances.py
