from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404, redirect
from django.db.models import Q
from .forms import NewItemForm, EditItemForm
from .models import Item, Category

# Create your views here.
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Item, Category

def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category')
    sort = request.GET.get('sort')
    page = request.GET.get('page', 1)  # get current page

    items = Item.objects.all()

    # Search
    if query:
        items = items.filter(name__icontains=query)

    # Category filter
    if category_id and category_id.isdigit():
        items = items.filter(category_id=int(category_id))

    # Sorting logic
    if sort == 'price_low':
        items = items.order_by('price')
    elif sort == 'price_high':
        items = items.order_by('-price')
    elif sort == 'name':
        items = items.order_by('name')
    else:
        items = items.order_by('-created_at')

    # Pagination
    paginator = Paginator(items, 6)  # show 6 items per page
    page_obj = paginator.get_page(page)

    categories = Category.objects.all()

    return render(request, 'item/items.html', {
        'items': page_obj,  # paginated items
        'query': query,
        'categories': categories,
        'category_id': category_id,
        'sort': sort,
        'page_obj': page_obj,
    })



def detail(request, pk):
    item=get_object_or_404(Item, pk=pk)
    related_items=Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'item/detail.html',{
        'item':item,
        'related_items':related_items
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Create Item',
    })

@login_required
def delete(request,pk):
    item=Item.objects.get(pk=pk, created_by=request.user)

    item.delete()
    return redirect('dashboard:index')

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })