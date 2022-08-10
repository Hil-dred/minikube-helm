eval $(minikube -p minikube docker-env)

docker build -t todo-app:kubectl .

kubectl apply -f kubNamespace.yml

kubectl config set-context --current --namespace=a

kubectl apply -f kubDeployment.yml

kubectl get all -n a
