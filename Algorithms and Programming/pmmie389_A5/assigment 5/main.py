import AirportUI
import AirportController
import Airport
import Plane
import Passenger

airport = Airport()
ctrl = AirportController(airport)
ui = AirportUI(ctrl)

ui.start()