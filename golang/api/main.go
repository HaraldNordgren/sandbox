package main

import (
    "fmt"
    "html"
    "log"
    "net/http"
)

func root (w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello, %q", html.EscapeString(r.URL.Path))
}

func yo (w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Yoyo, %q", html.EscapeString(r.URL.Path))
}

func main() {
	http.HandleFunc("/hej", yo)
    http.HandleFunc("/", root)

    log.Fatal(http.ListenAndServe(":8080", nil))

}