from django.shortcuts import render, get_object_or_404
from .models import BookStore, Book
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from core.models import User

# custom exception for not getting books
class NoBookException(Exception):
    pass

def login_view(request):
   if request.method == 'POST':
       username = request.POST['name']
       password = request.POST['password']
       user = authenticate(request, username=username, password=password)
       if user is not None:
           login(request, user)
           return render(request, 'user_detail.html', {'user': user})
   return render(request, 'login.html')

def get_books(request):
    user_id = request.user.id
    try:    
        store_id = BookStore.objects.get(user_id=user_id).id
        books_queryset = Book.objects.filter(store_id=store_id)
    except BookStore.DoesNotExist:
        return render(request, 'books.html', {'books':[]})   
        
    return render(request, 'books.html', {'books':list(books_queryset)})

def add_to_books(request):
    if request.method == 'POST':
      title = request.POST['title']
      author = request.POST['author']
      date = request.POST['date']
      
      ## getting user store id
      user_id = request.user.id
      try:
        store_id = BookStore.objects.get(user_id=user_id).id
      except BookStore.DoesNotExist:
        store = BookStore.objects.create(user_id=user_id) 
        store_id = store.id

      book = Book(title=title, author=author, publication_year=date, store_id=store_id)
      book.save()     
      
    return redirect('book_details')

def update_book(request):    
    if request.method == 'POST':
        # Get the updated data from the form
        id = request.POST.get('id')
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_date = request.POST.get('publication_date')

        book = get_object_or_404(Book, id=id)

        # Update the book's attributes
        book.title = title if title != "" else book.title
        book.author = author if author != "" else book.author
        book.publication_year = publication_date if publication_date != None else book.publication_year

        # Save the updated book to the database
        book.save()

        # Redirect to book detailpage
        return redirect('book_details')
    
def register(request):
    if request.method == 'POST':
        # Get the form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create a new user
        User.objects.create_user(username=username, email=email, password=password)
        

        # Redirect to login page
        return redirect('login')
    return render(request, 'register.html')


def delete_book(request):

    if request.method == 'POST':

        book_id = request.POST.get('id')
        book = get_object_or_404(Book, id=book_id)
        
        # Delete the book
        book.delete()

        # Redirect to the book list 
        return redirect('book_details')

    

    


    