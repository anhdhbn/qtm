1. Deploy metric server: `kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.3.6/components.yaml`
2. `kubectl get deployment metrics-server -n kube-system`