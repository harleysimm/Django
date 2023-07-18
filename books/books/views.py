from django.shortcuts import render, redirect
from .models import Book
from django.http import HttpResponse
from .forms import BookForm
from django.contrib import messages
import sweetify
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission


book_str = '/books'


@login_required
def books_list(request):
    num_session = request.session.get('numero_visitas', 0)
    request.session['numero_visitas']= num_session + 1

    print('numero de visitas = ', num_session + 1)

    books = Book.objects.filter(owner= request.user)
    context = {'books': books} #datos de la base de datos
    return render(request, 'books_list.html', context)

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    context = {'book': book}
    return render(request, 'book_detail.html', context)
@permission_required('books.add_book')
def new_book(request):
    if request.method == 'POST':
        #guardar el nuevo libro
        values = request.POST.getlist('preferencia')
        COLOR_FAVORITO = "," .join(values)
        titulo = request.POST['titulo']
        editorial = request.POST['editorial']
        state = request.POST['state']
        type = request.POST['type']
        obj1 = Book(
            titulo = titulo,
            editorial = editorial,
            state = state,
            type = type,
            preferencia = COLOR_FAVORITO,
            owner = request.user
        )
        # if form.is_valid():
            # form.save()
        obj1.save()
        sweetify.toast(request, 'Cheers to new toast')
        messages.success(request, 'El libro se creó correctamente')
        return redirect(book_str)
    else:
        #ir al formulario en blanco
        form = BookForm
        return render(request, 'new_book.html', {'form': form})

def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if book.preferencia != "":
        selected_colors = book.preferencia.split(",")
    else:
        selected_colors = []

    selected_colors = [int(x) for x in selected_colors]
    # form = BookForm(request.POST, instance = book)
    # if form.is_valid():
    #     form.save()
    if request.method == 'POST':
        titulo = request.POST['titulo']
        editorial = request.POST['editorial']
        state = request.POST['state']
        type = request.POST['type']
        values = request.POST.getlist('preferencia')
        COLOR_FAVORITO = ",".join(values)
        book.titulo = titulo
        book.editorial = editorial
        book.state = state
        book.type = type
        book.preferencia = COLOR_FAVORITO
        book.save()
        messages.success(request, 'El libro se modificó correctamente')
        return redirect(book_str)
    return render(request, 'edit_book.html', {'book': book, 'states':Book.STATUS, 'types':Book.TIPOS_BOOK, 'preferencia':Book.COLOR_FAVORITO, 'selected_colors':selected_colors})

def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    messages.success(request, 'El libro se eliminó correctamente')
    return redirect('/books')
    