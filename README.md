Aby pobrać i używać tego kodu lokalnie konieczne są następujące kroki:
1.	Skopiuj powyższy kod i zapisz go jako pliki o nazwach "app.py" i "models.py" odpowiednio.
2.	Zainstaluj wymagane narzędzia, takie jak Flask, SQLAlchemy, flask_sqlalchemy, flask_migrate oraz sqlite3, korzystając z narzędzi takich jak pip lub conda.
3.	Utwórz bazę danych SQLite o nazwie "books.db" w tym samym folderze, w którym znajdują się pliki "app.py" i "models.py".
4.	Uruchom terminal i przejdź do folderu, w którym znajdują się pliki "app.py" i "models.py".
5.	W terminalu wpisz następujące polecenia:
-	python models.py (spowoduje to utworzenie tabel w bazie danych)
-	python app.py (spowoduje to uruchomienie lokalnego serwera Flask)
6.	Po uruchomieniu serwera możesz korzystać z aplikacji, używając przeglądarki internetowej lub narzędzi do wysyłania żądań HTTP, takich jak Postman.
7.	Otwórz przeglądarkę internetową i odwiedź adres "http://localhost:5000/books", aby zobaczyć wszystkie książki w bazie danych.
8.	Możesz również korzystać z innych adresów URL i metod HTTP, takich jak "/books/{id}" (GET - pobranie konkretnej książki na podstawie identyfikatora), "/books" (POST - dodanie nowej książki), "/books/{id}" (PUT - aktualizacja istniejącej książki na podstawie identyfikatora) oraz "/books/{id}" (DELETE - usunięcie książki na podstawie identyfikatora).
9.	Możesz dostosować kod według własnych potrzeb, dodając lub usuwając funkcjonalności.

