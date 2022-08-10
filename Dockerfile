# pull base image
FROM golang:1.18.3 

# set working directory
WORKDIR /app

# copy project
COPY . .

COPY .kube /root/.kube

COPY .minikube /root/.minikube

# download cached requirements
RUN go mod download

EXPOSE 8080

ENTRYPOINT ["go","run","main.go"]