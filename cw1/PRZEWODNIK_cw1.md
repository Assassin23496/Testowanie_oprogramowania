# Ćwiczenia 1 – przewodnik do samodzielnej pracy

Ten przewodnik zawiera całą teorię potrzebną do wykonania ćwiczeń 1.
Rozdziały odpowiadają krokom instrukcji. Przeczytaj rozdział przed wykonaniem danego kroku –
każdy zajmuje 2–4 minuty.

Na ćwiczeniach nie programujesz i nie korzystasz z przeglądarki. Pracujesz na:

- `specyfikacja_KinoTO.md` – wymaganiach systemu (podstawa testów),
- `Symulator_KinoTO.xlsx` – systemie, który testujesz (formularz w Excelu z ukrytą logiką),
- `Szablon_dokumentacji_testowej.xlsx` – arkuszach, w których zapisujesz dokumentację,
- `plan_testow_szablon.md` i `raport_defektu_szablon.md` – szablonach tekstowych (Notatnik).

Terminologia jest zgodna z sylabusem ISTQB® Certyfikowany Tester – Poziom Podstawowy (wersja 4.0)
i normą ISO/IEC/IEEE 29119-3 (dokumentacja testowa).

---

## Krok 0. Pojęcia podstawowe

### 0.1 Czym jest testowanie

**Testowanie** to zestaw czynności, których celem jest wykrywanie defektów i ocena jakości
oprogramowania. Testujemy, aby:

- znaleźć defekty, zanim trafią do użytkownika,
- zdobyć zaufanie do jakości produktu (np. „najważniejsze funkcje działają”),
- dostarczyć informacji potrzebnych do decyzji (np. „czy można wydać wersję?”),
- sprawdzić zgodność z wymaganiami, umowami i przepisami.

Testowanie **nie jest** debugowaniem. Tester pokazuje, że coś działa źle (awarię), a programista
w ramach debugowania szuka przyczyny i ją usuwa. Po naprawie tester wykonuje **retest**
(test potwierdzający), a często także **testy regresji** – sprawdza, czy poprawka nie zepsuła
czegoś innego.

Wyróżniamy:

- **testowanie statyczne** – bez uruchamiania programu: przeglądy wymagań, kodu, dokumentacji,
- **testowanie dynamiczne** – z uruchomieniem programu (dziś: symulatora).

### 0.2 Pomyłka, defekt, awaria

| Pojęcie | Znaczenie | Przykład |
|---|---|---|
| Pomyłka (*error*) | działanie człowieka dające zły wynik | programista zapisał „> 18” zamiast „≥ 18” |
| Defekt (*defect, bug*) | wada w programie lub dokumencie | zły warunek ulgi w programie |
| Awaria (*failure*) | widoczne, nieprawidłowe działanie | 18-latek dostaje bilet ulgowy |

Pomyłka powoduje defekt; defekt wykonany w programie może spowodować awarię.
Defekt może też tkwić w **dokumencie** (np. sprzeczne wymagania) – wtedy wykrywamy go przeglądem.

### 0.3 Siedem zasad testowania (w skrócie)

1. Testowanie wykazuje obecność defektów, a nie ich brak.
2. Testowanie gruntowne (wszystkich kombinacji) jest niemożliwe – trzeba wybierać.
3. Wczesne testowanie oszczędza czas i pieniądze.
4. Defekty mają tendencję do kumulowania się w kilku miejscach.
5. Testy się „zużywają” – powtarzane bez zmian przestają znajdować nowe defekty.
6. Testowanie zależy od kontekstu (inaczej testujemy kino, a inaczej system medyczny).
7. Brak znalezionych defektów nie oznacza, że system jest przydatny dla użytkowników.

### 0.4 Proces testowy

| Czynność | Pytanie | Produkt (dziś) |
|---|---|---|
| Planowanie | po co, co i jak testujemy? | plan testów |
| Monitorowanie i nadzór | czy idziemy zgodnie z planem? | (raport z postępu) |
| Analiza | **co** testować? | lista niejasności, warunki testowe |
| Projektowanie | **jak** testować? | przypadki testowe, macierz śledzenia |
| Implementacja | co przygotować do wykonania? | dane testowe, kolejność wykonania |
| Wykonanie | jaki jest wynik? | wyniki, raporty o defektach |
| Ukończenie | co z tego wynika? | raport z wykonania |

Czynności nie muszą iść ściśle po kolei – w praktyce nakładają się i powtarzają.

### 0.5 Słowniczek

