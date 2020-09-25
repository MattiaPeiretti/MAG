import constants
import requests
import json

class ImageRetriever:
    def __init__(self, project_path):
        self.project_path = project_path
        self.query = {}
        self.images = []

    def set_query(self, rover, date, camera='', earth_date=False):
        
        if not rover:
            return False
        if not date:
            return False
        if not rover in constants.ROVERS:
            return False

        self.query = {
            'rover': rover,
            'date': date,
            'camera': camera,
            'earth_date': earth_date
        }

    def run(self):
        if not self.query:
            return False
        
        api_hyperlink = build_api_hyperlink(self.query['rover'], self.query['date'], self.query['camera'], self.query['earth_date'])
        
        res = requests.get(api_hyperlink)
        parsed = json.loads(res.text)
        print(json.dumps(parsed, indent=4))


    def images(self):
        pass


def build_api_hyperlink(rover, date, camera, earth_date=False):
    query = ''

    if not rover:
        return False
    if not date:
        return False
    if not rover in constants.ROVERS:
        return False
    
    if earth_date:
        query = constants.API_BASE_HYPERLINK + rover + '/photos?earth_date=' + date
    else:
        query = constants.API_BASE_HYPERLINK + rover + '/photos?sol=' + str(date)

    if camera:
        query += f'&camera={camera}'
    
    return f'{query}&api_key={constants.API_KEY}'


    

        
        

    

