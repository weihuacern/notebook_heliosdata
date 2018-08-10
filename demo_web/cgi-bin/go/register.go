package main

import (
	"fmt"
	"net/http"
	"net/http/cgi"
	"database/sql"
	_ "github.com/denisenkom/go-mssqldb"
)

var	connString =
	fmt.Sprintf("server=192.168.8.155;user id=SA;password=Helios123;port=1433;database=registration")

func main() {

	if err := cgi.Serve(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		header := w.Header()
		header.Set("Content-Type", "text/plain; charset=utf-8")

		r.ParseForm()
		form := r.Form
		fmt.Fprintf(w, "Form Input values:\n")
		for k := range form {
			fmt.Fprintln(w, "\tForm Value", k+":", form.Get(k))
		}
		fmt.Fprintf(w, "\n\n")

		ssn := r.FormValue("ssn")
		name := r.FormValue("name")
		phone := r.FormValue("phone")

		if ssn != "" && name != "" && phone != "" {
			query := fmt.Sprintf("INSERT INTO student values ('%s', '%s', '%s');",
								ssn, name, phone)

			db, err := sql.Open("mssql", connString)
			if err != nil {
				fmt.Fprintf(w, "Error connecting to DB\n")
				return
			}

			_, err = db.Query(query)
			if err != nil {
				 fmt.Fprintf(w, "Query error - %s\n", err)
				 return
			 }
			 defer db.Close()

			fmt.Fprintf(w, "Insert Success\n")
		} else {
			fmt.Fprintf(w, "Insufficient parameters\n")
		}
	})); err != nil {
		fmt.Println(err)
	}
}