- **Podstawa testów** – wszystko, z czego wyprowadzamy testy (specyfikacja, historyjki, umowa).
- **Przedmiot testów** – to, co testujemy (np. KinoTO 1.0).
- **Warunek testowy** – testowalny aspekt systemu, np. „liczba biletów 1–10”.
- **Przypadek testowy** – warunki wstępne, dane, kroki i oczekiwany wynik.
- **Procedura testowa** – kolejność wykonania kilku przypadków.
- **Wyrocznia testowa** – źródło wiedzy o oczekiwanym wyniku.
- **Pokrycie** – stopień, w jakim testy sprawdziły dane elementy (np. wymagania), w procentach.
- **Testalia** – wszystkie produkty testowania.
- **Testowanie czarnoskrzynkowe** – testy projektowane na podstawie specyfikacji, bez znajomości kodu
  (dlatego logika symulatora jest ukryta).
- **Testowanie białoskrzynkowe** – testy projektowane na podstawie budowy kodu.

---

## Krok 1. Przegląd specyfikacji (testowanie statyczne)

**Przegląd** to czytanie produktu pracy (np. specyfikacji) w poszukiwaniu defektów, bez uruchamiania
programu. Defekt w wymaganiu, wykryty zanim powstanie program, kosztuje tylko poprawkę tekstu.
Ten sam defekt wykryty u klienta oznacza poprawkę programu, ponowne testy, nowe wydanie i straty
wizerunkowe – to zasada **wczesnego testowania**.

Cechy dobrego wymagania:

| Cecha | Pytanie kontrolne | Przykład problemu |
|---|---|---|
| Jednoznaczne | Czy każdy rozumie je tak samo? | „poprawny adres e-mail” – wg jakich reguł? |
| Kompletne | Czy opisano dane błędne i komunikaty? | brak komunikatu dla pustego pola |
| Spójne | Czy nie przeczy innemu wymaganiu? | jedno pole „włącznie”, drugie bez tego słowa |
| Testowalne | Czy da się ocenić wynik: tak/nie? | „system działa szybko” |
| Atomowe | Czy opisuje jedną rzecz? | jedno wymaganie opisuje 5 pól naraz |

Jak zapisywać znaleziska (arkusz **Przegląd specyfikacji**): każdy problem w osobnym wierszu,
z ID wymagania, rodzajem problemu, opisem i pytaniem do autora (lub propozycją poprawki).
Pisz rzeczowo – oceniasz dokument, nie autora.

**Przykład.** REQ-FRM-05: „Liczba biletów musi być liczbą całkowitą z zakresu 1–10 (włącznie)”.
Granice są jasne, ale nie wiadomo, czy `2,0`, `+2`, `02` lub puste pole to błąd.
Zapis: `REQ-FRM-05 | Niejednoznaczność | „liczba całkowita” niezdefiniowana | Czy 2,0 i puste pole mają dawać komunikat?`

---

## Krok 2. Warunki testowe

**Warunek testowy** mówi, *co* sprawdzamy – jest ogólny i nie zawiera konkretnych danych.
**Przypadek testowy** mówi, *jak* to sprawdzamy – zawiera dane, kroki i oczekiwany wynik.

```
REQ-FRM-02 (imię 2–30 znaków: litery, spacja, myślnik)
 ├─ WT-FRM-01 minimalna długość imienia     → TC: imię "A" (błąd), imię "Al" (OK)
 ├─ WT-FRM-02 maksymalna długość imienia    → TC: 30 znaków (OK), 31 znaków (błąd)
 ├─ WT-FRM-03 dozwolone znaki               → TC: "Anna-Maria Łoś" (OK)
 └─ WT-FRM-04 niedozwolone znaki            → TC: "Anna1", "Anna_M" (błąd)
```

**Priorytet** warunku wynika z ryzyka: jak prawdopodobny jest defekt i jak poważne byłyby jego
skutki. Funkcje związane z pieniędzmi (cena, rabat, kwota do zapłaty) mają zwykle priorytet
wysoki. Warunki o wysokim priorytecie projektujemy i wykonujemy najpierw.

---

## Krok 3. Plan testów

Plan testów opisuje cele, zakres, podejście, zasoby i harmonogram testów. Typowe części
(wg ISO/IEC/IEEE 29119-3) są w pliku `plan_testow_szablon.md`. Najważniejsze pojęcia:

