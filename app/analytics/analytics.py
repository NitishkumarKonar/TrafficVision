from datetime import datetime


class TrafficAnalytics:

    def __init__(self):

        self.events = []

        self.total_vehicles = 0

        self.incoming = {
            "car": 0,
            "motorcycle": 0,
            "bus": 0,
            "truck": 0
        }

        self.outgoing = {
            "car": 0,
            "motorcycle": 0,
            "bus": 0,
            "truck": 0
        }

    def record_vehicle(
        self,
        vehicle_type,
        direction
    ):

        if vehicle_type not in self.incoming:
            return

        if direction == "IN":

            self.incoming[vehicle_type] += 1

        elif direction == "OUT":

            self.outgoing[vehicle_type] += 1

        else:

            return

        self.total_vehicles += 1

        event = {
            "timestamp": datetime.now().isoformat(),
            "vehicle_type": vehicle_type,
            "direction": direction
        }

        self.events.append(event)

    def get_summary(self):

        total_in = sum(
            self.incoming.values()
        )

        total_out = sum(
            self.outgoing.values()
        )

        return {
            "total": self.total_vehicles,

            "incoming": {
                "total": total_in,
                **self.incoming
            },

            "outgoing": {
                "total": total_out,
                **self.outgoing
            }
        }

    def get_events(self):

        return self.events.copy()

    def reset(self):

        self.events.clear()

        self.total_vehicles = 0

        for vehicle_type in self.incoming:
            self.incoming[vehicle_type] = 0
            self.outgoing[vehicle_type] = 0