all:
	run

create_project:

	gcloud projects create [PROJECT_ID]

	gcloud config set project [PROJECT-ID]

	gcloud app create [--region=REGION]

install:

	gcloud pubsub topics create cron-topic

	gcloud scheduler jobs create pubsub get_cannabis_data --schedule="20 4 * * *" --topic=get_cannabis_data --message-body="success"

publish:

	gcloud functions deploy get_cannabis_data --source ai/get_cannabis_data --entry-point get_cannabis_data --runtime python39 --trigger-topic get_cannabis_data --env-vars-file ai/get_cannabis_data/env.yaml
