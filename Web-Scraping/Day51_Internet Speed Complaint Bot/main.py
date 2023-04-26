from user import CHROME_DRIVER_PATH
from InternetSpeedTwitterBot import InternetSpeedTwitterBot

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()