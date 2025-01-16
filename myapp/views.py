from django.shortcuts import render

# Create your views here.
from django.db import transaction
from django.shortcuts import redirect, render,get_object_or_404
from .models import Member, wronginvoice
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    mem=Member.objects.all()
    return render(request,'index.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrec(request):

    x = request.POST.get('bill_number', '')


    y = request.POST.get('details_received', 'off') == 'on'  # Convert to boolean
    z = request.POST.get('date_received', None)  # Defaults to None if not provided
    #a = request.POST.get('invoice_correct', 'off') == 'on'  # Convert to boolean
    b = request.POST.get('date_corrected', None)  # Defaults to None if not provided
    c = request.POST.get('balance', 0.0)  # Defaults to 0.0 if not provided


    mem = Member(
        bill_number=x,
        details_received=y,
        date_received=z if z else None,  # Ensure None for blank values
        #invoice_correct=a,
        date_corrected=b if b else None,  # Ensure None for blank values
        balance=c
    )
    mem.save()

    return redirect("/")


def delete(request,id):
    mem=Member.objects.get(id=id)
    if mem.balance == 0:
        mem.delete()
    return redirect("/")

def update(request,id):
    mem=Member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request, id):
    # Fetch required fields from the form
    x = request.POST.get('bill_number', '')

    # Fetch optional fields with default handling
    y = request.POST.get('details_received') == 'yes'  # Convert to boolean
    z = request.POST.get('date_received') or None # Defaults to None if not provided
    a = request.POST.get('invoice_correct') == 'yes'  # Convert to boolean
    b = request.POST.get('date_corrected') or None # Defaults to None if not provided
    c = request.POST.get('balance', 0.0)  # Defaults to 0.0 if not provided

    # Update the database record
    mem = Member.objects.get(id=id)
    mem.bill_number = x
    mem.details_received = y
    #date_received = request.POST.get('date_received')
    if z is not None:
        mem.date_received = z  # Ensure None for blank values
    mem.invoice_correct = a
    if b is not None:
        mem.date_corrected = b  # Ensure None for blank values
    mem.balance = c
    # if mem.details_received and not mem.date_received:
    #     mem.date_received = request.POST.get('date_received', None)
    # mem.invoice_correct = request.POST.get('invoice_correct') == 'yes'
    # if mem.invoice_correct and not mem.date_corrected:
    #     mem.date_corrected = request.POST.get('date_corrected', None)
    mem.save()

    return redirect("/")

#def incorrect_invoices(request):
    # Get all the bills where invoice_correct is False (or 'no')
    #incorrect_bills = Member.objects.filter(invoice_correct=False, details_received = True)

    # Pass the filtered bills to the template
    #return render(request, 'wrong.html', {'mem': incorrect_bills})


@transaction.atomic
def wrong_invoice_page(request):
    # Get all matching bills
    bills = Member.objects.filter(invoice_correct=False, details_received=True)

    wrong_invoices = []  # To store the created objects
    for bill in bills:
        # Create the wronginvoice object for each bill
        if not wronginvoice.objects.filter(bill_number=bill.bill_number).exists():
            wrong_invoice = wronginvoice.objects.create(
                bill_number=bill.bill_number,
                balance=bill.balance
            )
            wrong_invoices.append(wrong_invoice)  # Keep track of created objects
        existing_wrong_invoices = wronginvoice.objects.all()
    # Render a response (adjust template as needed)
    return render(request, 'wrong.html', {'bills': bills, 'existing_wrong_invoices': existing_wrong_invoices})

# def wrong_invoice_page(request):
#     wrong_invoices = wronginvoice.objects.all()
#     return render(request, 'wrong.html', {'wrong_invoices': wrong_invoices})

def delete_wrong(request,id):
    wrong_invoices=wronginvoice.objects.get(id=id)
    if wrong_invoices.balance == 0:
        wrong_invoices.delete()
    return redirect("/wrong")

def update_wrong(request,id):
    wrong_invoices=wronginvoice.objects.get(id=id)
    return render(request,'update_wrong.html',{'wrong_invoices':wrong_invoices})

def uprec_wrong(request, id):
    # Fetch required fields from the form
    x = request.POST.get('bill_number', '')

    # Fetch optional fields with default handling
    y = request.POST.get('details_received') == 'yes'  # Convert to boolean
    z = request.POST.get('date_received') or None # Defaults to None if not provided
    #a = request.POST.get('invoice_correct') == 'yes'  # Convert to boolean
    #b = request.POST.get('date_corrected') or None # Defaults to None if not provided
    c = request.POST.get('balance', 0.0)  # Defaults to 0.0 if not provided

    # Update the database record
    wrong_invoices = wronginvoice.objects.get(id=id)
    wrong_invoices.bill_number = x
    wrong_invoices.details_received = y
    #date_received = request.POST.get('date_received')
    if z is not None:
        wrong_invoices.date_received = z  # Ensure None for blank values
    #mem.invoice_correct = a
    #if b is not None:
        #mem.date_corrected = b  # Ensure None for blank values
    wrong_invoices.balance = c
    # if mem.details_received and not mem.date_received:
    #     mem.date_received = request.POST.get('date_received', None)
    # mem.invoice_correct = request.POST.get('invoice_correct') == 'yes'
    # if mem.invoice_correct and not mem.date_corrected:
    #     mem.date_corrected = request.POST.get('date_corrected', None)
    wrong_invoices.save()

    return redirect("/wrong")

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages


@login_required
def home(request):
    return render(request, 'home.html')


# def register_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']
#         if password == confirm_password:
#             try:
#                 user = User.objects.create_user(username=username, password=password, email=email)
#                 user.save()
#                 login(request, user)
#                 return redirect('index')
#             except:
#                 messages.error(request, 'Username already exists.')
#         else:
#             messages.error(request, 'Passwords do not match.')
#     return render(request, 'registration/login.html')

def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('sname')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        new_user = User.objects.create_user(name, email, password)
        new_user.first_name = fname
        new_user.last_name = lname

        new_user.save()
        return redirect('login')

    return render(request, 'registration/register.html', {})

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('Error, user does not exist')


    return render(request, 'registration/login.html', {})