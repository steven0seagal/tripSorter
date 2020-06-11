class TripSorter():
    """
    Trip Sorter takes data as dictionary and returns ordered list of trip

    """
    def __init__(self, data):
        self.data = data

    def sort_all_data(self):
        """
        This function takes self.data and return ordered dictionary of trips
        :return: dict --> ordered data
        """

        "Iterate through input data and create list of begining points and destinations "
        start_points = []
        destinations = []
        for trip,info in self.data.items():
            start_points.append(info['start_point'])
            destinations.append(info['end_point'])

        "Find beginning and endig of all journeys"
        for place1 in start_points:
            if place1 not in destinations:
                first_city = place1
        for place2 in destinations:
            if place2 not in  start_points:
                last_city = place2

        "Start ordering data"
        ordered_dict = {}
        current_start = first_city

        for i in range(len(self.data)):

            current_end = destinations[start_points.index(current_start)]
            for trip,info in self.data.items():
                if info["start_point"] == current_start and info["end_point"] == current_end:
                    ordered_dict[trip] = info
            current_start = current_end
        return ordered_dict


    def print_out_complete(self, ordered_data):
        """
        Function takes ordered dictionary and return instructions for all parts of journey
        :return: string with instructions
        """
        complete_instructions = ""
        stage = 1
        for trip,info in ordered_data.items():
            complete_instructions += "{}. ".format(stage)
            stage += 1
            # PLANE
            if info["transport_type"] == "plane":
                complete_instructions += "From {0}, take flight {1} to {2}. Gate {3}, seat {4}. ".format(info["start_point"],
                                        info["transport_number"], info["end_point"],info["gate/platform"], info["seat_number"])
                if info["baggage_info"] == "":
                    complete_instructions += "Baggage will be automatically transfered from your last leg."
                else:
                    complete_instructions += "Baggage drop at ticket counter {0}.\n".format(info["baggage_info"])
            #TRAIN
            elif info["transport_type"] == "train":
                complete_instructions += "Take train {0} from {1} to {2}. Sit in seat {3}.\n".format(info["transport_number"],
                                        info["start_point"],info["end_point"],info["seat_number"])
            #BUS
            elif info["transport_type"] == "bus":
                complete_instructions += "Take the {0} from {1} to {2}. ".format(info["transport_type"], info["start_point"],
                                        info["end_point"])
                if info["seat_number"] == "":
                    complete_instructions += "No seat assignment. \n"
                else:
                    complete_instructions += "Sit in seat {0}.".format(info["seat_number"])

        return complete_instructions





###
"Example usagg"
test = {
  "trip1": {'transport_type':'plane', 'start_point':'Denver','end_point':'Barcelona','transport_number':'SK22',
            'seat_number':'7b', 'gate/platform':'45B','baggage_info':'344'},
  "trip2": {'transport_type':'train', 'start_point':'New York','end_point':'Denver','transport_number':'78A',
            'seat_number':'44', 'gate/platform':'3.75','baggage_info':''},
  "trip3": {'transport_type':'bus', 'start_point':'Barcelona','end_point':'Madrit','transport_number':'Mf78',
            'seat_number':'98', 'gate/platform':'5','baggage_info':''}
}
test_input = TripSorter(data=test)
ordered_input = test_input.sort_all_data()
result = test_input.print_out_complete(ordered_input)
print(result)