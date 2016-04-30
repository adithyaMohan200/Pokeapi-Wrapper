# Pok-api-Wrapper
#A wrapper for the Pokéapi in python

# Purpose

This wrapper simplifies the retrieval and parsing of data from the database. All methods either return a string, number or a dictionary that you can loop through to find what data you want. I will be adding more features as time passes 

# Usage

First you must import the class like: 

`import Pokemon `

Then you must create an object of Pokemon and pass the name of the pokemon you wish to retrieve information about like:

` charizard = Pokemon("charizard") `

Following are a list of methods that you can use currently:

`getMoves()`
    This method returns a list of all the names of the moves that the pokemon knows
    
  `getName()`
    This method returns the name of the pokemon
    
  `getAbilities()`
    This method returns a list of dictionaries. Each dictionary contains an `isHidden`, `slot`, and `name` key for the abilities
    
  `getForms()`
    This method returns a list of the forms of the pokemon
    
  `getGameIndices()`
    This method returns a list of dictionaries. Each dictionary contains a `gameIndex`, and `version` key for the games
    
  `getHeldItems()`
    This method returns the held items of the Pokemon.
  
  `getLocationAreaEncounters()`
    This method returns a list of names of the Areas you can locate the pokemon.
    
  `getSpecies()`
    This method returns the species of the pokemon
    
  `getStats()`
    This method returns a list of dictionaries. Each dictionary contains a `baseStat`, `effort`, and `name` of the stats.
    
  `getTypes()`
    This method returns a list of dictionaries. Each dictionary contains a `slot`, and `name` of the types.
    
  `getId(self)`
    This method returns the ID of the pokemon.

  `getBaseExperience()`
    This method returns the Base Experience of the pokemon.

  `getHeight()`
    This method returns the height of the pokemon.

  `def isDefault()`
    This method returns whether or not the pokemon is default.

  `getOrder()`
    This method returns the order of the pokemon.
    
  `getWeight()`
    This method returns the weight of the pokemon.
    
  `getMoveVersionDetails(move)`
    Given a move this method returns a list of dictionaries containing information about the version details of the move.
    
    `{'level':level,'versionName':versionName,'moveLearnMethod':moveLearnMethod`
    
  `getLocationVersionDetails(area)`
    Given a location this method returns a list of dictionaries containing information about the version details of the locations.
    ```
    {'maxChance':maxChance,'minLevel':minLevel,'maxLevel':maxLevel,'conditionValues':conditionValues,'chance':chance,'methodName':methodName,'versionName':versionName}
    ```
    
  #Examples
    
    #Input
      ```
      pok = Pokemon("eevee")
      print (pok.returnLocationVersionDetails("castelia-city-area"))
      ```
    
    #Output
      ```
      [{'methodName': u'dark-grass', 'versionName': u'black-2', 'maxChance': 10, 'minLevel': 19, 'chance': 4, 'conditionValues': [], 'maxLevel': 19}, {'methodName': u'dark-grass', 'versionName': u'black-2', 'maxChance': 10, 'minLevel': 19, 'chance': 1, 'conditionValues': [], 'maxLevel': 19}, {'methodName': u'walk', 'versionName': u'black-2', 'maxChance': 10, 'minLevel': 18, 'chance': 4, 'conditionValues': [], 'maxLevel': 18}, {'methodName': u'walk', 'versionName': u'black-2', 'maxChance': 10, 'minLevel': 18, 'chance': 1, 'conditionValues': [], 'maxLevel': 18}, {'methodName': u'dark-grass', 'versionName': u'white-2', 'maxChance': 10, 'minLevel': 19, 'chance': 4, 'conditionValues': [], 'maxLevel': 19}, {'methodName': u'dark-grass', 'versionName': u'white-2', 'maxChance': 10, 'minLevel': 19, 'chance': 1, 'conditionValues': [], 'maxLevel': 19}, {'methodName': u'walk', 'versionName': u'white-2', 'maxChance': 10, 'minLevel': 18, 'chance': 4, 'conditionValues': [], 'maxLevel': 18}, {'methodName': u'walk', 'versionName': u'white-2', 'maxChance': 10, 'minLevel': 18, 'chance': 1, 'conditionValues': [], 'maxLevel': 18}]
      ```
      
    #Input 
      ```
      pok = Pokemon("eevee")
      print (pok.getMoves())
      ```
      
    #Output
      ```
      [u'sand-attack', u'headbutt', u'tackle', u'body-slam', u'take-down', u'double-edge', u'tail-whip', u'bite', u'growl', u'dig', u'toxic', u'quick-attack', u'rage', u'mimic', u'double-team', u'reflect', u'focus-energy', u'bide', u'swift', u'skull-bash', u'rest', u'substitute', u'snore', u'curse', u'flail', u'protect', u'mud-slap', u'detect', u'endure', u'charm', u'swagger', u'attract', u'sleep-talk', u'heal-bell', u'return', u'frustration', u'baton-pass', u'iron-tail', u'hidden-power', u'rain-dance', u'sunny-day', u'shadow-ball', u'facade', u'helping-hand', u'wish', u'yawn', u'refresh', u'secret-power', u'hyper-voice', u'fake-tears', u'tickle', u'covet', u'natural-gift', u'trump-card', u'last-resort', u'captivate', u'synchronoise', u'round', u'echoed-voice', u'stored-power', u'retaliate', u'work-up', u'confide', u'baby-doll-eyes']
      ```


#Future Plans
  My next goal will be to implement some other data retrieval using the database including berries. I will also focus on making methods that can compare pokemon in different ways and overall help you do more things with the pokemon objects.
  
    
  
  
    
  `
  
