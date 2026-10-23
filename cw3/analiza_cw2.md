# Analiza testów – ćwiczenie 3

## B1. Specyfikacja

Testy zostały przygotowane na podstawie pliku `SPECYFIKACJA.md`. Zastosowano techniki klas równoważności (EP) oraz analizy wartości brzegowych (AWB). Kod źródłowy funkcji z pakietu `sut` nie był analizowany.

## B2. Klasy równoważności (EP)

### 1. grade_from_percent

| Klasa | Opis | Rodzaj | Wartość | Oczekiwany wynik |
|---|---|---|---|---|
| OC-K1 | 0–50% | poprawna | 25 | 2.0 |
| OC-K2 | 51–60% | poprawna | 55 | 3.0 |
| OC-K3 | 61–70% | poprawna | 65 | 3.5 |
| OC-K4 | 71–80% | poprawna | 75 | 4.0 |
| OC-K5 | 81–90% | poprawna | 85 | 4.5 |
| OC-K6 | 91–100% | poprawna | 95 | 5.0 |
| OC-N1 | Poniżej 0 | niepoprawna | -10 | ValueError |
| OC-N2 | Powyżej 100 | niepoprawna | 110 | ValueError |
| OC-N3 | Typ float | niepoprawna | 50.5 | TypeError |
| OC-N4 | Typ str | niepoprawna | "50" | TypeError |
| OC-N5 | Typ None | niepoprawna | None | TypeError |
| OC-N6 | Typ bool | niepoprawna | True | TypeError |

### 2. parking_fee

| Klasa | Opis | Rodzaj | Wartość | Oczekiwany wynik |
|---|---|---|---|---|
| PK-K1 | 0–15 min | poprawna | 10 | 0.0 |
| PK-K2 | 16–60 min | poprawna | 30 | 5.0 |
| PK-K3 | 61–120 min | poprawna | 90 | 10.0 |
| PK-K4 | 121–180 min | poprawna | 150 | 15.0 |
| PK-K5 | 181–1440 min | poprawna | 600 | 20.0 |
| PK-N1 | Poniżej 0 | niepoprawna | -10 | ValueError |
| PK-N2 | Powyżej 1440 | niepoprawna | 1500 | ValueError |
| PK-N3 | Typ float | niepoprawna | 15.5 | TypeError |
| PK-N4 | Typ str | niepoprawna | "60" | TypeError |
| PK-N5 | Typ bool | niepoprawna | True | TypeError |

### 3. validate_password

| Klasa | Opis | Rodzaj | Wartość | Oczekiwany wynik |
|---|---|---|---|---|
| HS-K1 | Poprawna długość, litery i cyfry | poprawna | "haslo123" | True |
| HS-K2 | Znaki specjalne | poprawna | "haslo12!" | True |
| HS-K3 | Spacje w haśle | poprawna | "moje haslo1" | True |
| HS-K4 | Polskie litery | poprawna | "żółw1234" | True |
| HS-N1 | Mniej niż 8 znaków | niepoprawna | "abc123" | False |
| HS-N2 | Więcej niż 20 znaków | niepoprawna | "abcdefghij12345678901" | False |
| HS-N3 | Brak litery | niepoprawna | "12345678" | False |
| HS-N4 | Brak cyfry | niepoprawna | "abcdefgh" | False |
| HS-N5 | Typ int | niepoprawna | 12345678 | TypeError |
| HS-N6 | Typ None | niepoprawna | None | TypeError |

### 4. ticket_price

| Klasa | Opis | Rodzaj | Wartość | Oczekiwany wynik |
|---|---|---|---|---|
| BL-K1 | 0–6 lat | poprawna | 3 | 0.0 |
| BL-K2 | 7–18 lat | poprawna | 12 | 10.0 |
| BL-K3 | 19–64 lat | poprawna | 40 | 20.0 |
| BL-K4 | 65–120 lat | poprawna | 70 | 10.0 |
| BL-N1 | Poniżej 0 | niepoprawna | -5 | ValueError |
| BL-N2 | Powyżej 120 | niepoprawna | 125 | ValueError |
| BL-N3 | Typ float | niepoprawna | 18.5 | TypeError |
| BL-N4 | Typ str | niepoprawna | "18" | TypeError |
| BL-N5 | Typ None | niepoprawna | None | TypeError |
| BL-N6 | Typ bool | niepoprawna | True | TypeError |

### Wnioski

Podział na klasy równoważności pozwala sprawdzić różne rodzaje danych wejściowych bez testowania każdej możliwej wartości. Dla każdej klasy wybrano reprezentatywny przykład i określono oczekiwany wynik na podstawie specyfikacji.


## B3. Analiza wartości brzegowych (AWB)

W testach zastosowano analizę wartości brzegowych 2-punktową (2p) i 3-punktową (3p). Wartości oczekiwane ustalono na podstawie specyfikacji.

