1. Create: `kubectl create -f nginx-rs.yaml`
2. `kubectl get po` or `kubectl get po -l tier=frontend`
3. `kubectl get rs nginx-rs -o wide`
4. `kubectl describe rs nginx-rs`
5. `kubectl scale rs nginx-rs --replicas=5`
6. `kubectl delete -f nginx-rs.yaml`