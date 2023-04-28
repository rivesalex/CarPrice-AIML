# CarPrice-AIML
Simple demonstration of an end-to-end machine learning program.

These files are meant to hold the files required to run the application, further dependencies are required including aws-lightsail utilities as well as docker to containerize all of this.

If Another person wanted to create an app from this, they could simply use Docker.
Prior to running the command, the main.py file will need to be modified in the following way:
  The port would need to be changed from 80 to something more conventional like 5000. 
To containerize the application: Use Docker and run the following command on a terminal inside the root folder (inside Cars-V2).
"sudo docker build -t <name> ."
To run the image run the following command:
"sudo docker run -p 5000:5000 <name>
  
 SPECIFIC to Uploading this unto Amazon AWS Lightsail Services:::
1) Make sure that the user is authorized to upload information, this is done on the AWS module.
2) Provide Access keys by running "**aws configure**"
  
3) Run the following: 
  **sudo -E aws lightsail push-container-image --region <CONTAINER_REGION> --service-name <CONTAINER_SERVICE> --label <NAME> --image <DOCKER_NAME*>:<VERSION**>**
  *The DOCKER_NAME is likely the same name built above
  ** typically the most up to date version is denoted as 'latest'
 Sample AWS submission:
  **sudo -E aws lightsail push-container-image --region us-west-1 --service-name container-service-0 --label TEST --image car:latest**
  
 In my usage I had to use the -E prefix because various steps require sudo permision. This could be a consequence of how aws lightsail was installed. 



