from datetime import datetime, timedelta, timezone
import json

from typing import Any
from juham.base import Base
from juham.web import RCloud, RCloudThread


class VisualCrossingThread(RCloudThread):
    """Asynchronous thread for acquiring forecast from the VisualCrossing
    site."""

    # class attributes
    _forecast_topic = ""
    _base_url = ""
    _api_key = ""
    _location = ""
    _interval: float = 12 * 3600

    def __init__(self, client=None):
        """Construct with the given mqtt client. Acquires data from the visual
        crossing web service and publishes the forecast data to
        forecast_topic.

        Args:
            client (object, optional): MQTT client. Defaults to None.
        """
        super().__init__(client)
        self.mqtt_client = client

    def update_interval(self) -> float:
        return self._interval

    # @override
    def make_url(self) -> str:
        if not self._api_key:
            self.error("Uninitialized api_key {self.get_class_id()}: {self._api_key}")
            return ""
        else:
            now = datetime.now()
            end = now + timedelta(days=1)
            start = now.strftime("%Y-%m-%d")
            stop = end.strftime("%Y-%m-%d")
            url = f"{self._base_url}{self._location}/{start}/{stop}?unitGroup=metric&contentType=json&include=hours&key={self._api_key}"
            self.debug(url)
            return url

    def init(
        self, topic: str, base_url: str, interval: float, api_key: str, location: str
    ) -> None:
        """Initialize the  data acquisition thread

        Args:
            topic (str): mqtt topic to publish the acquired data
            base_url (str): url of the web service
            interval (float): update interval in seconds
            api_key (str): api_key, as required by the web service
            location (str): geographic location
        """
        self._forecast_topic = topic
        self._base_url = base_url
        self._interval = interval
        self._api_key = api_key
        self._location = location

    # @override
    def process_data(self, data: Any):
        self.info("VisualCrossing process_data()")
        data = data.json()
        forecast = []
        self.info(f"VisualCrossing {data}")
        for day in data["days"]:
            for hour in day["hours"]:
                ts = int(hour["datetimeEpoch"])
                forecast.append(
                    {
                        "id": "visualcrossing",
                        "ts": ts,
                        "hour": datetime.fromtimestamp(ts, tz=timezone.utc).strftime(
                            "%H"
                        ),
                        "day": datetime.fromtimestamp(ts, tz=timezone.utc).strftime(
                            "%Y%m%d%H"
                        ),
                        "uvindex": hour["uvindex"],
                        "solarradiation": hour["solarradiation"],
                        "solarenergy": hour["solarenergy"],
                        "cloudcover": hour["cloudcover"],
                        "snow": hour["snow"],
                        "snowdepth": hour["snowdepth"],
                        "pressure": hour["pressure"],
                        "temp": hour["temp"],
                        "humidity": hour["humidity"],
                        "windspeed": hour["windspeed"],
                        "winddir": hour["winddir"],
                        "dew": hour["dew"],
                    }
                )
        msg = json.dumps(forecast)
        self.publish(self._forecast_topic, msg, qos=1, retain=False)
        self.info(f"VisualCrossing forecast published to {self._forecast_topic}")


class VisualCrossing(RCloud):
    """Constructs a data acquisition object for reading weather
    forecasts from the VisualCrossing web service. Subscribes to the
    forecast topic and writes hourly data such as solar energy, temperature,
    and other attributes relevant to home automation into a time series
    database.

    Spawns an asynchronous thread to run queries at the specified
    update_interval.
    """

    workerThreadId = VisualCrossingThread.get_class_id()
    forecast_topic = Base.mqtt_root_topic + "/forecast"
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    update_interval = 12 * 3600
    api_key = "SE9W7EHP775N7NDNW8ANM2MZN"
    location = "lahti,finland"

    def __init__(self, name="visualcrossing"):
        super().__init__(name)
        self.debug(f"VisualCrossing created")

    def on_connect(self, client, userdata, flags, rc):
        super().on_connect(client, userdata, flags, rc)
        if rc == 0:
            self.subscribe(self.forecast_topic)
            self.debug(f"VisualCrossing subscribed to topic {self.forecast_topic}")

    def on_message(self, client, userdata, msg):
        if msg.topic == self.forecast_topic:
            em = json.loads(msg.payload.decode())
            self.on_forecast(em)
        else:
            super().on_message(client, userdata, msg)

    def on_forecast(self, em: dict) -> None:
        """Handle weather forecast data.

        Args:
            em (dict): forecast
        """
        self.debug(f"VisualCrossing: got mqtt message {em}")

    # @override
    def run(self):
        # create, initialize and start the asynchronous thread for acquiring forecast
        self.worker = Base.instantiate(VisualCrossing.workerThreadId)
        self.worker.init(
            self.forecast_topic,
            self.base_url,
            self.update_interval,
            self.api_key,
            self.location,
        )
        self.debug(f"VisualCrossing.run(): base_url is {self.base_url}")
        self.debug(f"VisualCrossing.run(): interval is {self.update_interval}")
        self.debug(f"VisualCrossing.run(): api_key is {self.api_key}")
        self.debug(f"VisualCrossing.run(): location is {self.location}")
        super().run()

    # @override
    def to_dict(self):
        data = super().to_dict()
        data["_visualcrossing"] = {
            "topic": self.forecast_topic,
            "url": self.base_url,
            "api_key": self.api_key,
            "interval": self.update_interval,
        }
        return data

    # @override
    def from_dict(self, data):
        super().from_dict(data)
        if "_visualcrossing" in data:
            for key, value in data["_visualcrossing"].items():
                setattr(self, key, value)
