## TERMINATE AN INSTANCE

# Now that we can programmatically create and list instances, we also need a method to terminate them.
# For this script, we’ll follow the same pattern as before with importing the boto3 library and creating an EC2 resource. 
# But we’ll also take one parameter: the ID of the instance to be terminated. 
# To keep things simple, we’ll consider any argument to the script to be an instance ID. 
# We’ll use that ID to get a connection to the instance from the EC2 resource and then call the terminate() function on that instance. 
# Finally, we print the response from the terminate function. Here’s what the script looks like:
###################################################################################################################
vi terminate.py
#!/usr/bin/env python
import sys
import boto3
ec2 = boto3.resource('ec2')
for instance_id in sys.argv[1:]:
    instance = ec2.Instance(instance_id)
    response = instance.terminate()
    print response
    
#############################################################################################################################
# Run the list_instances.py script to see what instances are available. 
# Note one of the instance IDs to use as input to the terminate_instances.py script.  
# After running the terminate script, we can run the list instances script to confirm the selected instance was terminated. 
# That process looks something like this:

$ ./list_instances.py
i-0c34e5ec790618146 {u'Code': 16, u'Name': 'running'}
$ ./terminate_instances.py i-0c34e5ec790618146
{u'TerminatingInstances': [{u'InstanceId': 'i-0c34e5ec790618146', u'CurrentState': {u'Code': 32, u'Name': 'shutting-down'}, u'PreviousState': {u'Code': 16, u'Name': 'running'}}], 'ResponseMetadata': {'RetryAttempts': 0, 'HTTPStatusCode': 200, 'RequestId': '55c3eb37-a8a7-4e83-945d-5c23358ac4e6', 'HTTPHeaders': {'transfer-encoding': 'chunked', 'vary': 'Accept-Encoding', 'server': 'AmazonEC2', 'content-type': 'text/xml;charset=UTF-8', 'date': 'Sun, 01 Jan 2017 00:07:20 GMT'}}}

$ ./list_instances.py
i-0c34e5ec790618146 {u'Code': 48, u'Name': 'terminated'}
