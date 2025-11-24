import pytest
import json

@pytest.mark.api
class TestFilmSearchAPI:

    SEARCH_ENDPOINT = "/search-route"

    def test_api_search_the_pickup(self, api_request_context, search_payload):

        # Given
        search_query = "the pickup"
        payload = search_payload(search_query)

        # When
        response = api_request_context.post(
            self.SEARCH_ENDPOINT,
            data=json.dumps(payload)
        )

        # Then - weryfikacja status code
        assert response.status == 200, (
            f"Oczekiwano status 200 OK, ale otrzymano {response.status}. "
            f"Response: {response.text()}"
        )

        # Weryfikacja odpowiedzi JSON
        response_data = response.json()
        assert "data" in response_data, "Brak pola 'data' w odpowiedzi JSON"
        
        # Weryfikacja czy w danych znajduje się szukany film
        movies_data = response_data["data"]
    
        matching_movies = [
            movie for movie in movies_data 
            if search_query.lower() in movie.get("title", "").lower()
        ]
        
        assert len(matching_movies) > 0, (
            f"Brak filmów zawierających frazę '{search_query}' w odpowiedzi"
        )