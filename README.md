Script to web scrap El Sotano's website with book's ID. Retrieves general information of the book anda adds columns to the existing list of books.
## INPUT 
Excel file with ISBN column to do the search.
## OUTPUT
Same input file with more columns.

### build
```
docker build -t book_names_web_scrap .
```
### run
```
docker run -it --rm -v book_names_web_scrap/:book_names_web_scrap/ book_names_web_scrap python /home/jovyan/work/web_s.py
```
