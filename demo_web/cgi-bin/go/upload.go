package main

import (
	"os"
	"io"
	"strings"
	"fmt"
	"net/http"
	"net/http/cgi"
)

func main() {

	if err := cgi.Serve(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		h := w.Header()
		h.Set("Content-Type", "text/plain; charset=utf-8")
		// in your case file would be fileupload
		file, header, err := r.FormFile("file")
		if err != nil {
			fmt.Fprintf(w, "Error %v\n", err)
			return
		}
		defer file.Close()
		name := strings.Split(header.Filename, ".")
		fmt.Fprintf(w, "Upload Success\n")
		fmt.Fprintf(w, "File name: %s\n", name[0])
		fmt.Fprintf(w, "File size: %d\n", header.Size)

		fmt.Fprintf(w, "%s", header.Filename)
		f, err := os.OpenFile("/var/www/html/files/" + header.Filename, os.O_WRONLY|os.O_CREATE, 0666)
		if err != nil {
			fmt.Println(err)
			return
		}
		defer f.Close()
		io.Copy(f, file)
	})); err != nil {
		return
	}
}
