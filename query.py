"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

# A string/variable character string


# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

# An association table simplifies many to many relationships. It is a table that
# by itself has little meaning, but connects two tables. For example if you had 
# two different tables, one of kinds of smartphones, one of a bunch of different
# phone apps, to combine them without an association table you'd have multiple rows
# that saying x smartphone can run a,e,h, etc app or vice versa. With an association table
# both main tables can stay simple by only listing one specific phone type for each row
# in the other table one specific app for each row. Then in the association table all
# you use it for is to make the connections between the phone and the app without the
# mess/confusion/unreadability.


# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the ``id`` of "ram."
q1 = "Brand.query.filter_by(brand_id='ram').one()"

# Get all models with the name "Corvette" and the brand_id "che."
q2 = "Model.query.filter(Model.brand_id == 'che', Model.name=='Corvette').all()"

# Get all models that are older than 1960.
q3 = "Model.query.filter(Model.year < 1960).all()"

# Get all brands that were founded after 1920.
q4 = "Brand.query.filter(Brand.founded > 1920).all()"

# Get all models with names that begin with "Cor."
q5 = "Model.query.filter(Model.name.like('Cor%')).all()"

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = "Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()"

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = "Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()"

# Get any model whose brand_id is not "for."
q8 = "Model.query.filter(Model.brand_id != 'for').all()"


# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    model_info = db.session.query(Model.year, Brand.name, Brand.headquarters).filter(Model.year == year).all()

    print model_info

# get_model_info(1960)


def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""
    # year for brand not year for model? Since phrased year for brand I'll assume
    # you mean founded year. Maybe update this homework to have an output example?

    brands_summary = db.session.query(Brand.name, Model.name, Brand.founded).all()

    print brands_summary

# get_brands_summary()


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    brands_by_name = Brand.query.filter(Brand.name.like('%' + mystr + '%')).all()

    print brands_by_name

# search_brands_by_name('he')


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""


    models_between = Model.query.filter((Model.year > start_year) & (Model.year < end_year)).all()

    print models_between

# get_models_between(1956, 1959)