- **Zakres** – co testujemy, a co jest **poza zakresem** (z uzasadnieniem).
- **Ryzyko** – zdarzenie, które może mieć negatywne skutki:
  - **produktowe** – dotyczy jakości produktu (np. zła kwota do zapłaty),
  - **projektowe** – dotyczy przebiegu testów (np. brak czasu, niedostępny symulator).
  - **Poziom ryzyka = prawdopodobieństwo × wpływ** (np. w skali 1–3, wynik 1–9).
- **Kryteria wejścia** – warunki rozpoczęcia wykonywania testów (np. symulator działa).
- **Kryteria wyjścia** – warunki zakończenia testów (np. pokrycie wymagań 100%, wszystkie
  przypadki o priorytecie Wysoki wykonane). Powinny być mierzalne.
- **Kryteria zawieszenia i wznowienia** – kiedy przerywamy testy i kiedy wracamy.

Poziomy testów: **modułowe** (pojedyncza funkcja), **integracyjne** (współpraca części),
**systemowe** (cały system), **akceptacyjne** (czy system spełnia potrzeby użytkownika).
Typy testów: **funkcjonalne** (co system robi) i **niefunkcjonalne** (jak dobrze: wydajność,
użyteczność, bezpieczeństwo, dostępność). Dziś: testy systemowe, funkcjonalne, czarnoskrzynkowe,
manualne.

**Jak wypełnić plik .md.** To zwykły tekst. Zastąp fragmenty w nawiasach `<…>` własną treścią.
Wiersz tabeli to linia z kreskami `|` – nowy wiersz dodasz, kopiując istniejący. Linie zaczynające
się od `>` to komentarze szablonu – usuń je. Zapisz plik w kodowaniu UTF-8. 

---

## Krok 4. Przypadki testowe

### 4.1 Budowa przypadku

| Pole | Opis | Przykład |
|---|---|---|
| ID | unikalny identyfikator | TC-FRM-007 |
| Tytuł | co sprawdza | 11 biletów – odrzucone |
| Wymaganie | ID z podstawy testów | REQ-FRM-05 |
| Warunki wstępne | stan przed testem | symulator otwarty, żółte pola puste |
| Dane testowe | konkretne wartości wszystkich pól | Anna, anna@example.com, 30, **11**, bez kodu, karta: Nie |
| Kroki | ponumerowane czynności | 1. Wpisz dane. 2. Odczytaj „Komunikaty”. |
| Oczekiwany rezultat | z wymagania, z dokładnym komunikatem | „Można kupić od 1 do 10 biletów.”, brak podsumowania |

Dobry przypadek jest **powtarzalny** (każdy wykona go tak samo), **jednoznaczny** (wynik da się
ocenić bez dyskusji) i **niezależny** (nie wymaga wcześniejszego wykonania innego przypadku).

### 4.2 Klasy równoważności (EP – *equivalence partitioning*)

Dzielimy możliwe wartości na **klasy**, w których system powinien zachowywać się tak samo.
Z każdej klasy wybieramy jedną wartość – jeśli działa dla niej, zakładamy, że działa dla całej klasy.

Przykład – wiek (REQ-FRM-04 i REQ-CEN-02):

| Klasa | Typ | Wartość reprezentatywna | Oczekiwanie |
|---|---|---|---|
| 1–17 | poprawna (ulga) | 10 | cena biletu 15,00 zł |
| 18–64 | poprawna (bez ulgi) | 30 | cena biletu 30,00 zł |
| 65–120 | poprawna (ulga) | 70 | cena biletu 15,00 zł |
| < 1 | niepoprawna | 0 | „Podaj wiek od 1 do 120.” |
| > 120 | niepoprawna | 150 | „Podaj wiek od 1 do 120.” |
| nie jest liczbą całkowitą | niepoprawna | `abc`, `25,5` | „Podaj wiek od 1 do 120.” |

Zasada: w jednym przypadku testowym tylko **jedna** wartość niepoprawna, pozostałe pola poprawne –
inaczej nie wiadomo, która wartość wywołała komunikat (zjawisko *maskowania*).

### 4.3 Analiza wartości brzegowych (AWB)

Programiści najczęściej mylą się na granicach (`>` zamiast `≥`, przesunięcie o 1). AWB dotyczy
klas uporządkowanych (liczby, długości, kwoty).

- **Wariant 2-punktowy**: dla każdej granicy – sama granica i najbliższa wartość z sąsiedniej klasy.
  Wiek: **0, 1, 17, 18, 64, 65, 120, 121**.
- **Wariant 3-punktowy**: granica i **obaj** jej sąsiedzi, np. dla granicy 65: **64, 65, 66**.
- Długość tekstu: imię 2–30 znaków → 1, 2, 30, 31 znaków (2-punktowy).
- Liczba biletów 1–10 → 0, 1, 10, 11.

