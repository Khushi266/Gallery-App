from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Artwork, Bid
from .forms import BidForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def gallery(request):
    return render(request, 'gallery.html')
def ticket(request):
    return render(request, 'ticket.html')
def event(request):
    return render(request, 'event.html')
def contact(request):
    return render(request, 'contact.html')
def blog(request):
    return render(request, 'blog-home.html')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful registration
            messages.success(request, 'Your account has been created!')
            return redirect('gallery_home')  # Redirect to home after login
    else:
        form = UserCreationForm()
    return render(request, 'gallery/register.html', {'form': form})

def gallery_home(request):
    artworks = Artwork.objects.all()
    return render(request, 'gallery/home.html', {'artworks': artworks})

@login_required
def artwork_detail(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)
    bids = Bid.objects.filter(artwork=artwork).order_by('-bid_amount')
    


    return render(request, 'gallery/artwork_detail.html', {'artwork': artwork, 'bids': bids,})

@login_required
def payment_page(request, art_id):
    art_piece = get_object_or_404(Artwork, id=art_id)

    if request.method == 'POST':
        # Process the payment manually here (e.g., simulate successful payment)
        # Mark the art piece as sold
        art_piece.is_sold = True
        art_piece.save()

        # Redirect to a success page
        return redirect('payment_success', art_id=art_id)

    return render(request, 'gallery/payment.html', {'art_piece': art_piece})

def payment_success(request, art_id):
    art_piece = get_object_or_404(Artwork, id=art_id)
    return render(request, 'gallery/payment_success.html', {'art_piece': art_piece})

