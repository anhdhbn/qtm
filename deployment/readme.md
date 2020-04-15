1. `kubectl create -f nginx-deploy.yaml`
2. `kubectl set image deploy nginx-deploy nginx-container=nginx:1.9.1`
3. `kubectl edit deploy nginx-deploy`
4. `kubectl rollout status deployment/nginx-deploy`
5. `kubectl get deploy`