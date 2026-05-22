## Zakres zadania

1. Upewnij się, że w projekcie działa endpoint do weryfikacji tokenu (`/api/token/verify/`).
2. Wygeneruj parę tokenów (`access` + `refresh`) dla zalogowanego użytkownika.
3. Przetestuj **trzy scenariusze**:

   * **Poprawny token** – wywołanie `/api/token/verify/` powinno zwrócić odpowiedź potwierdzającą ważność.

    * Odpowiedź servera: status 200 OK
    {} - zwraca pusty json

   * **Zmanipulowany token** – ręcznie zmień w nim jeden znak (np. w sekcji payload lub signature) i spróbuj ponownie go zweryfikować; oczekiwany jest błąd integralności.

    * Odpowiedź servera: 401 Unauthorized

    {
        "detail": "Token is invalid",
        "code": "token_not_valid"
    } 

   * **Przeterminowany token** – skróć czas życia `ACCESS_TOKEN_LIFETIME` w konfiguracji, wygeneruj nowy token, poczekaj aż wygaśnie i spróbuj go zweryfikować lub użyć na chronionym endpointzie; oczekiwany jest błąd o wygaśnięciu.

    * Odpowiedź servera: 401 Unauthorized

   {
        "detail": "Token is expired",
        "code": "token_not_valid"
    }