# pyre-strict

# TODO This needs to be rewritten to match the new structure of the codebase
# TODO Add separate methods if state is loaded from robyn_object or json_file for each method

import logging
import pandas as pd

from robyn.modeling.entities.enums import Models, NevergradAlgorithm
from robyn.modeling.entities.modelrun_trials_config import TrialsConfig
from robyn.modeling.feature_engineering import FeatureEngineering
from robyn.modeling.model_executor import ModelExecutor
from robyn.data.entities.calibration_input import CalibrationInput
from robyn.data.entities.holidays_data import HolidaysData
from robyn.data.entities.hyperparameters import Hyperparameters
from robyn.data.entities.mmmdata import MMMData
from robyn.data.validation.calibration_input_validation import (
    CalibrationInputValidation,
)
from robyn.data.validation.holidays_data_validation import HolidaysDataValidation
from robyn.data.validation.hyperparameter_validation import HyperparametersValidation
from robyn.data.validation.mmmdata_validation import MMMDataValidation
from robyn.visualization.feature_visualization import FeaturePlotter
import matplotlib.pyplot as plt


class Robyn:


    
    def __init__(self, working_dir: str):
        """
        Initializes the Robyn object with a working directory.

        Args:
            working_dir (str): The path to the working directory.
        """
        self.working_dir = working_dir
        self.logger = logging.getLogger()
        self.logger.info("Robyn initialized with working directory: %s", working_dir)
        self.mmm_data: MMMData = None,
        self.holidays_data: HolidaysData = None,
        self.hyperparameters: Hyperparameters = None,
        self.calibration_input: CalibrationInput = None

    # Load input data for the first time and validates
    def initialize(
        self,
        mmm_data: MMMData,
        holidays_data: HolidaysData,
        hyperparameters: Hyperparameters,
        calibration_input: CalibrationInput,
    ) -> None:
        """
        Loads input data for the first time and validates it.
        Calls validate from MMMDataValidation, HolidaysDataValidation, HyperparametersValidation, and CalibrationInputValidation.

        Args:
            mmm_data (MMMData): The MMM data object.
            holidays_data (HolidaysData): The holidays data object.
            hyperparameters (HyperParametersConfig): The hyperparameters configuration object.
            calibration_input (CalibrationInputConfig): The calibration input configuration object.
        """

        mmm_data_validation = MMMDataValidation(mmm_data)
        holidays_data_validation = HolidaysDataValidation(holidays_data)
        hyperparameters_validation = HyperparametersValidation(hyperparameters)
        calibration_input_validation = CalibrationInputValidation(
            mmm_data, calibration_input, pd.Timestamp("2016-01-01"), pd.Timestamp("2018-12-31")
        )

        mmm_data_validation.validate()
        holidays_data_validation.validate()
        hyperparameters_validation.validate()
        calibration_input_validation.validate()

        self.mmm_data = mmm_data
        self.holidays_data = holidays_data
        self.hyperparameters = hyperparameters
        self.calibration_input = calibration_input

        print("Validation complete")

    def model_run(
        self,
        feature_plots: bool = False,
        trials_config: TrialsConfig = None,
    ) -> None:
        """ """
        feature_engineering = FeatureEngineering(
            self.mmm_data, self.hyperparameters, self.holidays_data
        )
        featurized_mmm_data = feature_engineering.perform_feature_engineering()

        if feature_plots:
            # Create a FeaturePlotter instance
            feature_plotter = FeaturePlotter(self.mmm_data, self.hyperparameters)

            # Plot spend-exposure relationship for each channel
            for channel in self.mmm_data.mmmdata_spec.paid_media_spends:
                try:
                    fig = feature_plotter.plot_spend_exposure(featurized_mmm_data, channel)
                    plt.show()
                except ValueError as e:
                    print(f"Skipping {channel}: {str(e)}")


        # Setup ModelExecutor
        model_executor = ModelExecutor(
            mmmdata=self.mmm_data,
            holidays_data=self.holidays_data,
            hyperparameters=self.hyperparameters,
            calibration_input=None,  # Add calibration input if available
            featurized_mmm_data=featurized_mmm_data,
        )

        # Setup TrialsConfig
        trials_config = TrialsConfig(iterations=2000, trials=5)  # Set to the number of cores you want to use

        print(
            f">>> Starting {trials_config.trials} trials with {trials_config.iterations} iterations each using {NevergradAlgorithm.TWO_POINTS_DE.value} nevergrad algorithm on x cores..."
        )

        # Run the model

        model_outputs = model_executor.model_run(
            trials_config=trials_config,
            ts_validation=False,  # changed from True to False -> deacitvate
            add_penalty_factor=False,
            rssd_zero_penalty=True,
            cores=8,
            nevergrad_algo=NevergradAlgorithm.TWO_POINTS_DE,
            intercept=True,
            intercept_sign="non_negative",
            model_name=Models.RIDGE,
        )
        print("Model training complete.")
