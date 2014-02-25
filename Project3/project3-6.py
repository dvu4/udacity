import numpy as np
import pandas
import scipy
import statsmodels.api as sm

"""
In this optional exercise, you should complete the function called
predictions(turnstile_weather). This function takes in our pandas
turnstile weather dataframe, and returns a set of predicted ridership values,
based on the other information in the dataframe.

You should attempt to implement another type of linear regression,
that you may have read about, such as ordinary least squares regression:
http://en.wikipedia.org/wiki/Ordinary_least_squares

This is your playground. Go wild!

How does your choice of linear regression compare to linear regression
with gradient descent?

You can look at the information contained in the turnstile_weather dataframe below:
https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

Note: due to the memory and CPU limitation of our amazon EC2 instance, we will
give you a random subset (~15%) of the data contained in turnstile_data_master_with_weather.csv

If you receive a "server has encountered an error" message, that means you are hitting
the 30 second limit that's placed on running your program. See if you can optimize your code so it
runs faster.
"""

def predictions(weather_turnstile):
    #
    # Your implementation goes here. Feel free to write additional
    # helper functions
    #
    y = weather_turnstile['ENTRIESn_hourly']
    x = weather_turnstile[['EXITSn_hourly', 'Hour', 'maxpressurei','maxdewpti','mindewpti','minpressurei','meandewpti','meanpressurei','fog','rain','meanwindspdi','mintempi','meantempi', 'maxtempi', 'precipi', 'thunder']]
    #[['fog', 'rain', 'meandewpti', 'precipi', 'thunder', 'Hour']]
    #['maxpressurei','maxdewpti','mindewpti','minpressurei','meandewpti','meanpressurei','fog','rain','meanwindspdi','mintempi','meantempi', 'maxtempi', 'precipi', 'thunder']]#'thunder', 'mintempi']]#[['meanwindspdi', 'rain', 'mintempi']]#', 'fog']]#, 'meanwindspdi']]
    prediction = sm.OLS(y, x).fit()
    #print prediction.summary()
    #prediction = sm.OLS('ENTRIESn_hourly ~ rain + meanwindspdi', data = weather_turnstile).fit()
    return prediction.predict()


