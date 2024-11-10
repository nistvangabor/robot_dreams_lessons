import requests

class RickAndMortyAPI:
    def __init__(self):
        self.base_url = "https://rickandmortyapi.com/api"

    def get_data(self, endpoint: str, params: dict = None):
        data = []
        url = f"{self.base_url}/{endpoint}"
        
        while url:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                result = response.json()
                data.extend(result['results'])
                url = result['info'].get('next')  # Update the URL to the next page if available
            else:
                print(f"Error {response.status_code}: {response.json().get('error', 'Unknown error')}")
                break
        return data

    def get_characters(self, name=None, status=None, species=None, type=None, gender=None):
        params = {
            "name": name,
            "status": status,
            "species": species,
            "type": type,
            "gender": gender,

        }
        return self.get_data("character", params)

    def get_episodes(self, name=None, episode=None):
        params = {
            "name": name,
            "episode": episode
        }
        return self.get_data("episode", params)

    def get_locations(self, name=None, type=None, dimension=None):
        params = {
            "name": name,
            "type": type,
            "dimension": dimension
        }
        return self.get_data("location", params)


# Example usage
api = RickAndMortyAPI()

# Fetch all characters
characters = api.get_characters()
print(f"Total characters found: {len(characters)}")

# Fetch all episodes
episodes = api.get_episodes()
print(f"Total episodes found: {len(episodes)}")

# Fetch all locations
locations = api.get_locations()
print(f"Total locations found: {len(locations)}")


#https://api.github.com
#list of public apis