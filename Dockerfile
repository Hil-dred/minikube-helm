#base image
FROM golang:1.18.3 

WORKDIR /app

COPY . .

RUN go mod download

EXPOSE 8080

ENTRYPOINT ["go","run","main.go"]