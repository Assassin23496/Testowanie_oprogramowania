# Plan testów – KinoTO 1.0

| Pole | Wartość |
|---|---|
| Identyfikator planu | PT-KinoTO-01 |
| Wersja / data | 1.0 / 2026-10-12 |
| Autor | Raman Vaitsiuk, nr albumu 175529, grupa ISI3 |
| Status | Do przeglądu |

## 1. Kontekst testowania

### 1.1 Przedmiot testów (elementy testowe)
Przedmiotem testów jest KinoTO 1.0 – symulator zakupu biletów do kina w pliku `Symulator_KinoTO.xlsx`. Sprawdzane będą pola formularza, walidacja danych, komunikaty o błędach, podsumowanie zakupu oraz naliczanie cen, ulg, rabatów i opłaty rezerwacyjnej.

### 1.2 Zakres testów
- **W zakresie:** formularz i jego walidacja (`REQ-FRM-01`–`REQ-FRM-08`), ceny biletów, ulgi wiekowe, kombinacje rabatów, obsługa kodu promocyjnego, opłata rezerwacyjna, kwota końcowa oraz format kwot (`REQ-CEN-01`–`REQ-CEN-07`).
- **Poza zakresem:** rzeczywiste płatności, wybór filmu i seansu, wydawanie lub wysyłanie biletów, wydajność i działanie na urządzeniach mobilnych – symulator nie udostępnia tych funkcji. Nie można też przetestować fizycznego przycisku „Kup”, ponieważ podsumowanie w Excelu pojawia się automatycznie.

### 1.3 Podstawa testów
Podstawą do wyprowadzenia przypadków testowych jest `specyfikacja_KinoTO.md` w wersji 1.0, zawierająca wymagania `REQ-FRM-01`–`REQ-FRM-08` oraz `REQ-CEN-01`–`REQ-CEN-07`. Dokument `PRZEWODNIK_cw1.md` określa sposób wykonania i udokumentowania ćwiczenia.

### 1.4 Założenia i ograniczenia
Testowanie odbywa się indywidualnie, w ograniczonym czasie ćwiczenia i tylko w udostępnionym symulatorze Excel. Logika programu jest ukryta, a arkusz chroniony, dlatego testy będą prowadzone metodą czarnej skrzynki. Wyniki zależą także od poprawnego wprowadzenia danych i ustawień formatu komórek.

### 1.5 Interesariusze
Odbiorcą dokumentacji jest prowadzący zajęcia, który ocenia wyniki ćwiczenia. Tester odpowiada za przygotowanie testów i ich udokumentowanie; informacje o defektach mogą zostać wykorzystane przez osobę utrzymującą symulator.

## 2. Komunikacja
Niejasności wymagań będą zapisywane w arkuszu „Przegląd specyfikacji”, a wyniki i wykryte defekty w odpowiednich arkuszach pliku `Vaitsiuk_cw1.xlsx`. Po zakończeniu pracy zostanie przygotowany raport z wykonania testów i przekazany prowadzącemu razem z planem i pozostałą dokumentacją.

## 3. Rejestr ryzyk

Skala: prawdopodobieństwo **P** oraz wpływ **W** przyjmują wartości od 1 (niskie) do 3 (wysokie). Poziom ryzyka to **P × W**. Oceny są szacunkowe, przyjęte do planowania.

| ID | Ryzyko (produktowe / projektowe) | Prawdopodobieństwo (1–3) | Wpływ (1–3) | Poziom (P×W) | Działanie ograniczające |
|---|---|---:|---:|---:|---|
| R1 | **Produktowe:** błędne naliczanie rabatów i kwoty do zapłaty. | 2 | 3 | 6 | Sprawdzić cztery kombinacje karty i promokodu oraz samodzielnie przeliczyć oczekiwane kwoty. |
| R2 | **Produktowe:** akceptowanie niedozwolonych danych lub niewyświetlenie właściwych komunikatów. | 2 | 3 | 6 | Zastosować wartości graniczne, dane niepoprawne i testy kilku błędów jednocześnie. |
| R3 | **Projektowe:** automatyczna zmiana formatu danych przez Excel, np. zamiana wieku na datę. | 3 | 2 | 6 | Przed wykonaniem testu sprawdzać wartość i format komórki; poprawiać format i ponawiać próbę, jeśli dane zostały zmienione. |
| R4 | **Projektowe:** zbyt mało czasu na wykonanie wszystkich testów. | 2 | 2 | 4 | Wykonać najpierw testy o wysokim priorytecie; pominięte testy i przyczyny odnotować w raporcie. |

## 4. Strategia testów

### 4.1 Poziomy i typy testów
Zostaną przeprowadzone ręczne testy systemowe i funkcjonalne całego symulatora. Testowanie będzie czarnoskrzynkowe, czyli oparte na wymaganiach i widocznych wynikach, bez analizy kodu ani ukrytych formuł.

