import unittest

from pyspark.sql import SparkSession
from pyspark.testing import assertDataFrameEqual
from example_job import etl


class PysparkTestCase(unittest.TestCase):
    spark: SparkSession

    @classmethod
    def setUpClass(cls) -> None:
        cls.spark = SparkSession.builder.appName("Tests").getOrCreate()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.spark.stop()


class ExampleJobTest(PysparkTestCase):
    def test_job(self):
        sample_data = [
            {"name": "John", "age": 35},
            {"name": "Alice", "age": 25},
        ]

        df = ExampleJobTest.spark.createDataFrame(sample_data)
        actual_df = etl(df)

        expected_data = [
            {"name": "John"},
        ]

        expected_df = ExampleJobTest.spark.createDataFrame(expected_data)

        assertDataFrameEqual(actual_df, expected_df)