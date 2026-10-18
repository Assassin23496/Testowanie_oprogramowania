# Specyfikacja wymagań – KinoTO 1.0 (zakup biletów do kina)

Wersja dokumentu: 1.0 · Status: **do przeglądu** · Podstawa testów na ćwiczeniach 1

## 0. Wprowadzenie

KinoTO to formularz zakupu biletów do kina. Na ćwiczeniach system jest dostępny jako
**symulator w arkuszu Excel** (`Symulator_KinoTO.xlsx`):

- wpisujesz dane w żółte pola,
- komunikaty i podsumowanie pojawiają się automatycznie
  (w symulatorze odpowiada to kliknięciu przycisku „Kup”),
- logika systemu jest ukryta – testujesz **czarnoskrzynkowo**, tylko na podstawie tej specyfikacji.

Każde wymaganie ma identyfikator `REQ-<obszar>-<numer>`, do którego odwołujesz się w warunkach
testowych, przypadkach testowych, macierzy śledzenia i raportach o defektach.

## A. Formularz zakupu (FRM)

| ID | Wymaganie |
|---|---|
| REQ-FRM-01 | Formularz zakupu zawiera pola: Imię, E-mail, Wiek, Liczba biletów, Kod promocyjny, pole wyboru „Mam Kartę Kinomaniaka” oraz przycisk „Kup”. |
| REQ-FRM-02 | Imię musi mieć od 2 do 30 znaków i może zawierać tylko litery, spację oraz myślnik. W przeciwnym razie komunikat: „Podaj poprawne imię.” |
| REQ-FRM-03 | E-mail musi być poprawnym adresem e-mail. W przeciwnym razie komunikat: „Niepoprawny adres e-mail.” |
| REQ-FRM-04 | Wiek kupującego musi być liczbą całkowitą z zakresu 1–120. W przeciwnym razie komunikat: „Podaj wiek od 1 do 120.” |
| REQ-FRM-05 | Liczba biletów musi być liczbą całkowitą z zakresu 1–10 (włącznie). W przeciwnym razie komunikat: „Można kupić od 1 do 10 biletów.” |
| REQ-FRM-06 | Kod promocyjny jest opcjonalny. |
| REQ-FRM-07 | Przy błędnych danych wyświetlana jest lista wszystkich błędów (po jednym komunikacie dla każdego błędnego pola), a zakup nie jest realizowany (brak podsumowania). |
| REQ-FRM-08 | Przy poprawnych danych wyświetlane jest podsumowanie: cena biletu, rabat, opłata rezerwacyjna i kwota do zapłaty (wg części B) oraz komunikat „Dziękujemy za zakup!”. |

## B. Wyliczanie ceny (CEN)

| ID | Wymaganie |
|---|---|
| REQ-CEN-01 | Cena normalnego biletu wynosi 30,00 zł. |
| REQ-CEN-02 | Bilet ulgowy kosztuje 50% ceny normalnej. Ulga przysługuje, gdy kupujący ma mniej niż 18 lat lub co najmniej 65 lat. Wszystkie bilety w zamówieniu są tego samego rodzaju. |
| REQ-CEN-03 | Rabat: 15%, gdy klient ma Kartę Kinomaniaka **i** podał poprawny kod promocyjny; 10%, gdy spełniony jest tylko jeden z tych warunków; 0%, gdy żaden. Rabaty się nie sumują. |
| REQ-CEN-04 | Poprawny kod promocyjny to „KINO10”; wielkość liter nie ma znaczenia. Gdy podano niepoprawny kod, wyświetlana jest informacja „Nieprawidłowy kod – pominięto”, a zakup jest kontynuowany bez rabatu z kodu. |
| REQ-CEN-05 | Opłata rezerwacyjna wynosi 2,00 zł za zamówienie. Opłata nie jest pobierana, gdy klient ma Kartę Kinomaniaka lub gdy wartość biletów przed rabatem wynosi co najmniej 100,00 zł. |
| REQ-CEN-06 | Kwota do zapłaty = liczba biletów × cena biletu (po uldze) × (100 − rabat) / 100, zaokrąglona do grosza, + opłata rezerwacyjna. |
| REQ-CEN-07 | Wszystkie kwoty (cena biletu, opłata, kwota do zapłaty) są wyświetlane z dwoma miejscami po przecinku i jednostką, np. „51,00 zł”. |

**Przykład.** Kupujący w wieku 30 lat, 2 bilety, karta: tak, kod: KINO10.
Cena biletu 30,00 zł (brak ulgi), rabat 15%, opłata 0,00 zł (karta).
Do zapłaty: 2 × 30,00 × 0,85 = 51,00 zł.

## Słownik

- **Karta Kinomaniaka** – karta stałego klienta kina.
- **Zamówienie** – jeden zakup obejmujący od 1 do 10 biletów.
- **Wartość biletów** – liczba biletów × cena biletu.
