from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.db.models import Count, Q
from item.models import Item, Category

# ---------------------------
# HOME / INDEX VIEW
# ---------------------------


def index(request):
    # Latest 6 unsold items
    items = Item.objects.filter(is_sold=False).order_by('-created_at')[:6]

    # Categories with unsold item counts
    categories = Category.objects.annotate(
        unsold_count=Count('items', filter=Q(items__is_sold=False))
    )

    # Popular items (Python-side sorting)
    all_unsold_items = Item.objects.filter(is_sold=False)
    popular_items = sorted(all_unsold_items, key=lambda x: x.popularity_score, reverse=True)[:8]

    # For hero rotator: top 1 popular item per category
    popular_by_category = []
    for category in categories:
        top_item = category.items.filter(is_sold=False).order_by('-created_at')[:1]
        if top_item.exists():
            popular_by_category.append(top_item.first())

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
        'popular_items': popular_items,
        'popular_by_category': popular_by_category,
    })

# ---------------------------
# CONTACT VIEW
# ---------------------------
def contact(request):
    return render(request, 'core/contact.html')


# ---------------------------
# SIGNUP VIEW
# ---------------------------
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {
        'form': form
    })


# ---------------------------
# LOGOUT VIEW
# ---------------------------
@login_required
def logout_view(request):
    logout(request)
    return redirect('core:index')
