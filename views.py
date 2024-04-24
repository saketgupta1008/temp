from django.http import JsonResponse

def search_suggestions(request):
    query = request.GET.get('query', '')
    if query:
        # Assuming you have a function `search_your_data` to find matches
        results = search_your_data(query)
        suggestions = [result.title for result in results]  # Customize based on your data structure
    else:
        suggestions = []
    return JsonResponse(suggestions, safe=False)
