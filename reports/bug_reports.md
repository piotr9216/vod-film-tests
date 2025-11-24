# Raporty Błędów - Vod.Film

## Błąd nr 1: Przycisk "Wyczyść" przy filtrze "Sortuj wg" nie resetuje sortowania

**Tytuł:** Przycisk "Wyczyść" na stronie Filmy przy filtrze "Sortuj wg" nie resetuje zastosowanego sortowania

**Środowisko:**

- Przeglądarka: Chrome 119
- System: Windows 10,
- URL: https://vod.film/filmy

**Kroki do reprodukcji:**

1. Wejdź na stronę https://vod.film/filmy
2. Kliknij w listę rozwijaną "Sortuj wg."
3. Wybierz dowolną opcję sortowania (np. "Popularnośc rosnąco")
4. Zaobserwuj zmianę w kolejności wyświetlanych filmów
5. Kliknij przycisk "Wyczyść" znajdujący się obok listy rozwijanej
6. Sprawdź kolejność wyświetlania filmów

**Rezultat oczekiwany (ER):**

Po kliknięciu "Wyczyść":

- Kolejność filmów powinna powrócić do oryginalnej (domyślnej)
- Lista rozwijana "Sortuj wg." powinna pokazywać wartość domyślną

**Rezultat aktualny (AR):**

- Po kliknięciu "Wyczyść" kolejność filmów nie zmienia się
- Sortowanie pozostaje aktywne zgodnie z wcześniej wybraną opcją
- Przycisk "Wyczyść" nie wykonuje żadnej akcji

**Sugerowany priorytet:** Średni

**Załączniki:**

- Zrzut ekranu: [link_do_zrzutu]

---

## Błąd nr 2: Po wyczyszczeniu filtrów w url dale pozostaje filtrowana fraza

**Tytuł:** Po kliknięciu przycisku "Wyczyść filtry" na stronie gatunki zakłądka reality-showw adresie url dalej pozostają wyszukiwane frazy

**Środowisko:**

- Przeglądarka: Chrome 119
- System: Windows 10
- URL: https://vod.film/filmy

**Kroki do reprodukcji:**

1. Wejdź na stronę główną https://vod.film/filmy
2. Kliknij w listę rozwijaną np. "Ocena" i ustaw ocene na 10
3. Jeśli dalej wyświetlane jest lista filmów to kliknij w listę rozwijaną np. "Rok wydania" i ustaw minimalny rok tj. 1920-1920
4. Zweryfikuj czy w url wyświetlone jest wyszukiwane query oraz czy na stronie wyświetlony jest komunikat :" Niestety, nie mogliśmy wyświetlić żadnych tytułów. Prosimy o wyczyszczenie filtrów i ponowną próbę."
5. Kliknij "Wyczyść filtry"
6. Zaobserwuj zmianę adresie url

**Rezultat oczekiwany (ER):**

- w url mamy tylko https://vod.film/filmy
- Filtrowanie zostaje zresetowane

**Rezultat aktualny (AR):**

- W adresie url pozostaj query z filtrownai: https://vod.film/filmy?rating=10&year=1920-1920
- Przy ponownej próbie fitrowania poprzednie filtry dalej obowiązują

**Sugerowany priorytet:** Średni

**Załączniki:**

- Zrzut ekranu: [link_do_zrzutu]
- Film demonstrujący: [link_do_filmu]
