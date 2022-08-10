eval $(minikube -p minikube docker-env)

docker build -t client-go:kubectl .

kubectl apply -f client-go-KubDeploy.yml

kubectl config set-context --current --namespace=a

kubectl get all -n a