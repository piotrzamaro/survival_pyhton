# survival_pyhton
Analiza przeżycia w środowisku python przy wykorzystaniu języka R

Repozytorium zawiera dwie funkcje:

- rekonstrukcja_IPD

- analiza_RMST

# **rekonstrukcja_ipd**

Fukcja służąca do rekonstrukcji danych IPD na podstawie opublikowanych wykresów krzywych Kaplana-Meiera. Jest to metoda odtworzenia pierwotnych danych pacjentów na podstawie opublikowanych krzywych przeżycia Kaplana-Meiera. Wynikiem zastosowanej procedury jest zestaw danych IPD. Na podstawie ekstrakcji współrzędnych przebiegu krzywych dostępnych w wykresie źródłowym oraz dostępnych danych dotyczących pacjentów w zagrożeniu zastosowany algorytm rekonstruuje indywidualne dane pacjenta. Pakietem źródłowym R wykorzystanym w metodzie jest *IPDfromKM*

Dane wejściowe obejmują:

* **arm0**: współrzędne przebiegu krzywych KM dla grupy interwencyjnej 
* **arm1**: współrzędne przebiegu krzywych KM dla grupy kontrolnej
* **nrisk_arm0:** liczba pacjentów w zagrożeniu dla grupy interwencyjnej 
* **nrisk_arm1:** liczba pacjentów w zagrożeniu dla grupy kontrolnej
* **trisk:** interwał czasu zdarzenia odpowiadający przedziałom osi y
* **maxy:** maksymalny punkt osi y (1 lub 100)

Wynikiem zastosowanej funkcji jest dwukolumnowy zestaw danych zawierających zmienne: **time** (czas zdarzenia) oraz **status** (status zdarzenia)


# **analiza_RMST**

Funkcja służąca do oszacowania wartości RMST na podstawie zrekonstruowanych danych IPD. 
Wartość obszaru pod przebiegiem krzywej Kaplana-Meiera reprezentowana jest wartością RMST, która mierzy ograniczony średni czas przeżycia od początku obserwacji do określonego punktu definiowanego jako czas obcięcia (ang. truncation time, tau). Obszar powyżej krzywej Kaplana-Meiera reprezentuje ograniczony średni czas utracony (RMTL). RMST (restricted mean survival time) można interpretować jako średni czas przeżycia wolny od zdarzeń do określonego punktu czasowego, tau. W odróżnieniu od mediany, przedstawiającej 50% przeżycia w danym punkcie czasowym, RMST przedstawia czas przeżycia do danego punktu czasowego.

Dane wejściowe obejmują zrekonstruowane dane IPD, tj. dwukolumnowy zestaw danych zawierających zmienne: **time** (czas zdarzenia) oraz **status** (status zdarzenia). 

Wynikiem zastosowanej funkcji są oszacowane wartości RMST w dwóch horyzontach:

* horyzont roczny, tj. punkt odcięcia równy 12 miesiącom 
* horyzont badania, tj. punkt odcięcia równy maksymalnemu wspólnemu przebiegowi dwóch ramion badania

