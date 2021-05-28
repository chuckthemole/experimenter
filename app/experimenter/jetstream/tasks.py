from celery.utils.log import get_task_logger

from experimenter.celery import app
from experimenter.jetstream import client as jetstream
from experimenter.experiments.models import NimbusExperiment

logger = get_task_logger(__name__)

@app.task
def fetch_jetstream_data():
  for experiment in NimbusExperiment.objects.all():
    experiment.results_data = jetstream.get_experiment_data(experiment)
    experiment.save()
