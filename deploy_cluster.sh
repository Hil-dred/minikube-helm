eval $(minikube -p minikube docker-env)

docker build -t passwordmanager:kubectl .

kubectl apply -f kubNamespace.yml

kubectl config set-context --current --namespace=a

kubectl apply -f kubDeployment.yml

kubectl get all -n a
