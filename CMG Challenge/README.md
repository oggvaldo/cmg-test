# CMG Challenge

Write a program that takes the contents of the [sample log file](python/sample.log), and outputs the devices and their classification. The solution should run in a Container environment.

## Classifications

### Thermometer

- It is branded “ultra precise” if the mean of the readings is within 0.5 degrees of the known temperature, and the standard deviation is less than 3
- It is branded “very precise” if the mean is within 0.5 degrees of the room, and the standard deviation is under 5
- Otherwise, it’s sold as “precise”.

### Humidity

- It must be discarded unless it is within 1 humidity percent of the reference value for all readings. (All humidity sensor readings are a decimal value representing percent moisture saturation.)

### How it works
The code will read on the first line the references to determine which should be the precision for the thermometer and if the humidity is correctly read or not. If yes, the classifications will be applied. 


### How to execute
To execute it on local env, if you want to test just the code, simply run the following command:
``python3 test.py``

The sample log should be on the same local from the python code to be able to read.

To execute it from Docker, just build the docker image and run it normally ``docker build -t cmg-test/test:latest . `` or ``docker run cmg-test``.

To execute it as helm chart, just run the following command:
- helm install cmg-test helm/

To deploy it using Terraform, first we need the values to redirect it into the current cluster on AKS, them we can just apply the following codes:
- ``terraform init``
- ``terraform plan``
- ``terraform apply``

Don't forget to run these commands from the terraform-aks-folder. This will create the cluster where the test application can be deployed.
After this, set the cluster and context on kubectl to deploy the application there, using the following commands:

- ``kubectl config set-cluster <nameofthecluster>``
- ``kubectl config set-context <nameofthecontext>``

After set the environment, just deploy the application using the (not properly working) deployment.yaml:

- ``kubectl apply -f Kubernetes/deployment.yaml``

### To do:
I'm still trying to create the kubernetes manifests/helm chart to use with this test, but we can see that it is more suitable to add this as a job instead a deployment. If I can adjust this in time, we can run this application running without use so much resources. But, for the moment, the terraform files, dockerfile and the application itself is running fine. 