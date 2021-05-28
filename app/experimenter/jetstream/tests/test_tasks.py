from django.test import TestCase

from experimenter.jetstream import client as jetstream
from experimenter.jetstream import tasks
from experimenter.experiments.models import NimbusExperiment
from experimenter.experiments.tests.factories import NimbusExperimentFactory

class TestFetchJetstreamDataTask(TestCase):
  def setUp(self):
    super().setUp()

    self.experiment = NimbusExperimentFactory.create_with_lifecycle(
      NimbusExperiment.Lifecycles.CREATED
    )


  def test_results_data_not_null(self):
    self.assertEqual(self.experiment.results_data, None)