### 1. grade_from_percent

Precyzja: 1 punkt procentowy.

| Granica | 2p | 3p – dodatkowo | Oczekiwane |
|---|---|---|---|
| Początek zakresu | -1, 0 | 1 | ValueError, 2.0, 2.0 |
| 50/51 | 50, 51 | 49, 52 | 2.0, 3.0, 2.0, 3.0 |
| 60/61 | 60, 61 | 59, 62 | 3.0, 3.5, 3.0, 3.5 |
| 70/71 | 70, 71 | 69, 72 | 3.5, 4.0, 3.5, 4.0 |
| 80/81 | 80, 81 | 79, 82 | 4.0, 4.5, 4.0, 4.5 |
| 90/91 | 90, 91 | 89, 92 | 4.5, 5.0, 4.5, 5.0 |
| Koniec zakresu | 100, 101 | 99 | 5.0, ValueError, 5.0 |

Pokrycie: 2p – 14 wartości, 3p – 26 wartości łącznie.

### 2. parking_fee

Precyzja: 1 minuta.

| Granica | 2p | 3p – dodatkowo | Oczekiwane |
|---|---|---|---|
| Początek zakresu | -1, 0 | 1 | ValueError, 0.0, 0.0 |
| 15/16 | 15, 16 | 14, 17 | 0.0, 5.0, 0.0, 5.0 |
| 60/61 | 60, 61 | 59, 62 | 5.0, 10.0, 5.0, 10.0 |
| 120/121 | 120, 121 | 119, 122 | 10.0, 15.0, 10.0, 15.0 |
| 180/181 | 180, 181 | 179, 182 | 15.0, 20.0, 15.0, 20.0 |
| Koniec zakresu | 1440, 1441 | 1439 | 20.0, ValueError, 20.0 |

Pokrycie: 2p – 12 wartości, 3p – 22 wartości łącznie.

### 3. validate_password

Precyzja: 1 znak.

| Granica | 2p | 3p – dodatkowo | Oczekiwane |
|---|---|---|---|
| Minimalna długość 8 | 7, 8 | 6, 9 | False, True, False, True |
| Maksymalna długość 20 | 20, 21 | 19, 22 | True, False, True, False |

Hasła używane w testach zawierają co najmniej jedną literę i jedną cyfrę. Dzięki temu sprawdzamy wyłącznie granice długości.

Pokrycie: 2


## B4. Wyniki testów grade_from_percent

Uruchomiono 38 testów funkcji `grade_from_percent`.

**Wyniki:**
- 34 testy zakończone sukcesem.
- 4 testy zakończone niepowodzeniem.

### Znalezione błędy

**Błąd 1 – Niepoprawna obsługa typów danych**

Funkcja nie zgłasza błędu `TypeError` dla wartości `50.5`, `"50"` oraz `True`, chociaż zgodnie ze specyfikacją powinna przyjmować tylko liczby całkowite.

**Błąd 2 – Niepoprawna ocena dla 90%**

Dla wartości 90 funkcja zwraca ocenę `5.0`, zamiast oczekiwanej `4.5`.

### Wnioski

Testy pozwoliły wykryć błędy w sprawdzaniu typów danych oraz na granicy przedziału ocen. Szczególnie przydatna okazała się analiza wartości brzegowych (AWB). Nie zmieniano kodu funkcji, ponieważ celem ćwiczenia było wykrycie błędów za pomocą testów.

## B5. Wyniki testów parking_fee

Uruchomiono 33 testy funkcji `parking_fee`.

**Wyniki:**
- 32 testy zakończyły się sukcesem.
- 1 test zakończył się niepowodzeniem.

### Znaleziony błąd

**Błąd 3 – Niepoprawna opłata za 1 minutę parkowania**

Dla wartości `1` funkcja zwraca `5.0 zł`, chociaż zgodnie ze specyfikacją powinna zwrócić `0.0 zł`.

Dla pozostałych sprawdzonych wartości funkcja działa poprawnie.

### Wnioski

Testy EP i AWB 2p nie wykryły błędu. Dopiero zastosowanie AWB 3p pozwoliło znaleźć nieprawidłową opłatę za jedną minutę parkowania. Pokazuje to, że warto sprawdzać również wartości znajdujące się blisko granic przedziałów.


## B6. Wyniki testów validate_password

Uruchomiono 19 testów funkcji `validate_password`.

**Wyniki:**
- 17 testów zakończyło się sukcesem.
- 2 testy zakończyły się niepowodzeniem.

### Znalezione błędy

**Błąd 4 – Odrzucanie hasła ze znakiem specjalnym**

Dla hasła `haslo12!` funkcja zwraca `False`, mimo że hasło ma poprawną długość oraz zawiera litery i cyfry.

