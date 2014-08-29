from django.shortcuts import render, Http404, HttpResponseRedirect
from django.core.mail import send_mail
from store.models import Manufacturer, Product
from store.forms import ContactForm


def index(request):
	return render(request, 'store/index.html')


def catalog(request):
	page_no = request.GET.get('p', '1')
	if page_no == 'all':
		next_page = None
		prev_page = None
		products = Product.objects.order_by('item_no')
	elif page_no.isdigit():
		page_no = int(page_no)
		num_products = Product.objects.count()
		if page_no > num_products:
			page_no -= 1
		elif page_no <= 0:
			page_no = 1
		prev_page = None if page_no == 1 else page_no - 1
		next_page = None if page_no >= num_products else page_no + 1
		products = Product.objects.order_by('item_no')[page_no - 1:page_no]
	else:
		return HttpResponseRedirect('/catalog')

	return render(request, 'store/catalog.html', {'products': products, 'next_page': next_page, 'prev_page': prev_page})


def product(request, item_slug):
	curr_product = Product.objects.get(slug_url=item_slug)
	return render(request, 'store/product.html', {'part': curr_product})


def linecard(request):
	linecards = Manufacturer.objects.filter(is_linecard=True)
	return render(request, 'store/linecard.html', {'manufacts': linecards})


def contact(request):
	if request.method == 'POST':
		submitted_form = ContactForm(request.POST)
		if submitted_form.is_valid():
			name = submitted_form.cleaned_data['name']
			company = submitted_form.cleaned_data['company']
			email = submitted_form.cleaned_data['email']
			phone = submitted_form.cleaned_data['phone']
			msg = submitted_form.cleaned_data['msg']

			email_msg = '{name} has contacted us from {company}.\nYou can reach him back at {email} and {phone}.\nHere is his message:\n\t{msg}'.format(
				name=name, company=company, email=email, phone=phone, msg=msg)

			send_mail('New message from a masline.com visitor!', email_msg, 'website@masline.com', ['wgordon@masline.com'])

			return HttpResponseRedirect('/')
		else:
			return render(request, 'store/contact_us.html', {'form': submitted_form})
	else:
		new_form = ContactForm()
		return render(request, 'store/contact_us.html', {'form': new_form})


def other(request, page_name):
	page_data = {
		'catalog': 'Masline\'s extensive catalog',
		'services': 'Masline\'s world renowned services',
		'about': 'us!',
		'news': 'some boring news',
	}.get(page_name, None)
	if page_data is None:
		raise Http404
	return render(request, 'store/other_pages.html', {'page_title': page_name.title(), 'page_data': page_data})