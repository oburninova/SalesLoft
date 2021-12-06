# SalesLoft

## Flask App to call Public API deploy in EKS cluster using Docker image

## Features
- Flask app with Public API https://tradestie.com/api/v1/apps/reddit
- Docker image
- Kubernetes deployment manifests 

## Deployment steps
### Flask app with python code 
1. Install python3
2. Install the dependencies run "pip3 install -r requirements.txt"
3. Change directory to /app and run "*flask run*" or "*python3 app.py*" 
4. Head to the url shown in the logs to check API response 


### Build docker image
1. Download and run Docker 
2. Create docker repo to store image "oburninova/flask_app"
3. Head to the project directory and run "docker build --platform linux/amd64 -t oburninova/flask_app:v2 ."
4. After creating image run "docker push oburninova/flask_app:v2" to push image to repo
5. Run "docker run -p 4000:4000 oburninova/flask_app:v2*"
6. And open http://localhost:4000/ to check API response 

### Deploy deployment using docker image
1. Use the ELK cluster 
2. Create manifest file fo deplpyment nd NodePort service using NodePort 30007
3. Create deployment and service to run "kubectl apply -f kube.yaml" 
4. Open the port 30007 in your worker-nodes in EKS cluster 
5. Run "kubect get pods -o wide" to check the private IP of EC2 of the running pod
6. Check the public IP of the EC@ and open in http://publicIp:30007/
