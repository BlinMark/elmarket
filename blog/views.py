from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .models import Category, Product
from cart.forms import CartAddProductForm
from .forms import OrderCreateForm
from django.contrib.auth.models import User


# Страница всех новостей
def about(request): #post_list
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/about.html', {'posts': posts}) #'blog/post_list.html'


# Страница конкретной новости
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# Начальная страница
def index(request):
    home_page = Post.objects.all().order_by('-pub_date')
    context = {'home_page': home_page}
    return render(request, 'blog/index.html', {'index': index})


# О нас
def post_list(request): #about
    about_page = Post.objects.all().order_by('-pub_date')
    context = {'about_page': about_page}
    return render(request, 'blog/about.html', {'about': about})


# Блог
def blog(request):
    blog_page = Post.objects.all().order_by('-pub_date')
    context = {'blog_page': blog_page}
    return render(request, 'blog/blog_z.html', {'blog': blog})


# Страница с товарами
def ProductList(request, category_slug=None, template='blog/list.html', page_template='blog/list_page.html'):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if request.is_ajax():
        template = page_template
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, template, {
        'category': category,
        'categories': categories,
        'products': products,
        'page_template': page_template
    })


############

# Страница товара
def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    form = OrderCreateForm()

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        form.save(commit=True)

    return render(request, 'blog/base_product.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'form': form})


def admin(request):
    if auth.get_user(reuest).is_authenticated:
        return redirect('/admin/')
    else:
        return redirect('/admin/login/?next=/admin/')

