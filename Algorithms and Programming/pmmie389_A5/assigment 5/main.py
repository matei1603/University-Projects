import AirportUI
import AirportController
import Airport

airport = Airport()
ctrl = AirportController(airport)
ui = AirportUI(ctrl)

ui.start()