eval $(minikube -p minikube docker-env)

docker build -t client-go:kubectl .

# 'helm install' for a new deployment
# 'helm upgrade' for a helm revision

helm install clientgo-helm clientgo-helm  -f ./clientgo-helm/values.yaml

kubectl config set-context --current --namespace=a

kubectl get all -n a