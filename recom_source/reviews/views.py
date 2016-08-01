from django.shortcuts import render, get_object_or_404
from .models import Review, Wine


def review_list(request):
    """
    Gets a list of the latest 9 reviews and renders it using `reviews/list.html'.
    """
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list': latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    """
    Gets a review given its ID and renders it using review_detail.html.
    """
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def wine_list(request):
    """
    Gets all the wines sorted by name and passes it to wine_list.html to be rendered
    """
    wine_list = Wine.objects.order_by('-name')
    context = {'wine_list': wine_list}
    return render(request, 'reviews/wine_list.html', context)


def wine_detail(request, wine_id):
    """
    Gets a wine from the DB given its ID and renders it using wine_detail.html
    """
    wine = get_object_or_404(Wine, pk=wine_id)
    return render(request, 'reviews/wine_detail.html', {'wine': wine})
