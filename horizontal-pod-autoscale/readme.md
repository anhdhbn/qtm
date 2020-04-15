1. Deploy metric server: `kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.3.6/components.yaml`
2. `kubectl get deployment metrics-server -n kube-system`
3. Deploy backend: `kubectl apply -f https://raw.githubusercontent.com/anhdhbn/qtm/master/horizontal-pod-autoscale/deployment.yaml`
4. `kubectl get po -o wide` to get node
4. `kubectl get ep | grep 'backend-k8s-test-service' | awk -F' ' '{print $2}'`
5. `siege --time=1H 10.4.2.3:80/stress-test/10s-test/10`
6. `kubectl create -f https://raw.githubusercontent.com/anhdhbn/qtm/master/horizontal-pod-autoscale/hpa.yaml`
7. `watch kubectl get hpa`