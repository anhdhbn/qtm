1. `gcloud container clusters create cluster-vpa --enable-vertical-pod-autoscaling --num-nodes=1 --zone=us-central1-c --machine-type="custom-4-4096"`
2. `gcloud container clusters get-credentials cluster-vpa --zone us-central1-c`
3. `kubectl apply -f deployment.yaml service.yaml vpa.yaml`
4. `kubectl get ep | grep 'backend-k8s-test-service' | awk -F' ' '{print $2}'`
5. `siege --time=3m 10.44.0.13:80/stress-test/10s-test/200`
6. `kubectl describe backend-k8s-test-vpa`
7. `kubectl describe vpa my-vpa`
8. `kubectl describe pod `