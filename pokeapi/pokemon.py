import requests
import json
class Pokemon:
    
    def __init__(self,poke):
        pokel = poke.lower()    
        pokemon = requests.get('http://pokeapi.co/api/v2/pokemon/' + pokel)
        self.info = json.loads(pokemon.text)
    def getMoves(self):
        
        moves=[]
        search = len(self.info['moves'])
        for i in range(0,search):
            moves.append(self.info['moves'][i]['move']['name'])
            
        return moves
    
    def getName(self):
        return self.info['name']
    
    def getAbilities(self):
        abilities = []
        
        for i in range(0,len(self.info['abilities'])):
            hidden = self.info['abilities'][i]['is_hidden']
            slot = self.info['abilities'][i]['slot']
            name= self.info['abilities'][i]['ability']['name']
            abilities.append({'isHidden':hidden,'slot':slot,'name':name})
        
        return abilities


    def getForms(self):
        forms=[]
        for i in range(0,len(self.info['forms'])):
            forms.append(self.info['forms'][i]['name'])
        
        return forms

    
    def getGameIndices(self):
        indices = []

        for i in range(0,len(self.info['game_indices'])):
            gameIndex  = self.info['game_indices'][i]['game_index']
            version = self.info['game_indices'][i]['version']['name']
            indices.append({'gameIndex':gameIndex,'version':version})
                
            return indices

    def getHeldItems(self):
        items=[]
        for i in range(0,len(self.info['held_items'])):
            items.append(self.info['held_items']['name'])
        return items

    def getLocationAreaEncounters(self):
        encounters=[]
        for i in range(0,len(self.info['location_area_encounters'])):
            encounters.append(self.info['location_area_encounters'][i]['location_area']['name'])
        
        return encounters

    def getSpecies(self):
        return self.info['species']['name']

    def getStats(self):
        stats=[]
        for i in range(0,len(self.info['stats'])):
            baseStat = self.info['stats'][i]['base_stat']
            effort = self.info['stats'][i]['effort']
            name = self.info['stats'][i]['stat']['name']
            stats.append({'baseStat':baseStat,'effort':effort,'name':name})
        return stats

    def getTypes(self):
        types=[]
        for i in range(0,len(self.info['types'])):
            slot = self.info['types'][i]['slot']
            name = self.info['types'][i]['type']['name']
            types.append({'slot':slot,'name':name})
        return types

    def getId(self):
        return self.info['id']
    
    def getBaseExperience(self):
        return self.info['base_experience']
    
    def getHeight(self):
        return self.info['height']

    def isDefault(self):
        return self.info['is_default']
    
    def getOrder(self):
        return self.info['order']

    def getWeight(self):
        return self.info['weight']

    def getMoveVersionDetails(self,move):
        details=[]
        for i in range(0,len(self.info['moves'])):
            if self.info['moves'][i]['move']['name'] == move:
                for j in range(0,len(self.info['moves'][i]['version_group_details'])):
                    level = self.info['moves'][i]['version_group_details'][j]['level_learned_at']
                    versionName = self.info['moves'][i]['version_group_details'][j]['version_group']['name']
                    moveLearnMethod = self.info['moves'][i]['version_group_details'][j]['move_learn_method']['name']
                    details.append({'level':level,'versionName':versionName,'moveLearnMethod':moveLearnMethod})
        
        return details

    def getLocationVersionDetails(self,area):
                details=[]
                for i in range(0,len(self.info['location_area_encounters'])):
                    if self.info['location_area_encounters'][i]['location_area']['name'] == area:
                        for j in range(0,len(self.info['location_area_encounters'][i]['version_details'])):
                            maxChance = self.info['location_area_encounters'][i]['version_details'][j]['max_chance']
                            versionName = self.info['location_area_encounters'][i]['version_details'][j]['version']['name']
                    for z in range(0,len(self.info['location_area_encounters'][i]['version_details'][j]['encounter_details'])):
                        minLevel = self.info['location_area_encounters'][i]['version_details'][j]['encounter_details'][z]['min_level']
                        maxLevel = self.info['location_area_encounters'][i]['version_details'][j]['encounter_details'][z]['max_level']
                        conditionValues = self.info['location_area_encounters'][i]['version_details'][j]['encounter_details'][z]['condition_values']
                        chance = self.info['location_area_encounters'][i]['version_details'][j]['encounter_details'][z]['chance']
                        methodName = self.info['location_area_encounters'][i]['version_details'][j]['encounter_details'][z]['method']['name']
                        details.append({'maxChance':maxChance,'minLevel':minLevel,'maxLevel':maxLevel,'conditionValues':conditionValues,'chance':chance,'methodName':methodName,'versionName':versionName})
                    
                return details
