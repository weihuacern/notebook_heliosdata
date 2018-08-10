package main

import (
	"fmt"
	"net/http"
	"net/http/cgi"
	"database/sql"
	_ "github.com/denisenkom/go-mssqldb"
	_ "github.com/go-sql-driver/mysql"
)

var	registration_connString =
	fmt.Sprintf("server=192.168.8.155;user id=SA;password=Helios123;port=1433;database=registration")

var	eval_connString =
	fmt.Sprintf("root:Helios123@tcp(192.168.8.74:3306)/eval")

func printResult(rows *sql.Rows, w http.ResponseWriter) {
	cols, err := rows.Columns()
	if err != nil {
		fmt.Fprintf(w, "%s\n", err)
		return
	}
	columns := len(cols)
	for i := 0; i < columns; i++ {
		fmt.Fprintf(w, "%s\t", cols[i])
	}
	fmt.Fprintf(w, "\n")
	rawResult := make([][]byte, columns)
	result := make([]string, columns)
	dest := make([]interface{}, columns)

	for i := range rawResult {
		dest[i] = &rawResult[i] // Put pointers to each string in the interface slice
	}
	for rows.Next() {
		err = rows.Scan(dest...)
		if err != nil {
			fmt.Printf("Failed to scan row", err)
			return
		}

		for i, raw := range rawResult {
			if raw == nil {
				result[i] = ""
			} else {
				result[i] = string(raw)
			}
			fmt.Fprintf(w, "%s\t", result[i])
		}
		fmt.Fprintf(w, "\n")
	}


}

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

		if ssn != "" {
			registration_query := fmt.Sprintf("SELECT * FROM student where ssn = %s;", ssn)
			eval_query := fmt.Sprintf("SELECT * FROM evaluation where ssn = %s;", ssn)

			registration_db, err := sql.Open("mssql", registration_connString)
			if err != nil {
				fmt.Fprintf(w, "Error connecting to registration DB\n")
				return
			}

			eval_db, err := sql.Open("mysql", eval_connString)
			if err != nil {
				fmt.Fprintf(w, "Error connecting to eval DB\n")
				return
			}


			registration_rows, err := registration_db.Query(registration_query)
			if err != nil {
				fmt.Fprintf(w, "Registration Query error - %s\n", err)
				return
			}

			eval_rows, err := eval_db.Query(eval_query)
			if err != nil {
				fmt.Fprintf(w, "Evaluation Query error - %s\n", err)
				return
			}

			printResult(registration_rows, w)
			printResult(eval_rows, w)


			fmt.Fprintf(w, "Success\n")
		} else {
			fmt.Fprintf(w, "Insufficient parameters\n")
		}
	})); err != nil {
		fmt.Println(err)
	}
}