### 4.4 Kombinacje warunków (tablica decyzyjna – wersja uproszczona)

Gdy wynik zależy od kilku warunków jednocześnie, wypisujemy wszystkie kombinacje (dla 2 warunków
logicznych – 4, dla 3 – 8). Przykład REQ-CEN-03:

| Karta | Kod KINO10 | Rabat |
|---|---|---|
| tak | tak | 15% |
| tak | nie | 10% |
| nie | tak | 10% |
| nie | nie | 0% |

Każdy wiersz to co najmniej jeden przypadek testowy. Oczekiwaną kwotę liczymy samodzielnie ze
wzoru (REQ-CEN-06), np. wiek 30, 2 bilety, karta i kod: 2 × 30,00 × 0,85 = 51,00 zł; opłata 0 zł
(karta) → do zapłaty 51,00 zł.

### 4.5 Typowe błędy w przypadkach testowych

- brak konkretnych danych („wpisz błędne imię”),
- oczekiwany rezultat „błąd” zamiast dokładnego komunikatu lub kwoty,
- kilka wartości niepoprawnych w jednym przypadku,
- brak odwołania do wymagania,
- zależność od innego przypadku („kontynuuj po TC-3”).

---

## Krok 5. Macierz śledzenia

**Śledzenie** (*traceability*) to powiązania między wymaganiami a przypadkami testowymi (a dalej –
wynikami i defektami). Macierz śledzenia pozwala:

- znaleźć **luki** – wymagania bez żadnego testu,
- policzyć **pokrycie wymagań** = liczba wymagań pokrytych ÷ liczba wszystkich wymagań × 100%,
- przy zmianie wymagania od razu wskazać testy do poprawy (**analiza wpływu**),
- przy niezaliczonym teście wskazać, którego wymagania dotyczy problem.

W szablonie identyfikatory wymagań są już wpisane, a kolumny „Liczba przypadków”, „Zaliczone”,
„Niezaliczone” i „Pokrycie” wypełniają się same na podstawie arkusza „Przypadki testowe”.

---

## Krok 6. Wykonanie przypadków testowych

- Wykonuj kroki dokładnie tak, jak je zapisano – na tym polega powtarzalność.
- Porównaj rzeczywisty rezultat z oczekiwanym:
  - zgodny → **Zaliczony**,
  - różny → **Niezaliczony** (powtórz test; jeśli różnica się powtarza – raport o defekcie),
  - nie da się wykonać → **Zablokowany** (podaj powód),
  - świadomie pominięty → **Pominięty** (podaj powód).
- Zapisz, kto i kiedy wykonał test.

**Symulator KinoTO** to arkusz Excela, który zachowuje się jak formularz: wpisujesz dane w żółte pola,
a komunikaty i podsumowanie pojawiają się same (odpowiednik kliknięcia „Kup”). Arkusz jest chroniony –
logika jest ukryta, tak jak w prawdziwym systemie testowanym metodą czarnej skrzynki. Przed każdym
przypadkiem wyczyść żółte pola.

---

## Krok 7. Testowanie eksploracyjne i raporty o defektach

### 7.1 Testowanie eksploracyjne

Tester **jednocześnie** poznaje system, projektuje i wykonuje testy, a kolejne kroki wybiera
na podstawie tego, co właśnie zaobserwował. Aby było to uporządkowane, stosuje się **sesje**
o stałym czasie i **kartę testu** (*charter*):

```
Zbadaj:   <obszar>
Używając: <zasoby, techniki, rodzaje danych>
Aby:      <cel – jakie informacje chcemy zdobyć>
```

W trakcie sesji prowadzimy notatki: co sprawdzono, co zauważono, jakie pytania się pojawiły.
Technika znajduje defekty, których nie przewidziały zaprojektowane przypadki. Jej skuteczność zależy
od doświadczenia testera. Pomysły na nietypowe dane: puste pola, same spacje, liczby ujemne
i ułamkowe, bardzo długie teksty, polskie znaki, różna wielkość liter, wartości graniczne.

### 7.2 Skąd wiadomo, że to defekt? (wyrocznie)

Oczekiwany wynik wynika ze **specyfikacji** (najważniejsza wyrocznia), z **wzorów i przykładów**
w specyfikacji, z **konwencji** (kwota z jednostką „zł”), ze **spójności** (te same nazwy pól wszędzie)
i ze zdrowego rozsądku (brak literówek). Jeśli żadne źródło nie rozstrzyga – zapisz **pytanie**,
a nie raport o defekcie.

