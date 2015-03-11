"""
Code examples from Chapter 7: Forms
#####################################################################

# Forms in Django
>>> from .forms import PersonDetailsForm

>>> f = PersonDetailsForm()
>>> print(f.as_p())
<p><label for="id_name">Name:</label> <input id="id_name" maxlength="100" name="name" type="text" /></p>
<p><label for="id_age">Age:</label> <input id="id_age" name="age" type="number" /></p>

>>> f.is_bound
False

>>> g = PersonDetailsForm({"name": "Blitz", "age": "30"})

>>> print(g.as_p())
<p><label for="id_name">Name:</label> <input id="id_name" maxlength="100" name="name" type="text" value="Blitz" /></p>
<p><label for="id_age">Age:</label> <input id="id_age" name="age" type="number" value="30" /></p>

>>> g.is_bound
True


# Why Does Data Need Cleaning?
>>> fill = {"name": "Blitz", "age": "30"}

>>> g = PersonDetailsForm(fill)

>>> g.is_valid()
True

>>> g.cleaned_data == {'age': 30, 'name': 'Blitz'}  # Dict ordering varies hence example changed
True

>>> type(g.cleaned_data["age"]) ==  type(1)  # Example changed as type represenation changes with Python version
True

"""
