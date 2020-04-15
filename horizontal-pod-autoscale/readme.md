1. Deploy metric server: `kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.3.6/components.yaml`
2. `kubectl get deployment metrics-server -n kube-system`
3. Deploy backend: `kubectl apply -f https://raw.githubusercontent.com/anhdhbn/qtm/master/horizontal-pod-autoscale/deployment.yaml`
4. Deploy service: `kubectl apply -f https://raw.githubusercontent.com/anhdhbn/qtm/master/horizontal-pod-autoscale/service.yaml`
4. `kubectl get po -o wide` to get node
4. `kubectl get ep | grep 'backend-k8s-test-service' | awk -F' ' '{print $2}'`
5. `siege --time=3m 10.44.0.13:80/stress-test/10s-test/200`
6. `kubectl create -f https://raw.githubusercontent.com/anhdhbn/qtm/master/horizontal-pod-autoscale/hpa.yaml`
8. `kubectl autoscale deployment/backend-k8s-test --cpu-percent=80 --min=1 --max=20`
7. `watch kubectl get hpa`