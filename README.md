# Python-OpenAI.API

API server for testing OpenAI API - it's still in progress and new features are being added. Will be expanded by:

1. Adding method to send a message to OpenAI and receive a reply from chat model - ✅ done - `OpenAIAPI` class
2. Creating services for each API method to separate api logic and make the code more maintainable. - ✅ done
3. Services will be implemented using production and mock versions to test the code + base services to work as interfaces that can be implemented in production/mock services. - ✅ done
4. API classes will use dependency injection to get services from the container - package `injector` - ✅ done
5. Adding more maintainable error handling - ✅ done

# Installation

App was build using Python 3.12.2.

1. Create system environment variable `API_KEY` with your OpenAI API key - it's required for the app to work properly when checking the API key that is being sent in http request.
2. Run `pip install -r requirements.txt` to install dependencies.
3. Run `python app.py` to start the app - it will run on localhost at port 8040.

# Other information

1. API docs is available at `http://localhost:8040/api/docs`
2. Base api url is `http://localhost:8040/api`
3. UsersAPI class and its methods were only created as a test to show how function `verify_api_key` from `ApiServer` works.
4. `verify_api_key` function checks if the API key passed in the header of http request is valid on the endpoints that are not public - those endpoints require to pass authorization header with API key.
5. If you want to use `/users/{user_id}` protected endpoint from swagger you need to:
   - authenticate using API key fetched from `/keys/` endpoint
   - set `user_id = 1`, otherwise it will raise an exception that user was not found.
6. If you wany to use `/openai/` protected endpoint from swagger you need to authenticate using API key fetched from `/keys/` endpoint
7. To use mock dependencies and data `service_type = ServiceType.MOCK` in `app.py` file - no mock data for openAi services
8. API app is localized to English by default - error messages are being translated. To change the language, change the `lang_code` parameter of `Localizations.lang_initialization(lang_code="...")` function in `app.py` file - to see changes you need to re-run the app. Supported languages codes: 'pl', 'es', 'en'. If you use unsupported language code, app will use default language.
9. Localization was made by creating a custom class `Localizations`. I know I could use `gettext` module, but wanted to do this that way, since it's only test API app to show my coding skills.
