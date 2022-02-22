# daily-notify

Script to post daily notification to telegram.

Currenly handles:

- weather (lat, lon can be changed in config.py)
- exchange rate for Belarus

Can be easily deployed to AWS Lambda using serverless.

Example output message:

```
{
Today is 22-02-2022.

Clouds.
Temperature is 1.92 °C, but feels like -4.07 °C.
Humidity is 79 % and wind 8.68 m/s.
Daylight hours from 2022-02-22 08:14:56 to 2022-02-22 18:31:58 for 10.3 hours.

EUR: 2.9397 ↑0.66%
USD: 2.587 ↑0.75%
RUB: 3.3681 ↓0.65%
}
```
