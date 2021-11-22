

<div align="center" style="text-align:center; margin-top:1rem; margin-bottom: 1rem;">
  <img style="max-width:420px" width="420px" alt="" src="https://firebasestorage.googleapis.com/v0/b/cannlytics.appspot.com/o/public%2Fimages%2Flogos%2Fcannlytics_ai_with_text.png?alt=media&token=78d19117-eff5-4f45-a8fa-3bbdabd6917d">
  <div style="margin-top:1rem; margin-bottom:1rem;">
    <h3>Simple, easy, cannabis analytics.</h3>
  </div>

[![License: MIT](https://img.shields.io/badge/License-MIT-darkgreen.svg)](https://opensource.org/licenses/MIT)
[![Coverage Status](https://coveralls.io/repos/github/cannlytics/cannlytics-ai/badge.svg?branch=main)](https://coveralls.io/github/cannlytics/cannlytics-ai?branch=main)

<https://cannlytics.com>

</div>

Cannlytics AI is 🔥 Cannlytics-powered artificial intelligence 🤖. Cannlytics strives to be the go-to source of public cannabis data. Cannlytics wishes to use our comparative advantage in aggregating data from disparate resources and provide you with a simple, standardized interface to consume the data.

- [🌱 Installation](#installation)
- [🏃‍♀️ Quickstart](#quickstart)
- [🔨 Development](#development)
- [🦾 Automation](#automation)
- [👩‍🔬 Testing](#testing)
- [❤️ Support](#support)
- [🏛️ License](#license)

## 🌱 Installation <a name="installation"></a>

You can simply clone the repository to get your hands on the AI source code.

```shell
git clone https://github.com/cannlytics/cannlytics-ai.git
```

## 🏃‍♀️ Quickstart <a name="quickstart"></a>

You can run each data collection routine through the command line. For example:

```shell
python ai/get_cannabis_data/get_data_ma.py
```

## 🔨 Development <a name="development"></a>

Please see the [data collection guides](guides/data/data-collection.md) for information on how public data is collected.

## 🦾 Automation <a name="automation"></a>

Now for the fun part, automation.

> Note that you will need to [enable billing for your project](http://console.cloud.google.com/billing/?_ga=2.91797530.1059044588.1636848277-147951098.1631325967), [enable the Cloud Scheduler API](http://console.cloud.google.com/apis/library/cloudscheduler.googleapis.com?_ga=2.121230088.1059044588.1636848277-147951098.1631325967), and [enable the Pub/Sub API](http://console.cloud.google.com/apis/library/pubsub.googleapis.com?_ga=2.121230088.1059044588.1636848277-147951098.1631325967).

1. Create a Pub/Sub topic:

    ```
    gcloud pubsub topics create get_cannabis_data_daily
    ```

2. Deploy the function:

    ```
    gcloud functions deploy get_cannabis_data_daily --entry-point get_cannabis_data_daily --runtime python39 --trigger-topic get_cannabis_data_daily --memory 1024MB --timeout 300 --env-vars-file env.yaml
    ```

3. Finally, create a [Cloud Scheduler](https://cloud.google.com/scheduler/docs/creating#gcloud) cron job:

    ```
    gcloud scheduler jobs create pubsub get_cannabis_data_daily --schedule "20 4 * * *" --topic get_cannabis_data_daily --message-body "success"
    ```

Your function should now run nicely everyday at 4:20am EDT. You can read the logs for your function with:

```
gcloud functions logs read get_cannabis_data_daily
```

## 👩‍🔬 Testing <a name="testing"></a>

You can run tests with code coverage with `pytest`.

```
pytest --cov=ai tests/
```

## ❤️ Support <a name="support"></a>

Cannlytics is made available with ❤️ and <a href="https://opencollective.com/cannlytics-company">your good will</a>. Please consider making a contribution to keep the good work coming 🚢

🥞 Bitcoin donation address: 34CoUcAFprRnLnDTHt6FKMjZyvKvQHb6c6

## 🏛️ License <a name="license"></a>

```
Copyright (c) 2021 Cannlytics and Cannlytics Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
