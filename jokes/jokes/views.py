import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Joke
from .serializers import JokeSerializer  

class GetJokeView(APIView):
    def get(self, request):
        url = "https://v2.jokeapi.dev/joke/Any?amount=100"
        response = requests.get(url)
        data = response.json()
        
        jokes_data = data.get('jokes', [])
        
        if not jokes_data:
            return Response({"message": "No jokes found or error fetching jokes."}, status=400)
        
        for joke_ in jokes_data:
            category = joke_.get('category')
            joke_type = joke_.get('type')
            nsfw = joke_.get('flags', {}).get('nsfw', False)
            political = joke_.get('flags', {}).get('political', False)
            sexist = joke_.get('flags', {}).get('sexist', False)
            safe = joke_.get('safe', True)
            lang = joke_.get('lang')
            
            # Handle joke types: 'single' or 'twopart'
            if joke_type == 'single':
                joke = joke_.get('joke')
                setup = None
                delivery = None
            elif joke_type == 'twopart':
                joke = None
                setup = joke_.get('setup')
                delivery = joke_.get('delivery')
            else:
                # Skip jokes with unknown types
                continue
            print("Joke Data:", {
                "category": category,
                "joke_type": joke_type,
                "joke": joke,
                "setup": setup,
                "delivery": delivery,
                "nsfw": nsfw,
                "political": political,
                "sexist": sexist,
                "safe": safe,
                "lang": lang
            })
            if not category or not joke_type:
                print(f"Skipping joke due to missing required fields: category={category}, joke_type={joke_type}")
                continue

            # Save the joke to the database
            try:
                Joke.objects.create(
                    category=category,
                    joke_type=joke_type,
                    joke=joke,
                    setup=setup,  
                    delivery=delivery, 
                    nsfw=nsfw,
                    political=political,
                    sexist=sexist,
                    safe=safe,
                    lang=lang
                )
            except Exception as e:
                print(f"Error saving joke: {e}")

        return Response({"message": f"{len(jokes_data)} jokes fetched and saved successfully."})
