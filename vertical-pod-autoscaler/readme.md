1. `gcloud container clusters create cluster-vpa --enable-vertical-pod-autoscaling --num-nodes=1 --zone=us-central1-c --machine-type="custom-4-4096"`
2. `gcloud container clusters get-credentials cluster-vpa --zone us-central1-c`
3. `kubectl apply -f deployment-auto.yaml`
3. `kubectl apply -f vpa-auto.yaml`
4. `kubectl describe vpa my-vpa`
5. `kubectl describe pod ...`