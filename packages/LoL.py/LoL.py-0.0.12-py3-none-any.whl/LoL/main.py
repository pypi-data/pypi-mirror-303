import requests


class HTTPException(Exception):
    pass

class LoL():

    def __init__(self, api_key, region = 'na') -> None:
        self.__api_key = api_key
        self.__regions = {"americas":[['na','na1'],['br','br1'],['lan','la1'],['las','la2'],['oce','oc1']],
                        "europe":[["eune",'eun1'],["euw",'euw1'],["tr",'tr1'],["ru",'ru']],
                        "asia":[["kr","kr"],["jp","jp1"]]
                        }
        self.__v5_region, self.__v4_region = self.__get_regions(region)
        self.__url_key = f"?api_key={self.__api_key}"
        self.__base_url_1 = f"https://{self.__v4_region}.api.riotgames.com/lol"
        self.__base_url_2 = f"https://{self.__v5_region}.api.riotgames.com/lol"
        self.__version = self.__getVersion()

    def get_summoner(self, name:str =None, accountId =None, puuid =None, summonerid =None):
        """
        return: accountId, id, puuid, profileIconid, name, summonerLevel, revisionDate 
        """
        if name:
            name = name.split(":")
            game_name = name[0]
            tag = name[1]
            #url = f"{self.__base_url_1}/summoner/v4/summoners/by-name/{name}{self.__url_key}"
            url = f"{self.__base_url_1}/riot/account/v1/accounts/by-riot-id/{game_name}/{tag}{self.__url_key}"
        elif accountId:
            url = f"{self.__base_url_1}/summoner/v4/summoners/by-account/{accountId}{self.__url_key}"
        elif puuid:
            url = f"{self.__base_url_1}/summoner/v4/summoners/by-puuid/{puuid}{self.__url_key}"
        elif summonerid:
            url = f"{self.__base_url_1}/summoner/v4/summoners/{summonerid}{self.__url_key}"

        return self.__get_information(url)
    
    def get_champion_rotations(self):
        """
        return: maxNewPlayerLevel, freeChampionidsForNewPlayers: List[int], freeChampionids: List[int]
        """
        url = f"{self.__base_url_1}/platform/v3/champion-rotations{self.__url_key}"
        return self.__get_information(url)
    
    def get_all_champions(self):
        """
        return: list of champions with their names and keys: Dict
        """
        champion_data_url = f"http://ddragon.leagueoflegends.com/cdn/{self.__version}/data/en_US/champion.json"
        champion_info = self.__get_information(champion_data_url)
        champion_data = champion_info['data']
        champion_name_id = {}
        for champion in champion_data.keys():
            champion_name_id[champion_data[champion]['id']] = [champion_data[champion]['key'], champion_data[champion]['name']]

        return champion_name_id
    
    def get_champions_mastery_by_summonerId(self, summonerId:int):
        url = f"{self.__base_url_1}/champion-mastery/v4/champion-masteries/by-summoner/{summonerId}{self.__url_key}"
        return self.__get_information(url)
    
    def get_champion_mastery_by_summonerId_and_championId(self, summonerId:int, championId:int):
        url = f"{self.__base_url_1}/champion-mastery/v4/champion-masteries/by-summoner/{summonerId}/by-champion/{championId}{self.__url_key}"
        return self.__get_information(url)
    
    def get_matches_by_puuid(self, puuid:int):
        url = f"{self.__base_url_2}/match/v5/matches/by-puuid/{puuid}/ids{self.__url_key}"
        return self.__get_information(url)
    
    def get_match_by_matchid(self, matchid:str, timeline:bool=False):
        url = f"{self.__base_url_2}/match/v5/matches/{matchid}{self.__url_key}"
        if timeline is True:
            url = f"{self.__base_url_2}/match/v5/matches/{matchid}/timeline{self.__url_key}"
        return self.__get_information(url)
    
    def get_live_match_by_summonerId(self, summonerId: int):
        url = f"{self.__base_url_1}/spectator/v4/active-games/by-summoner/{summonerId}{self.__url_key}"
        return self.__get_information(url)
    
    def get_patch_version(self):
        return self.__getVersion()

    #regions
    def __get_regions(self, region):
        for v5_r in self.__regions.keys():
            for v4_r in self.__regions[v5_r]:
                if region.lower() in v4_r:
                    return v5_r, v4_r[1] 

    #helper
    def __get_information(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        else:
            return self.__get_status_error(r.status_code)

    def __getVersion(self):
        url = 'http://ddragon.leagueoflegends.com/api/versions.json'
        resp = requests.get(url)
        data = resp.json()
        return data[0]

    def __get_status_error(self, status):
        if status == 400:
            raise HTTPException("400 Error - Bad Request")
        elif status == 401:
            raise HTTPException("401 Error - Invalid URL")
        elif status == 404:
            raise HTTPException("404 Error - Summoner Not Found")
        elif status == 500:
            raise HTTPException("500 Error - Internal Server Error")
        else:
            raise HTTPException(str(status) + " Error - Unknown")