**Błąd 5 – Odrzucanie hasła ze spacją**

Dla hasła `moje haslo1` funkcja zwraca `False`, mimo że hasło spełnia wymagania dotyczące długości oraz obecności liter i cyfr.

### Wnioski

Testy EP pozwoliły wykryć problemy z obsługą znaków specjalnych i spacji. Testy długości hasła AWB 2p i 3p zakończyły się sukcesem. Kod funkcji nie został zmieniony.

## B7. Wyniki testów ticket_price

Uruchomiono 28 testów funkcji `ticket_price`.

**Wyniki:**
- 26 testów zakończyło się sukcesem.
- 2 testy zakończyły się niepowodzeniem.

### Znaleziony błąd

**Błąd 6 – Niepoprawna obsługa wieku 119 i 120 lat**

Dla wieku 119 i 120 lat funkcja zgłasza `ValueError`, mimo że zgodnie ze specyfikacją są to poprawne wartości.

Oczekiwany wynik dla obu wartości to `10.0 zł`.

### Wnioski

Testy AWB 2p i 3p pozwoliły wykryć błąd przy górnej granicy dozwolonego wieku. Pozostałe 26 testów zakończyło się sukcesem. Kod funkcji nie został zmieniony.


## B8. Uruchomienie wszystkich testów

Uruchomiłem wszystkie testy poleceniem:

`python -m pytest -v`

Wynik:
- Liczba testów: 120
- PASSED: 111
- FAILED: 9

Następnie wykonałem:

`python -m pytest --lf -v`

Uruchomiono ponownie 9 nieudanych testów. Wszystkie ponownie zakończyły się niepowodzeniem.

Wyniki pokazują, że wykryte błędy są powtarzalne. Nie zmieniałem kodu funkcji w katalogu `sut`.

## B9. Analiza nieudanych testów

Wszystkie 9 nieudanych testów zostało uruchomionych ponownie. Wyniki się powtórzyły.

Na podstawie specyfikacji stwierdzono 6 grup defektów. Testy wykryły problemy z typami danych, wartościami brzegowymi oraz obsługą znaków w hasłach.

Najwięcej nieudanych testów dotyczyło funkcji `grade_from_percent` (4). W przypadku `parking_fee` i `ticket_price` szczególnie przydatna była analiza wartości brzegowych.

## B10. Defekty

### DEF-01 – Niepoprawna obsługa typów w grade_from_percent

- Wymaganie: OC-4
- Kroki: wywołać `grade_from_percent(50.5)`, `grade_from_percent("50")` oraz `grade_from_percent(True)`.
- Oczekiwany wynik: `TypeError`.
- Rzeczywisty wynik: funkcja nie zgłasza `TypeError`.
- Test: `test_ep_wrong_type`
- Technika: EP
- Ważność: wysoka

### DEF-02 – Niepoprawna ocena dla 90%

- Wymaganie: OC-2
- Kroki: wywołać `grade_from_percent(90)`.
- Oczekiwany wynik: `4.5`.
- Rzeczywisty wynik: `5.0`.
- Test: `test_bva_2p`
- Technika: AWB 2p
- Ważność: średnia

### DEF-03 – Niepoprawna opłata za 1 minutę parkowania

- Wymaganie: PK-3
- Kroki: wywołać `parking_fee(1)`.
- Oczekiwany wynik: `0.0`.
- Rzeczywisty wynik: `5.0`.
- Test: `test_bva_3p_extra`
- Technika: AWB 3p
- Ważność: wysoka

### DEF-04 – Odrzucanie hasła ze znakiem specjalnym

- Wymaganie: HS-3, HS-4
- Kroki: wywołać `validate_password("haslo12!")`.
- Oczekiwany wynik: `True`.
- Rzeczywisty wynik: `False`.
- Test: `test_ep_valid_classes`
- Technika: EP
- Ważność: średnia

### DEF-05 – Odrzucanie hasła ze spacją

- Wymaganie: HS-3, HS-4
- Kroki: wywołać `validate_password("moje haslo1")`.
- Oczekiwany wynik: `True`.
- Rzeczywisty wynik: `False`.
- Test: `test_ep_valid_classes`
- Technika: EP
- Ważność: średnia

### DEF-06 – Niepoprawna obsługa wieku 119 i 120 lat

- Wymaganie: BL-1, BL-3
- Kroki: wywołać `ticket_price(119)` oraz `ticket_price(120)`.
- Oczekiwany wynik: `10.0` dla obu wartości.
- Rzeczywisty wynik: `ValueError`.
- Testy: `test_bva_2p`, `test_bva_3p_extra`
- Technika: AWB 2p i AWB 3p
- Ważność: średnia

### Wnioski końcowe

Wykonano 120 testów, z czego 111 zakończyło się sukcesem, a 9 niepowodzeniem.

