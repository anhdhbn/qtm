1. Deploy metric server: `kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.3.6/components.yaml`
2. `kubectl get deployment metrics-server -n kube-system`
3. Deploy backend: `kubectl apply -f https://raw.githubusercontent.com/anhdhbn/qtm/master/horizontal-pod-autoscale/deployment.yaml`