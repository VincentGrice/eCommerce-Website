# ^Cvagrant@vagrant:/vagrant/eCommerce/src$ python managpy shell
# Python 2.7.12 (default, Dec  4 2017, 14:50:18)
# [GCC 5.4.0 20160609] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from tags.models import Tag
# >>> Tag.objects.all()
# <QuerySet [<Tag: orange>, <Tag: blue>, <Tag: pink>, <Tag: insta>]>
# >>> Tag.objects.last()
# <Tag: insta>
# >>> black = Tag.objects.last()
# >>> black.title
# u'insta'
# >>> black.slug
# u'ig'
# >>> black.active
# True
# >>> black.products
# <django.db.models.fields.related_descriptors.ManyRelatedManager object at 0x7ff790bbec10>
# >>> black.products.all()
# <ProductQuerySet [<Product: Instagram quilt>]>
# >>> insta = Tag.objects.last()
# >>> insta.title
# u'insta'
# >>> insta.products.all().first()
# <Product: Instagram quilt>
# >>> exit()
# vagrant@vagrant:/vagrant/eCommerce/src$ python manage.py shell
# Python 2.7.12 (default, Dec  4 2017, 14:50:18)
# [GCC 5.4.0 20160609] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from products.models import product
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# ImportError: cannot import name product
# >>> from products.models import Product
# >>> qs = Product.objects.all()
# >>> qs
# <ProductQuerySet [<Product: FAMU rattlers quilt>, <Product: Cancer Awareness Quilt>, <Product: Dallas Cowboys Quilt>, <Product: Instagram quilt>]>
# >>> famu = qs.first()
# >>> famu
# <Product: FAMU rattlers quilt>
# >>> famu.title
# u'FAMU rattlers quilt'
# >>> famu.description
# u'This is an awesome quilt for practice'
# >>> famu.tags
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# AttributeError: 'Product' object has no attribute 'tags'
# >>> famu.tag_set
# <django.db.models.fields.related_descriptors.ManyRelatedManager object at 0x7f38df553510>
# >>> famu.tag_set.all()
# <QuerySet [<Tag: orange>]>
# >>>