Metoda EP wykryła problemy z typami danych i walidacją haseł. AWB 2p wykryła błędy przy granicach ocen i wieku. AWB 3p dodatkowo wykryła błąd opłaty za jedną minutę parkowania.

Żadna z tych technik osobno nie wykryła wszystkich problemów, dlatego warto stosować je razem.

## Pokrycie kodu testami

Do sprawdzenia pokrycia użyłem polecenia:

`python -m pytest --cov=sut --cov-report=term-missing --cov-report=html`

Wyniki:
- Pokrycie kodu: 100%
- Liczba instrukcji: 67
- Niepokryte instrukcje: 0
- Testy PASSED: 111
- Testy FAILED: 9

Raport pokrycia został zapisany w katalogu `htmlcov`.

### Wnioski

Testy wykonały wszystkie instrukcje w badanych funkcjach, ale mimo to wykryto błędy. Oznacza to, że 100% pokrycia kodu nie gwarantuje poprawnego działania programu.

Techniki EP i AWB pomogły wykryć błędy, których samo pokrycie kodu nie pokazuje.


## Zadanie samodzielne – xfail i pokrycie EP/AWB

### 1. Oznaczenie znanych defektów (xfail)

Testy wykrywające znane defekty oznaczyłem jako `xfail` z parametrem `strict=True`.

Każdy taki test ma przypisany numer defektu od DEF-01 do DEF-06.

Uruchomiłem wszystkie testy poleceniem:

`python -m pytest -v -rx`

**Otrzymany wynik:**
- 120 testów
- 111 PASSED
- 9 XFAIL
- 0 FAILED
- 0 XPASS

Wszystkie znane defekty zostały poprawnie oznaczone. Oznaczenie `xfail` nie naprawia błędów, tylko pozwala odróżnić znane problemy od nowych niepowodzeń testów.

### 2. Pokrycie EP i AWB

Na podstawie przygotowanych tabel oraz testów obliczyłem pokrycie:

- EP: 44/44 = 100%
- AWB 2p: 40/40 = 100%
- AWB 3p: 74/74 = 100%

Wszystkie zaplanowane klasy równoważności i wartości brzegowe mają odpowiednie przypadki testowe.

### Wnioski

Testy wykryły 6 grup defektów. Mimo osiągnięcia 100% pokrycia zaplanowanych przypadków EP i AWB program nadal zawiera błędy.

Dzięki `xfail` można oznaczyć znane problemy, a EP i AWB pomagają sprawdzić poprawność działania funkcji dla różnych danych wejściowych.

## Hasło z polskimi znakami

Dodałem test hasła o długości 20 znaków, zawierającego polskie litery.

Test `test_password_20_polish_chars` zakończył się sukcesem.

Wynik testowania funkcji `validate_password`:
- 20 testów
- 18 PASSED
- 2 XFAIL

Funkcja poprawnie zaakceptowała hasło o długości 20 znaków z polskimi literami.


##  Each Choice

Przygotowałem zestaw 8 przypadków testowych dla funkcji `validate_password`.

Sprawdziłem różne długości haseł, brak litery lub cyfry, polskie znaki, znak specjalny oraz spację.

Uruchomiłem testy poleceniem:

`python -m pytest tests/test_passwords.py -v`

**Wyniki:**
- 28 testów łącznie
- 24 PASSED
- 4 XFAIL
- 0 FAILED

W samym zestawie Each Choice 6 testów zakończyło się sukcesem, a 2 miały status XFAIL z powodu wcześniej wykrytych błędów DEF-04 i DEF-05.

### Wnioski

Each Choice pozwala sprawdzić różne warianty danych wejściowych przy stosunkowo niewielkiej liczbie testów. Znane błędy nie zostały poprawione, lecz odpowiednio oznaczone.

## Podsumowanie końcowe ćwiczenia

Po dodaniu testów samodzielnych uruchomiłem cały zestaw testów wraz z raportem HTML i pomiarem pokrycia kodu.

**Ostateczny wynik:**
- 129 testów
- 118 PASSED
- 11 XFAIL
- 0 FAILED
- 0 XPASS
- Pokrycie kodu: 100%

Wykryłem 6 grup defektów, które oznaczyłem jako `xfail` z odpowiednimi identyfikatorami.

Wygenerowałem dwa raporty:
- `raport.html` – wyniki przed oznaczeniem defektów jako xfail.
- `raport_xfail.html` – wyniki po oznaczeniu defektów jako xfail.

Dodatkowo wygenerowałem raport pokrycia kodu w folderze `htmlcov`.

### Wniosek

Testy EP, AWB i Each Choice pomogły sprawdzić różne przypadki działania funkcji oraz wykryć błędy. Pomimo 100% pokrycia kodu program nadal zawiera znane defekty. Pokazuje to, że samo pokrycie nie gwarantuje poprawności programu.
