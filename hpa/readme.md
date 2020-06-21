1. `gcloud container clusters create cluster-hpa --num-nodes=1 --zone=us-central1-c --machine-type="custom-4-4096"`
2. Deploy backend: `kubectl apply -f https://raw.githubusercontent.com/anhdhbn/qtm/master/horizontal-pod-autoscaler/deployment.yaml`
3. Deploy service: `kubectl apply -f https://raw.githubusercontent.com/anhdhbn/qtm/master/horizontal-pod-autoscaler/service.yaml`
4. `kubectl get po -o wide` to get node
5. `kubectl get ep | grep 'backend-k8s-test-service' | awk -F' ' '{print $2}'`
6. `siege --time=3m 10.44.0.13:80/stress-test/200`
7. `kubectl create -f https://raw.githubusercontent.com/anhdhbn/qtm/master/horizontal-pod-autoscaler/hpa.yaml`
8. `kubectl autoscale deployment/backend-k8s-test --cpu-percent=80 --min=1 --max=3`
9. `watch kubectl get hpa`

<!-- 1. Deploy metric server: `kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.3.6/components.yaml`
2. `kubectl get deployment metrics-server -n kube-system` -->