from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class SortBoardsingCards(Resource):
    """
    class for Sorting Boarding Cards that accepts only JSON input

    """
    # POST method
    # curl http://localhost:5000/ -d "{"city":"Wwa", "sex":"Male"}"
    def post(self):

        json_data = request.get_json(force=True)
        return json_data


api.add_resource(SortBoardsingCards, '/')

if __name__ == '__main__':
    app.run(debug=True)