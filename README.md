# FastAPI Login with Kubernetes Orchestration
### You will use:
- Docker
- Python 3.11
- Minikube

### How to run:
-  Run docker img:
    ```
    > docker build -t fastapi/login .
    > docker run -it fastapi/login /bin/bash
    > docker run -it --rm -p 8080:8001 fastapi/login

    ```
    *Navigate to:* localhost:8080/docs



-  Run with minikube:
    ```
    > minikube start
    > minikube image load fastapi/login
    > kubectl apply -f deployment.yml
    > kubectl get all
    > kubectl port-forward deployment/login-app 8001:8001

    ```
   *Navigate to:* localhost:8001/docs