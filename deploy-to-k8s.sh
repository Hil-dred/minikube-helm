eval $(minikube -p minikube docker-env)

docker build -t client-go:kubectl .

helm install  clientgo-helm clientgo-helm  -f ./clientgo-helm/values.yaml

kubectl config set-context --current --namespace=a

kubectl get all -n a