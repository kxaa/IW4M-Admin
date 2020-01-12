from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from master import app
import json

class Version(Resource):
    config_folder = './master/config/'
    master_file_name = 'master'
    def get(self, api_version=0):
        if api_version == 0:
            config = json.load(open('{0}/{1}.old.json'.format(Version.config_folder, Version.master_file_name)))
        else:
            config = json.load(open('{0}/{1}.json'.format(Version.config_folder, Version.master_file_name)))
        return { 
            'current-version-stable' : config['current-version-stable'],
            'current-version-prerelease' : config['current-version-prerelease']
         }, 200

    #@jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('current-version-stable')
        parser.add_argument('current-version-prerelease')
        parser.add_argument('jwt-secret', help='jwt-secret is required', required = True)
        args = parser.parse_args()

        config = json.load(open('{0}/{1}.json'.format(Version.config_folder, Version.master_file_name)))

        if args['current-version-stable'] != None:
            config['current-version-stable'] = args['current-version-stable']

        if args['current-version-prerelease'] != None:
            config['current-version-prerelease'] = args['current-version-prerelease']

        if args['jwt-secret'] == app.config['JWT_SECRET_KEY']:
            with open('{0}/{1}.json'.format(Version.config_folder, Version.master_file_name), 'w') as out_json:
                json.dump(config, out_json, indent=4)
    
            return { 'message': 'stable is {0}, prerelease is {1}'.format(config['current-version-stable'], config['current-version-prerelease']) }
        else :
            return { 'message': 'invalid jwt secret' }, 401