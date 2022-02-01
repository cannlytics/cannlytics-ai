# Get Cannabis Data Massachusetts

This routine periodically gets cannabis data published by the Massachusetts Cannabis Commission.

## Setup

You will need to create an `env.yaml` file with the following environment variable.

```yaml
FRED_API_KEY: your-api-key
```

## Development

The function can be run locally for testing and development.

```bash
python ai/get_cannabis_data/main.py
```

## Deployment

Cloud Functions are used as a mechanism to run the routine on a schedule in the cloud. You will need to [enable billing for your project](http://console.cloud.google.com/billing/), [enable the Cloud Scheduler API](http://console.cloud.google.com/apis/library/cloudscheduler.googleapis.com), and [enable the Pub/Sub API](http://console.cloud.google.com/apis/library/pubsub.googleapis.com) to allow all functionality.

```shell
gcloud services enable cloudfunctions.googleapis.com cloudscheduler.googleapis.com pubsub.googleapis.com --project=<your-project-id>
```

1. Create a Pub/Sub topic:

    ```
    gcloud pubsub topics create get_cannabis_data_ma
    ```

2. Deploy the function:

    ```
    gcloud functions deploy get_cannabis_data_ma --entry-point get_cannabis_data_ma --runtime python39 --trigger-topic get_cannabis_data_ma --memory 1024MB --timeout 300 --env-vars-file env.yaml
    ```

3. Finally, create a [Cloud Scheduler](https://cloud.google.com/scheduler/docs/creating#gcloud) cron job:

    ```
    gcloud scheduler jobs create pubsub get_cannabis_data_ma --schedule "20 4 * * *" --topic get_cannabis_data_ma --message-body "success"
    ```

Your function should now run nicely everyday at 4:20am EDT.

> You can substitute `create` in step 3 with `update` to update your scheduled job.

> Note: If you encounter a `PERMISSION_DENIED` error, then make sure that [the service account being used has sufficient permissions](https://stackoverflow.com/a/58646481/5021266).

## Logs

You can read the logs for your function with:

```
gcloud functions logs read get_cannabis_data_ma
```