### 4.2 Techniki projektowania testów
Zastosowane zostaną: podział na klasy równoważności (EP), analiza wartości brzegowych (AWB), tablica decyzyjna dla kombinacji karty Kinomaniaka i kodu KINO10, testowanie eksploracyjne oraz lista kontrolna.

### 4.3 Kryteria wejścia
Można rozpocząć wykonywanie testów, gdy dostępne są dokument `specyfikacja_KinoTO.md` w wersji 1.0, działający `Symulator_KinoTO.xlsx` i arkusz dokumentacji oraz gdy przygotowano przypadki testowe z danymi wejściowymi i oczekiwanymi wynikami.

### 4.4 Kryteria wyjścia (ukończenia)
Testowanie można uznać za ukończone zgodnie z planem po wykonaniu 100% przypadków o priorytecie wysokim, powiązaniu każdego z 15 wymagań z co najmniej jednym przypadkiem testowym i zapisaniu wyników oraz wykrytych defektów. Brak otwartych defektów krytycznych jest warunkiem pozytywnej rekomendacji; niespełnienie kryteriów trzeba wyraźnie opisać w raporcie końcowym.

### 4.5 Kryteria zawieszenia i wznowienia
Testy zostają zawieszone, gdy plik nie działa, wyniki się nie aktualizują albo błędy środowiska uniemożliwiają wiarygodną ocenę. Zostają wznowione po przywróceniu działania symulatora oraz sprawdzeniu, że wprowadzane dane i obliczenia są aktualizowane prawidłowo.

### 4.6 Dane testowe i środowisko
Środowisko: Excel Online (Microsoft 365) w przeglądarce, plik `Symulator_KinoTO.xlsx`, pola wejściowe C4–C9. Użyte zostaną dane poprawne i niepoprawne, m.in. granice wieku 1–120, liczby biletów 1–10, długości imienia 2–30 oraz różne kombinacje karty i promokodu. Przed każdym testem pola wejściowe należy wyczyścić i sprawdzić format danych.

### 4.7 Retesty i testy regresji
Po naprawie defektu należy ponownie wykonać przypadek, który go wykrył (retest), oraz powiązane przypadki sprawdzające funkcje mogące ucierpieć wskutek poprawki (regresja). Jeżeli poprawiona wersja symulatora nie będzie dostępna, należy zaznaczyć, że retestów i regresji nie przeprowadzono.

### 4.8 Metryki
Mierzone będą: liczba zaprojektowanych i wykonanych testów, liczba testów zaliczonych, niezaliczonych, zablokowanych i pominiętych, liczba defektów według ważności oraz procent pokrycia wymagań przypadkami testowymi.

### 4.9 Produkty testowania (testalia)
Produkty pracy to: plan testów, przegląd specyfikacji, warunki testowe, przypadki testowe, macierz śledzenia, wyniki wykonania, notatki z sesji eksploracyjnej, raporty defektów, lista kontrolna i raport z wykonania testów.

## 5. Działania testowe i harmonogram

| Działanie | Kto | Termin / czas | Produkt |
|---|---|---|---|
| Analiza specyfikacji i wyznaczanie warunków testowych | Raman Vaitsiuk | Etap 1 – ok. 20 min | Przegląd specyfikacji, warunki testowe |
| Projektowanie przypadków i macierzy śledzenia | Raman Vaitsiuk | Etap 2 – ok. 30 min | Przypadki testowe, macierz śledzenia |
| Wykonanie testów i sesja eksploracyjna | Raman Vaitsiuk | Etap 3 – ok. 45 min (w tym 20 min sesji eksploracyjnej) | Wyniki wykonania, notatki, raporty defektów |
| Lista kontrolna, raportowanie i przegląd dokumentacji | Raman Vaitsiuk | Etap 4 – ok. 25 min | Lista kontrolna, raport z wykonania, komplet dokumentacji |

Podane czasy są orientacyjnym harmonogramem pracy, a nie zapisem rzeczywistego czasu wykonania.

## 6. Role i odpowiedzialności
Raman Vaitsiuk odpowiada za planowanie, analizę wymagań, projektowanie i wykonanie przypadków testowych, zgłaszanie defektów i przygotowanie raportu końcowego. Prowadzący zajęcia odpowiada za ocenę dokumentacji i ewentualne zatwierdzenie planu.

## 7. Zatwierdzenie

| Rola | Imię i nazwisko | Data | Podpis |
|---|---|---|---|
| Autor | Raman Vaitsiuk | 2026-10-12 | Dokument elektroniczny – bez podpisu |
| Zatwierdzający | Prowadzący zajęcia | Jeszcze nie zatwierdzono | Oczekuje na zatwierdzenie |
