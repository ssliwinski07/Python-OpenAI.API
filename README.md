# Python-OpenAI.API

API server for testing OpenAI API - it's still in progress and new features are being added. For now it has one method to fetch OpenAI API key. Will be expanded by:

1. Adding method to send a message to OpenAI and receive a reply from chat model - 🛠️ in progress
2. Creating services for each API method to separate api logic and make the code more maintainable. - ✅ done for `ApiKeyService` class
3. Services will be implemented using production and mock versions to test the code + base services to work as interfaces that can be implemented in production/mock services. - ✅ done
4. API classes will use dependency injection to get services from the container - package `injector` - ✅ done for `ApiKeyApi` class
5. Adding more maintainable error handling - 🛠️ in progress (partially done for `ApiKeyApi` and `ApiKeyService`)

# Installation

App was build using Python 3.12.2.

1. Create system environment variable `API_KEY` with your OpenAI API key - it's required for the app to work properly when checking the API key that is being sent in http request.
2. Run `pip install -r requirements.txt` to install dependencies.
3. Run `python app.py` to start the app - it will run on localhost at port 8040.

# Other information

1. API docs is available at `http://localhost:8040/api`
2. UsersAPI class and its methods were only created as a test to show how function `verify_api_key` from `ApiServer` works.
3. `verify_api_key` function checks if the API key passed in the header of http request is valid on the endpoints that are not public - those endpoints require to pass authorization header with API key.
4. If you want to use `/users/{user_id}` protected endpoint from swagger you need to:
   - authorize using API key fetched from `/keys/` endpoint
   - set `user_id = 1`, otherwise it will raise an exception that user was not found.
