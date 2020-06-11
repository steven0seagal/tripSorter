from flask import Flask, request
from flask_restful import Resource, Api
from flasgger import Swagger, swag_from
from scripts import TripSorter
app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)



class SortBoardsingCards(Resource):
    """
    class for Sorting Boarding Cards that accepts only JSON input

    """
    # POST method
    # curl http://localhost:5000/ -d "{"city":"Wwa", "sex":"Male"}"
    @swag_from('tripsort.yml')
    def post(self):

        json_data = request.get_json(force=True)
        try:
            input = TripSorter(data=json_data)
            ordered_input = input.sort_all_data()
            result = input.print_out_complete(ordered_input)
            return result
        except:
            return 'Sorry your out input data is not correct ! ', 403

api.add_resource(SortBoardsingCards, '/')

if __name__ == '__main__':
    app.run(debug=True)