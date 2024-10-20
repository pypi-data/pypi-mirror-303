from masterpiece.core import MasterPiece, Application, Log
from juham.base.base import Base
from juham.base.jmqtt import JMqtt
from juham.database import JInflux
from juham.mqtt import JPaho2

from juham.ts import ForecastRecord
from juham.ts import PowerRecord
from juham.ts import PowerPlanRecord
from juham.ts import LogRecord
from juham.web import RSpotHintaFi

# from juham.web import RVisualCrossing

from juham.web import HomeWizardWaterMeter
from juham.shelly import ShellyPlus1
from juham.shelly import Shelly1G3
from juham.shelly import ShellyPro3EM
from juham.shelly import ShellyMotion
from juham.automation import RPowerPlan
from juham.automation import RBoiler
from juham.automation import WaterCirculator
from juham.automation import EnergyCostCalculator
from juham.base import JApp


class Kerttula(JApp):
    """Kerttula home automation application."""

    shelly_temperature = "shellyplus1-a0a3b3c309c4"  # temperature sensors
    shelly_boilerradiator = "shellyplus1-alakerta"  # hot water heating relay

    def __init__(self, name: str = "kerttula"):
        """Creates home automation application with the given name.
        If --enable_plugins is False create hard coded configuration
        by calling instantiate_classes() method.

        Args:
            name (str): name for the application
        """
        super().__init__(name)
        self.instantiate_classes()

    # @override
    def instantiate_classes(self):
        super().instantiate_classes()
        self.add(ForecastRecord())
        self.add(PowerRecord())
        self.add(PowerPlanRecord())
        self.add(LogRecord())
        self.add(RSpotHintaFi())
        self.add(HomeWizardWaterMeter())
        self.add(ShellyPlus1(self.shelly_temperature))  # for temperature sensors
        self.add(ShellyPlus1(self.shelly_boilerradiator))  # boiler heating radiator
        self.add(Shelly1G3())  # humidity
        self.add(ShellyPro3EM())
        self.add(ShellyMotion())
        self.add(RPowerPlan())
        self.add(RBoiler())
        self.add(WaterCirculator())
        self.add(EnergyCostCalculator())

        # pluginized
        self.instantiate_plugin_by_name("VisualCrossing")
        self.instantiate_plugin_by_name("OpenWeatherMap")
        self.print()

    @classmethod
    def register(cls):
        appname = "kerttula"
        MasterPiece.app_name(appname)
        MasterPiece.set_log(Log(appname))
        Application.register_plugin_group(appname)
        Application.load_class_attributes()


def main():

    # Support plugins
    Kerttula.load_plugins()

    # Parse startup arguments
    Kerttula.parse_args()

    # instantiate the application
    app = Kerttula()

    # app.serialize()

    # start the network loops
    app.run_forever()


if __name__ == "__main__":
    main()
