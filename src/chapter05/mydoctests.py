"""
Code examples from Chapter 5: Templates
#####################################################################

# Understanding Django’s Template Language
>>> "<h1>{title}</h1>".format(title="SuperBook")
'<h1>SuperBook</h1>'

>>> from django.template import Template, Context
>>> Template("<h1>{{ title }}</h1>").render(Context({"title": "SuperBook"}))
'<h1>SuperBook</h1>'


>>> class DrOct:
...     arms = 4
...     def speak(self):
...         return "You have a train to catch."
>>> mydict = {"key":"value"}
>>> mylist = [10, 20, 30]


>>> "Dr. Oct has {0} arms and says: {1}".format(DrOct().arms, DrOct().speak())
'Dr. Oct has 4 arms and says: You have a train to catch.'
>>> mydict["key"]
'value'
>>> mylist[1]
20

>>> s = DrOct()
>>> def t(s, context=locals()):
...     return Template(s).render(Context(context))

>>> t("Dr. Oct has {{ s.arms }} arms and says: {{ s.speak }}")
'Dr. Oct has 4 arms and says: You have a train to catch.'
>>> t("{{ mydict.key }}")
'value'
>>> t("{{ mylist.1 }}")
'20'


# Filters
>>> title="SuperBook"
>>> title.upper()[:5]
'SUPER'
>>> t("{{ title|upper|slice:':5' }}")
'SUPER'

# Tags
# Uses dummy time since now() can vary 
>>> if 1==1:
...     print(" Date is {0} ".format("31-08-2014"))            # doctest: +NORMALIZE_WHITESPACE
 Date is 31-08-2014
>>> t("{% if 1 == 1 %} Date is 31-08-2014 {% endif %}")        # doctest: +NORMALIZE_WHITESPACE
' Date is 31-08-2014 '
""" 
