from eICU_preprocessing.split_train_test import create_folder
from models.run_tpc import TPC
from models.initialise_arguments import initialise_tpc_arguments
from models.final_experiment_scripts.best_hyperparameters import best_tpc


if __name__=='__main__':

    c = initialise_tpc_arguments()
    c['exp_name'] = 'TempWeightShare'
    c['dataset'] = 'eICU'
    c['share_weights'] = True
    c = best_tpc(c)
    c['model_type'] = 'temp_only'

    log_folder_path = create_folder('models/experiments/final/eICU/LoS', c.exp_name)
    temp_weight_share = TPC(config=c,
                            n_epochs=c.n_epochs,
                            name=c.exp_name,
                            base_dir=log_folder_path,
                            explogger_kwargs={'folder_format': '%Y-%m-%d_%H%M%S{run_number}'})
    temp_weight_share.run()