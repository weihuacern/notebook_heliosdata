package main

import (
	"fmt"
	"net/http"
	"net/http/cgi"
	"database/sql"
	_ "github.com/denisenkom/go-mssqldb"
	_ "github.com/go-sql-driver/mysql"
)

var	connString =
	fmt.Sprintf("root:Helios123@tcp(192.168.8.74:3306)/eval")

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
		course := r.FormValue("course")
		eval := r.FormValue("eval")

		if ssn != "" && course != "" && eval != "" {
			query := fmt.Sprintf("INSERT INTO evaluation values ('%s', '%s', '%s');",
								ssn, course, eval)

			db, err := sql.Open("mysql", connString)
			if err != nil {
				fmt.Fprintf(w, "Error connecting to DB\n")
				return
			}

			_, err = db.Query(query)
			if err != nil {
				 fmt.Fprintf(w, "Query error - %s\n", err)
				 return
			 }

			fmt.Fprintf(w, "Insert Success\n")
		} else {
			fmt.Fprintf(w, "Insufficient parameters\n")
		}
	})); err != nil {
		fmt.Println(err)
	}
}
