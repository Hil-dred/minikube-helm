package main

import (
	"context"
	"fmt"

	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes"

	//"k8s.io/client-go/tools/clientcmd"
	"k8s.io/client-go/rest"

	"log"
	"net/http"
)

func main() {

	// rules := clientcmd.NewDefaultClientConfigLoadingRules()
	// configOverrides := &clientcmd.ConfigOverrides{}
	// kubeconfig := clientcmd.NewNonInteractiveDeferredLoadingClientConfig(rules, configOverrides)
	// config, err := kubeconfig.ClientConfig()
	config, err := rest.InClusterConfig()

	if err != nil {
		panic(err)
	}
	clientset := kubernetes.NewForConfigOrDie(config)

	if err != nil {
		panic(err)
	}

	//HTTP SERVER
	http.HandleFunc("/podnames", func(w http.ResponseWriter, r *http.Request) {

		fmt.Fprint(w, "\nCONFIG \n")
		fmt.Fprint(w, config)
		fmt.Fprintf(w, "\n\nNAMESPACE A\n")

		for _, p := range podlist.Items {
			podname := p.GetName() + "\n"
			fmt.Fprintf(w, podname)

		}

	})

	fmt.Printf("Starting server at port 8080\n")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatal(err)
	}

}
