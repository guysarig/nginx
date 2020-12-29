from monitoring import HealthTests
from common import MyLogger

logger = MyLogger()
test_health = HealthTests(logger=logger)


test_health.web_connectivity(url="http://localhost")

docker pull alpine/helm
