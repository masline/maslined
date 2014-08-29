from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class Image(models.Model):
	description = models.CharField(max_length=50, verbose_name="Description of Image", blank=True)
	picture = models.ImageField(upload_to='imgs/full', db_index=True)

	def thumbnail(self):
		return '<img src="{0}" height="125px" />'.format(self.picture.url)
	thumbnail.allow_tags = True

	def __str__(self):
		return self.picture.name


@receiver(pre_save, sender=Image)
def article_remove_old_pics_on_save(sender, **kwargs):
	instance = kwargs['instance']
	if instance.id is not None:
		prev_image = sender.objects.get(id=instance.id).picture
		storage, path = prev_image.storage, prev_image.path
		storage.delete(path)


@receiver(post_delete, sender=Image)
def article_remove_old_pics_on_delete(sender, **kwargs):
	instance = kwargs['instance']
	prev_image = instance.picture
	storage, path = prev_image.storage, prev_image.path
	storage.delete(path)


class Logo(models.Model):
	description = models.CharField(max_length=50, verbose_name="Description of Logo", blank=True)
	picture = models.ImageField(upload_to='imgs/logo')

	def thumbnail(self):
		return '<img src="{0}" height="125px" />'.format(self.picture.url)
	thumbnail.allow_tags = True

	def __str__(self):
		return self.picture.name


@receiver(pre_save, sender=Logo)
def article_remove_old_pics_on_save(sender, **kwargs):
	instance = kwargs['instance']
	if instance.id is not None:
		prev_image = sender.objects.get(id=instance.id).picture
		storage, path = prev_image.storage, prev_image.path
		storage.delete(path)


@receiver(post_delete, sender=Logo)
def article_remove_old_pics_on_delete(sender, **kwargs):
	instance = kwargs['instance']
	prev_image = instance.picture
	storage, path = prev_image.storage, prev_image.path
	storage.delete(path)


class Manufacturer(models.Model):
	name = models.CharField(max_length=50, db_index=True)
	home_page = models.URLField(blank=True)
	logo = models.ForeignKey(Logo, blank=True)
	is_linecard = models.BooleanField(default=False)
	bio = models.TextField(blank=True)

	def logo_thumb(self):
		return '<img src="{0}" height="125px" />'.format(self.logo.picture.url)
	logo_thumb.allow_tags = True

	def __str__(self):
		return self.name


class Attribute(models.Model):
	name = models.CharField(max_length=50, db_index=True)
	position = models.PositiveSmallIntegerField(default=1)
	parent = models.ForeignKey('self', blank=True)

	def __str__(self):
		return self.name


class Price(models.Model):
	price = models.DecimalField(max_digits=15, decimal_places=7)
	min_qty = models.PositiveIntegerField()
	max_qty = models.PositiveIntegerField()

	def __str__(self):
		return '{min} - {max} @ ${price}'.format(min=self.min_qty, max=self.max_qty, price=self.price)


class Product(models.Model):
	item_no = models.CharField(max_length=50, verbose_name="The manufacturer supplied part number", db_index=True)
	manu_no = models.ForeignKey(Manufacturer)
	images = models.ManyToManyField(Image, blank=True)
	attributes = models.ManyToManyField(Attribute, blank=True)
	pricing = models.ManyToManyField(Price, blank=True)
	weight = models.DecimalField(max_digits=15, decimal_places=7, default=0)
	slug_url = models.SlugField(db_index=True)

	def thumbs(self):
		img_list = '<ul>'
		for img in self.images.all():
			img_list += '<li style="list-style-type: none;"><img src="{0}" height="50px" /></li>'.format(img.picture.url)
		img_list += '</ul>'
		if len(self.images.all()) == 0:
			return 'No pictures'
		else:
			return img_list
	thumbs.allow_tags = True

	def prices(self):
		price_tbl = '<table><thead><tr><th>Price</th><th>Min</th><th>Max</th></tr></thead><tbody>'
		for price_obj in self.pricing.all().order_by('min_qty'):
			price_tbl += '<tr><td>{price}</td><td>{min}</td><td>{max}</td></tr>'.format(
				price=price_obj.price, min=price_obj.min_qty, max=price_obj.max_qty)
		price_tbl += '</tbody></table>'
		if len(self.pricing.all()) == 0:
			return 'No prices'
		else:
			return price_tbl
	prices.allow_tags = True

	def __str__(self):
		return self.item_no