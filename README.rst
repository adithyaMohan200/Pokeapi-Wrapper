Pokeapi-Wrapper
===============

A wrapper for the Pokéapi in python
===================================

Purpose
=======

This wrapper simplifies the retrieval and parsing of data from the
database. All methods either return a string, number or a dictionary
that you can loop through to find what data you want. I will be adding
more features as time passes

Installation
===========

``sudo pip install PokeapiWrapper``

Usage
=====

First you must import the class like:

``from pokeapi import pokemon. Pokemon``

Then you must create an object of Pokemon and pass the name of the
pokemon you wish to retrieve information about like:

``charizard = Pokemon("charizard")``

Following are a list of methods that you can use currently:

``getMoves()`` This method returns a list of all the names of the moves
that the pokemon knows

``getName()`` This method returns the name of the pokemon

``getAbilities()`` This method returns a list of dictionaries. Each
dictionary contains an ``isHidden``, ``slot``, and ``name`` key for the
abilities

``getForms()`` This method returns a list of the forms of the pokemon

``getGameIndices()`` This method returns a list of dictionaries. Each
dictionary contains a ``gameIndex``, and ``version`` key for the games

``getHeldItems()`` This method returns the held items of the Pokemon.

``getLocationAreaEncounters()`` This method returns a list of names of
the Areas you can locate the pokemon.

``getSpecies()`` This method returns the species of the pokemon

``getStats()`` This method returns a list of dictionaries. Each
dictionary contains a ``baseStat``, ``effort``, and ``name`` of the
stats.

``getTypes()`` This method returns a list of dictionaries. Each
dictionary contains a ``slot``, and ``name`` of the types.

``getId(self)`` This method returns the ID of the pokemon.

``getBaseExperience()`` This method returns the Base Experience of the
pokemon.

``getHeight()`` This method returns the height of the pokemon.

``def isDefault()`` This method returns whether or not the pokemon is
default.

``getOrder()`` This method returns the order of the pokemon.

``getWeight()`` This method returns the weight of the pokemon.

``getMoveVersionDetails(move)`` Given a move this method returns a list
of dictionaries containing information about the version details of the
move.
``{'level':level,'versionName':versionName,'moveLearnMethod':moveLearnMethod``

``getLocationVersionDetails(area)`` Given a location this method returns
a list of dictionaries containing information about the version details
of the locations.
``{'maxChance':maxChance,'minLevel':minLevel,'maxLevel':maxLevel,'conditionValues':conditionValues,'chance':chance,'methodName':methodName,'versionName':versionName}``

Example
========
charizard = Pokemon("charizard")
print(charizard.getMoves())


Future Plans
============

My next goal will be to implement some other data retrieval using the
database including berries. I will also focus on making methods that can
compare pokemon in different ways and overall help you do more things
with the pokemon objects.