### 7.3 Raport o defekcie

Cel raportu: inna osoba (programista), korzystając **wyłącznie** z raportu, odtwarza awarię
i rozumie, dlaczego to problem. Pola raportu opisuje `raport_defektu_szablon.md`;
raporty zapisujesz w arkuszu **Raporty defektów**.

Przykład (fikcyjny):

| Słaby raport | Dobry raport |
|---|---|
| Tytuł: „Cena nie działa” | Tytuł: „Podsumowanie: wiek 10 – cena biletu 30,00 zł zamiast 15,00 zł” |
| brak danych | Dane: imię Ola, e-mail ola@example.com, wiek 10, 1 bilet, bez kodu, karta: Nie |
| „Powinno być taniej” | Oczekiwane: 15,00 zł – ulga dla wieku < 18 (REQ-CEN-02) |
| „Czasem” | Powtarzalność: zawsze (3 na 3 próby) |

Zasady: jeden raport = jeden problem; rzeczowo, bez ocen ludzi; sprawdź, czy nie jest duplikatem.

### 7.4 Ważność a priorytet

- **Ważność** (*severity*) – jak poważny jest wpływ defektu na system i użytkownika
  (krytyczna, wysoka, średnia, niska). Ocenia ją zwykle tester.
- **Priorytet** (*priority*) – jak pilnie trzeba defekt naprawić (wysoki, średni, niski).
  Decyduje zwykle właściciel produktu / kierownik.

Mogą się różnić: literówka w nazwie kina na ekranie głównym – ważność niska, priorytet wysoki;
błąd w rzadko używanym raporcie rocznym – ważność wysoka, priorytet średni.

### 7.5 Cykl życia defektu

```
Nowy → Otwarty → W naprawie → Naprawiony → Do retestu → Zamknięty
  ├→ Odrzucony (to nie defekt / nie do odtworzenia / duplikat)
  ├→ Odroczony (naprawa w późniejszej wersji)
  └ … Do retestu → Ponownie otwarty (retest nieudany)
```

---

## Krok 8. Testowanie w oparciu o listę kontrolną

To technika **oparta na doświadczeniu**: zamiast pełnych przypadków testowych tester sprawdza
listę pozycji (pytań). Pozycje pochodzą z doświadczenia, typowych błędów, standardów i wymagań.

- Pozycję formułuj jako pytanie, na które odpowiedź **„Tak” oznacza stan poprawny**
  (np. „Czy wszystkie kwoty mają format „0,00 zł”?”).
- Listy bywają **ogólne** (dla każdego formularza) i **specyficzne** (dla konkretnego ekranu).
- Zalety: szybkość, elastyczność, łatwe utrzymanie. Wady: różni testerzy mogą sprawdzać tę samą
  pozycję w różny sposób; wynik zależy od doświadczenia.
- Listę trzeba aktualizować – pozycje, które nigdy nie znajdują problemów, „zużywają się”,
  a nowe typowe błędy trzeba dopisywać.

Obszary do inspiracji dla ekranu formularza: zgodność ze specyfikacją (nazwy pól, treść komunikatów),
komunikaty (czy każdy błąd ma komunikat, czy wskazuje pole), prezentacja wyników (format kwot,
ukrycie wyniku przy błędach), użyteczność (czy wiadomo, co wypełnić, czy etykiety są jasne).

---

## Krok 9. Raport z wykonania testów

Raport podsumowuje testy dla osób, które podejmują decyzje. Zawiera:

- zakres wykonanych prac i **odstępstwa od planu** (co nie zostało zrobione i dlaczego),
- metryki: przypadki zaprojektowane / wykonane / zaliczone, defekty według ważności,
  pokrycie wymagań,
- ocenę **kryteriów wyjścia** z planu testów,
- najważniejsze problemy i ryzyka,
- **rekomendację** (np. „nie wydawać do czasu naprawy DEF-002”),
- wnioski na przyszłość (*lessons learned*).

W szablonie liczby wyliczają się automatycznie z pozostałych arkuszy – uzupełniasz pola opisowe.

---

## Źródła do dalszej lektury

- A. Roman, L. Stapp, M. Pilaeten, *Certyfikowany tester ISTQB®. Poziom podstawowy*, wyd. II, Helion 2024.
- Sylabus ISTQB® Certified Tester Foundation Level v4.0 – https://www.istqb.org
- ISO/IEC/IEEE 29119-3 – Software and systems engineering – Software testing – Part 3: Test documentation.
