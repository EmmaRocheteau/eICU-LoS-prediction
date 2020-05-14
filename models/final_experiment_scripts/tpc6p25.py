from eICU_preprocessing.split_train_test import create_folder
from models.run_tpc import TPC
from models.initialise_arguments import initialise_tpc_arguments


if __name__=='__main__':

    c = initialise_tpc_arguments()
    c['mode'] = 'test'
    c['exp_name'] = 'TPC6.25'
    c['model_type'] = 'tpc'
    c['percentage_data'] = 6.25
    c['n_epochs'] = 8

    log_folder_path = create_folder('models/experiments/final', c.exp_name)

    for i in range(10):
        tpc = TPC(config=c,
                  n_epochs=c.n_epochs,
                  name=c.exp_name,
                  base_dir=log_folder_path,
                  explogger_kwargs={'folder_format': '%Y-%m-%d_%H%M%S{run_number}'})
        tpc.run()