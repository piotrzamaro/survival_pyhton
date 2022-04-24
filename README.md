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


