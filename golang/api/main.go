A. Commit message:
Implement HTTP server timeouts to prevent resource exhaustion attacks

B. Change summary:
Replaced the default `http.ListenAndServe` call with a custom `http.Server` instance incorporating `ReadHeaderTimeout`, `ReadTimeout`, `WriteTimeout`, and `IdleTimeout` to mitigate potential slow
HTTP attack vectors.

C. Compatibility Risk:
Medium

D. Fixed Code:
```go
package main

import (
    "fmt"
    "html"
    "log"
    "net/http"
    "time"
)

func root(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello, %q", html.EscapeString(r.URL.Path))
}

func yo(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Yoyo, %q", html.EscapeString(r.URL.Path))
}

func main() {
    http.HandleFunc("/hej", yo)
    http.HandleFunc("/", root)

    srv := &http.Server{
        Addr:              ":8080",
        ReadHeaderTimeout: 15 * time.Second,
        ReadTimeout:       15 * time.Second,
        WriteTimeout:      10 * time.Second,
        IdleTimeout:       30 * time.Second,
        Handler:           nil,
    }

    log.Fatal(srv.ListenAndServe())
}
```