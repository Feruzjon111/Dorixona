from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .forms import DorixonaForm
from .models import Dorixona

class HomeView(View):
    def get(self, request):
        dorixona = Dorixona.objects.all()[:4]
        context = {'dorixona': dorixona}
        return render(request, 'home.html', context)


class ProductsView(View):
    def get(self, request):
        dorixona = Dorixona.objects.all()
        context = {'dorixona': dorixona}
        return render(request, 'products.html', context)


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

class ProductCreateView(View):
    def get(self, request):
        form = DorixonaForm()
        return render(request, 'product_create.html', {'form': form})

    def post(self, request):
        form = DorixonaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
        return render(request, 'product_create.html', {'form': form})


class ProductDeleteView(View):
    def get(self, request, pk):
        dorixona = get_object_or_404(Dorixona, pk=pk)
        context = {'dorixona': dorixona}
        return render(request, 'product_delete.html', context)

    def post(self,request, pk):
        dorixona = get_object_or_404(Dorixona, pk=pk)
        dorixona.delete()
        return redirect('products')

class ProductUpdateView(View):
    def get(self, request, pk):
        dorixona = get_object_or_404(Dorixona, pk=pk)
        form = DorixonaForm(instance=dorixona)
        context = {'dorixona': dorixona, 'form': form}
        return render(request, 'product_update.html', context)

    def post(self, request, pk):
        dorixona = get_object_or_404(Dorixona, pk=pk)
        form = DorixonaForm(request.POST or None, request.FILES or None, instance=dorixona)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('detail', pk=dorixona.pk)
        context = {'form': form, 'dorixona': dorixona}
        return render(request, 'product_update.html', context)


class ProductDetailView(View):
    def get(self, request, pk):
        dorixona = get_object_or_404(Dorixona, pk=pk)
        context = {'dorixona': dorixona}
        return render(request, 'product_detail.html', context)

