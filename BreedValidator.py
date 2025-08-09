import re

class BreedValidator:
    def __init__(self):
        self.ignoreBreedKeys = ["allamericandog", "gooldendoodle"]
        self.ignoreBreeds = [
            'All American Dog', 'Gooldendoodle', 'All American Dogs', 'Gooldendoodles']

    def getBreedWords(self, breed):
        words = re.sub(r'[^a-zA-Z\s]', '', breed).lower().split()
        words.sort()
        # remove ending 's' from each word
        words = [word.rstrip('s') for word in words if word]

        return words

    def getBreedKey(self, breed):
        if breed in self.ignoreBreeds:
            return None

        breed_normalizations = [
            {"names": ["ANATOLIAN SHEPHERD"],
                "officialName": "Anatolian Shepherd Dog"},
            {"names": ["Appenzeller Sennenhundes", "APPENZELLER SENNENHUNDE"],
                "officialName": "Appenzeller Sennenhund"},
            {"names": ["Beagles (13 Inch)", "Beagles (15 Inch)", "Beagle (13 Inch)", "Beagle (15 Inch)",
                       "Beagles, Over 13 In But Not Exceeding 15 In", "Beagles, Not Exceeding 13 In"], "officialName": "Beagle"},
            {"names": ["BERGAMASCO"], "officialName": "Bergamasco Sheepdog"},
            {"names": ["Black & Tan Coonhounds"],
                "officialName": "Black and Tan Coonhound"},
            {"names": ["Bracchi Italiani", "Bracco Italiani",
                       "Bracchi Italiano"], "officialName": "Bracco Italiano"},
            {"names": ["BRAQUE FRANCAIS PYRENEES"],
                "officialName": "Braque Francais Pyrenean"},
            {"names": ["DANISH BROHOLMER"], "officialName": "Broholmer"},
            {"names": ["Bull Terriers (White)", "Bull Terriers (Colored)",
                       "Bull Terrier (Colored)"], "officialName": "Bull Terrier"},
            {"names": ["CANAAN"], "officialName": "Canaan Dog"},
            {"names": ["CARPATHIAN SHEPHERD"],
                "officialName": "Romanian Carpathian Shepherd"},
            {"names": ["LOUISIANA CATAHOULA LEOPARD"],
                "officialName": "Catahoula Leopard Dog"},
            {"names": ["CAUCASIAN SHEPHERD"],
                "officialName": "Caucasian Shepherd Dog"},
            {"names": ["CENTRAL ASIAN SHEPHERD"],
                "officialName": "Central Asian Shepherd Dog"},
            {"names": ["Cirnechi dell'Etna"],
                "officialName": "Cirneco dell'Etna"},
            {"names": ["Chihuahuas (Smooth Coat)", "Chihuahuas (Long Coat)",
                       "Chihuahua (Long Coat)"], "officialName": "Chihuahua"},
            {"names": ["Collies (Rough)", "Collie (Rough)", "Collies (Smooth)",
                       "Collie (Smooth)"], "officialName": "Collie"},
            {"names": ["Czechoslovakian Vlcaks"],
                "officialName": "Czechoslovakian Vlciak"},
            {"names": ["Dachshunds (Longhaired)", "Dachshund (Longhaired)", "Dachshund (Wirehaired)",
                       "Dachshunds (Wirehaired)", "Dachshunds (Smooth)"], "officialName": "Dachshund"},
            {"names": ["DANISH SWEDISH FARMDOG"],
                "officialName": "Danish-Swedish Farmdog"},
            {"names": ["Deutscher Wachtelhunde"],
                "officialName": "Deutscher Wachtelhund"},
            {"names": ["Drentsche Patrijshonden"],
                "officialName": "Drentsche Patrijshond"},
            {"names": ["English Toy Spaniels (B & P C)", "English Toy Spaniels (K C & R)", "English Toy Spaniel (Blenheim & Prince Charles)", "English Toy Spaniel (King Charles& Ruby)",
                       "English Toy Spaniels (Blenheim & Prince Charles)", "English Toy Spaniels (King Charles & Ruby)"], "officialName": "English Toy Spaniel"},
            {"names": ["Golden Retiever"], "officialName": "Golden Retriever"},
            {"names": ["Grand Basset Griffon Vendeens", "GRAND BASSET GRIFFON VENDEEN"],
                "officialName": "Grand Basset Griffon Vendéen"},
            {"names": ["HANOVERIAN HOUND"],
                "officialName": "Hanoverian Scenthound"},
            {"names": ["HOKKAIDO KEN"], "officialName": "Hokkaido"},
            {"names": ["Jindos", "JINDO"], "officialName": "Korean Jindo Dog"},
            {"names": ["Keeshonden"], "officialName": "Keeshond"},
            {"names": ["Komondorok"], "officialName": "Komondor"},
            {"names": ["Kuvaszok"], "officialName": "Kuvasz"},
            {"names": ["IRISH RED & WHITE SETTER"],
                "officialName": "Irish Red and White Setter"},
            {"names": ["Lowchen"], "officialName": "Löwchen"},
            {"names": ["Manchester Terrier", "Manchester Terriers",
                       "MANCHESTER TERRIER/STANDARD"], "officialName": "Manchester Terrier Standard"},
            {"names": ["Mudik"], "officialName": "Mudi"},
            {"names": ["NOVA SCOTIA DUCK TOLLING RET."],
                "officialName": "Nova Scotia Duck Tolling Retriever"},
            {"names": ["Perro de Presa Canario"],
                "officialName": "Presa Canario"},
            {"names": ["Petits Bassets Griffons Vendeens", "Petit Basset Griffon Vendeens",
                       "Petit Basset Griffon Vendeen"], "officialName": "Petit Basset Griffon Vendéen"},
            {"names": ["Plotts", "PLOTT"], "officialName": "Plott Hound"},
            {"names": ["Poodle", "Poodles"],
                "officialName": "Poodle (Standard)"},
            {"names": ["Poodle/Miniature"],
                "officialName": "Poodle (Miniature)"},
            {"names": ["PORCELAINE HOUND"], "officialName": "Porcelaine"},
            {"names": ["Pulik"], "officialName": "Puli"},
            {"names": ["Pumik"], "officialName": "Pumi"},
            {"names": ["Russian Tsvetnaya Blonkas",
                       "Russian Tsvetnaya Blonka (Misc Effective 1/1/2023)"], "officialName": "Russian Tsvetnaya Bolonka"},
            {"names": ["ROMANIAN MIORITIC SHEEPDOG"],
                "officialName": "Romanian Mioritic Shepherd Dog"},
            {"names": ["Segugi Italiani"], "officialName": "Segugio Italiano"},
            {"names": ["Setter (Irish) Red & White", "Setter (Irish) Red and White"],
             "officialName": "Irish Red and White Setter"},
            {"names": ["Siberian Huskies"], "officialName": "Siberian Husky"},
            {"names": ["Small Munsterlander Pointers"],
                "officialName": "Small Munsterlander"},
            {"names": ["Soft-Coated Wheaten Terriers"],
                "officialName": "Soft Coated Wheaten Terrier"},
            {"names": ["Spaniels (Cocker) Parti-Color", "Spaniel (Cocker) Parti-Color", "Spaniels (Cocker) Ascob",
                       "Spaniel (Cocker) Ascob", "Spaniels (Cocker) Black"], "officialName": "Cocker Spaniel"},
            {"names": ["Spinoni Italiani"],
                "officialName": "Spinone Italiano"},
            {"names": ["St. Bernards", "ST. BERNARD"],
                "officialName": "Saint Bernard"},
            {"names": ["WACHTELHUND"],
                "officialName": "Deutscher Wachtelhund"},
        ]

        breedName = breed
        for entry in breed_normalizations:
            if breed.lower() in [name.lower() for name in entry["names"]]:
                breedName = entry["officialName"]
                break

        words = self.getBreedWords(breedName)
        return ''.join(words).replace(" and ", "").replace(" ", "").rstrip("s")

    def getBreedKeyMap(self, dbBreeds):
        breedKeyMap = {}
        for dbBreed in dbBreeds:
            # create a map of nameKey to breed object
            breedKeyMap[dbBreed['nameKey']] = dbBreed

        return breedKeyMap

    def getBreedKeyToWordsMap(self, dbBreeds):
        breedKeyToWordsMap = {}
        for dbBreed in dbBreeds:
            breedKeyToWordsMap[dbBreed['nameKey']
                               ] = self.getBreedWords(dbBreed['breedName'])

        return breedKeyToWordsMap

    def isValidBreed(self, breed, dbBreeds):
        # check if the breed is in the ignore list
        breedKey = self.getBreedKey(breed)
        if breedKey is None or breedKey == '':
            return False

        if breedKey in self.ignoreBreedKeys:
            return False

        # check if the breed is in the database
        breedKeyMap = self.getBreedKeyMap(dbBreeds)
        if breedKey in breedKeyMap:
            return True

        breedWords = self.getBreedWords(breed)
        breedKeyToWordsMap = self.getBreedKeyToWordsMap(dbBreeds)
        # loop through the breedKeyToWordsMap to find the most matches between the breedWords and the words in the breedKeyToWordsMap
        bestMatchKey = None
        bestMatchCount = 0
        for key, words in breedKeyToWordsMap.items():
            matchCount = len(set(breedWords) & set(words))
            if matchCount > bestMatchCount:
                bestMatchCount = matchCount
                bestMatchKey = key
        if bestMatchKey is not None:
            # print(f'Found best match for {breed}: {breedKeyMap[bestMatchKey]["breedName"]} with {bestMatchCount} matches')
            return True
        else:
            return False

    def getOfficialBreedName(self, breed, breedKeyMap):
        if breedKeyMap is None or not isinstance(breedKeyMap, dict):
            return None

        # check if the breed is in the ignore list
        breedKey = self.getBreedKey(breed)
        if breedKey is None or breedKey == '':
            return None

        if breedKey in self.ignoreBreedKeys:
            return None

        # check if the breed is in the breedKeyMap
        if breedKey in breedKeyMap:
            return breedKeyMap[breedKey]['breedName']

        # if not found, return None
        return None

    def getBreedNameFromOfaKey(self, ofaKey, dbBreeds):
        if dbBreeds is None or not isinstance(dbBreeds, list):
            return None

        if ofaKey is None or ofaKey == '':
            return None

        dbBreed = None
        for breed in dbBreeds:
            if 'ofaKey' in breed and breed['ofaKey'] == ofaKey:
                dbBreed = breed
                break

        if dbBreed is not None:
            return dbBreed['breedName']

        # if not found, return None
        return None

    def getOfaBreedKeys(self, dbBreeds):
        if dbBreeds is None or not isinstance(dbBreeds, list):
            return []
        
        breedKeys = []
        for dbBreed in dbBreeds:
            if 'ofaKey' in dbBreed:
                breedKeys.append(dbBreed['ofaKey'])

        return breedKeys
