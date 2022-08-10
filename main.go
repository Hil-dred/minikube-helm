package main

import (
	"context"
	"flag"
	"fmt"
	"path/filepath"

	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/tools/clientcmd"
	"k8s.io/client-go/util/homedir"

	"net/http"
	"log"
)

func main() {
	var kubeconfig *string
	if home := homedir.HomeDir(); home != "" {
		kubeconfig = flag.String("kubeconfig", filepath.Join(home, ".kube", "config"), "(optional) absolute path to the kubeconfig file")
	} else {
		kubeconfig = flag.String("kubeconfig", "", "absolute path to the kubeconfig file")
	}
	flag.Parse()

	// use the current context in kubeconfig
	config, err := clientcmd.BuildConfigFromFlags("", *kubeconfig)
	if err != nil {
		panic(err.Error())
	}

	// create the clientset
	clientset, err := kubernetes.NewForConfig(config)
	if err != nil {
		panic(err.Error())
	}

	//HTTP ENDPOINTS
	http.HandleFunc("/index", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprint(w, "\nHello World, Welcome to my Cluster.\n")
		fmt.Fprint(w, "\n\nService is powered by Go")
	})

	http.HandleFunc("/podnames", func(w http.ResponseWriter, r *http.Request) {

		fmt.Fprintf(w, "\n\nNAMESPACE A\n")

		podlist, e := clientset.CoreV1().Pods("a").List(context.TODO(), metav1.ListOptions{})
		if e !=nil{
			fmt.Fprintf(w, "\n\nERROR OCCURED, SEE REASON BELOW\n")
			fmt.Fprintf(w, e.Error())
		}

		for _, p := range podlist.Items {
			podname := p.GetName() + "\n"
			fmt.Fprintf(w, podname)

		}

	})


	//HTTP SERVER
	fmt.Printf("Starting server at port 8080\n")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatal(err)
	}
}