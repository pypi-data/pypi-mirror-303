import os
import random
import argparse

import json
import torch
import numpy as np
import pandas as pd

from config import DL_MODELS, DL_MODELS_IMAGE_BASED, ML_MODELS, METRICS
from TabMap.code.tabmap_construction import TabMapGenerator
# from image_generators.IGTD_construction import table_to_image
# from image_generators.refined_construction import generate_refined
from pyDeepInsight import ImageTransformer
from sklearn.manifold import TSNE

from dataloader.dataset import load_data
from sklearn.model_selection import StratifiedKFold, train_test_split

from hparams_tuner.ml_models_tuner import MLModelTuner
from hparams_tuner.dl_models_tuner import DLModelTuner
# from hparams_tuner.dl_models_tuner import DLModelTuner
from evaluate_model import Model_Evaluation

def seed_everything(seed: int):
    """Seed all random number generators."""
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def main(args):
    seed_everything(args.seed)
    
    model_list = ['tabmap']
    # 'DI', 'IGTD', '1DCNN', 'tabnet', 'LR', 'RF', 'GB', 'XGB']
    
    # Define a range of noise levels to experiment with
    noise_levels = [0.0, 0.01, 0.1, 0.5, 1.0, 2.0]
    
    # Iterate through noise levels and perform sensitivity analysis
    for noise_level in noise_levels:
        # Define paths to load data, save checkpoints and predictions
        data_dir = os.path.join(args.data_path, args.data_set)
        features, labels, _ = load_data(data_dir, scaler_name='minmax',
                                        noise_level=noise_level, noipreprocessed=False)
        # Create directories for saving checkpoints and predictions if they don't exist
        os.makedirs(os.path.dirname(data_dir), exist_ok=True)
        # Create directories for saving checkpoints and predictions if they don't exist
        os.makedirs(os.path.dirname(data_dir), exist_ok=True)
        os.makedirs(f'{args.results_path}/{args.data_set}/results3/{args.data_set}_{noise_level}', exist_ok=True)
        
        if labels.ndim > 1:
            n_classes = labels.shape[1]
        else:
            n_classes = len(np.unique(labels))
        
        # Generate TabMaps for the input data
        images_dict = {}
        
        if 'tabmap' in model_list:
            # if not os.path.exists(file_path):
            generator = TabMapGenerator(metric=args.metric, 
                                    loss_fun=args.loss_fun, 
                                    epsilon=args.epsilon, 
                                    add_const=args.add_const,
                                    num_iter=args.num_iter)
            generator.fit(features, nd=args.nd, truncate=False, 
                        row_num=args.row_num, 
                        col_num=args.col_num)
            images_dict['tabmap'] = generator.transform(features)        
            np.save(os.path.join(data_dir, "tabmap.npy"), images_dict['tabmap'])
            print(f"Shape of tabmaps array: {images_dict['tabmap'].shape}")

        predictions_test_df = pd.DataFrame()
        performance_test_df = pd.DataFrame()
        best_hparams = []
        
        skf = StratifiedKFold(n_splits=args.cv_folds, shuffle=True, random_state=args.seed)
        for fold_id, (train_idx, test_idx) in enumerate(skf.split(features, labels)):
            
            # Stratified Sampling for train and val
            train_idx, valid_idx = train_test_split(train_idx,
                                            test_size=0.125,
                                            random_state=args.seed,
                                            # shuffle=True,
                                            stratify=labels[train_idx])
            
            print('\n\nFold_ID', fold_id)
            for model_id in model_list:
                print(f'\nTraining {model_id}')
                
                best_parameters_path = f"{args.results_path}/{args.data_set}/results2/{args.data_set}_{noise_level}/model_best_params.json"
                data_config = {
                    "data_set": args.data_set,
                    "data_dir": data_dir,
                    "n_classes": n_classes,
                    "input_size": images_dict[model_id].shape[1:] \
                        if model_id in DL_MODELS_IMAGE_BASED else features.shape[1],
                    "fold_id": fold_id,
                }
                
                if model_id in DL_MODELS:
                    tuner = DLModelTuner(data_config, train_idx, valid_idx, model_id, 
                                        args.results_path, 
                                        use_default_hparams=args.use_default_hparams,
                                        random_seed=args.seed)
                elif model_id in ML_MODELS:
                    tuner = MLModelTuner(data_config, train_idx, valid_idx, model_id, 
                                        args.results_path, 
                                        use_default_hparams=args.use_default_hparams,
                                        random_seed=args.seed)
                
                best_params_dict = tuner.params_dict
                best_params_dict['fold'] = fold_id
                best_hparams.append(best_params_dict)

                # Model evaluation on the best trained model
                model_eval = Model_Evaluation(model_id)
                # Save the predictions
                if model_id in DL_MODELS_IMAGE_BASED:
                    y_pred = model_eval.model_predict(tuner.final_model, features=images_dict[model_id][test_idx], multilabel=False)
                else:
                    y_pred = model_eval.model_predict(tuner.final_model, features=features[test_idx], multilabel=False)
                
                predictions_test = pd.DataFrame({"model": model_id, "fold": fold_id, "true": labels[test_idx].ravel(), "pred": y_pred.ravel()})
                predictions_test_df = pd.concat([predictions_test_df, predictions_test], ignore_index=True)
                
                # save the performance
                print('Saving the prediction results...')
                performance_test = model_eval.prediction_performance(labels[test_idx].ravel(), y_pred.ravel())
                performance_test = pd.DataFrame([performance_test])
                performance_test["fold"] = fold_id
                performance_test_df = pd.concat([performance_test_df, performance_test])

            print(f'Fold_id: {fold_id}\n', performance_test_df)
        
        predictions_test_df.set_index(["model", "fold"]).to_csv(f"{args.results_path}/{args.data_set}/results2/{args.data_set}_{noise_level}/model_preds.csv", sep='\t')
        performance_test_df.set_index(["model", "fold"]).to_csv(f"{args.results_path}/{args.data_set}/results2/{args.data_set}_{noise_level}/model_performance.csv", sep='\t')
        mean_performance_test_df = performance_test_df.groupby(["model"])[METRICS].agg(["mean", "std"]).reset_index()
        for metric in METRICS:
            mean_performance_test_df[(metric, "mean")] = mean_performance_test_df[(metric, "mean")].round(4)
            mean_performance_test_df[(metric, "std")] = mean_performance_test_df[(metric, "std")].round(4)
        mean_performance_test_df.to_csv(f"{args.results_path}/{args.data_set}/results2/{args.data_set}_{noise_level}/mean_model_performance.csv", sep='\t')
        print(mean_performance_test_df)
        # parameter_df = pd.DataFrame(best_hparams)
        # parameter_df.to_csv(f"{args.results_path}/{args.data_set}/model_best_params.csv", sep='\t', index=False)
        with open(best_parameters_path, "w") as json_file:
            json.dump(best_hparams, json_file, indent=4)


# Construct argument parser
def get_args():
    parser = argparse.ArgumentParser(description='Script for training a TabMap classifier',
                                     add_help=False)
    parser.add_argument('--seed', default=2, type=int)
    
    # Dataset parameters
    parser.add_argument('--data_path', default='/data/yan/pyTabMap/data', type=str,
                        help='path to dataset')
    parser.add_argument('--results_path', default='/data/yan/pyTabMap/results/ablation/sensitivity', type=str,
                        help='path to save results')
    parser.add_argument('--data_set', default='parkinson',
                        type=str, help='dataset name')
    parser.add_argument('--scaler_name', default='minmax', 
                        choices=['zscore', 'minmax', 'maxabs', 'robust', 'norm', 'quantile', 'power'],
                        type=str, help='scaler name')
    parser.add_argument('--device', default='cuda', choices=['cuda', 'cpu'],
                    help='device to use for training / testing (default: cuda)')
    
    # TabMap construction parameters
    parser.add_argument('--metric', type=str, default='correlation', choices=['euclidean', 'correlation', 'gower'],
                        help='distance metric for calculating feature association')
    parser.add_argument('--loss_fun', type=str, default='kl_loss', choices=['kl_loss', 'square_loss'],
                        help='loss function for tabmap construction')
    parser.add_argument('--epsilon', type=float, default=0.0,
                        help='regularization term for tabmap construction, need to > 0')
    parser.add_argument('--nd', action="store_true", default=False,
                        help='whether to perform deconvolution on interaction matrix')
    parser.add_argument('--add_const', action="store_true", default=True,
                        help='whether to add constant when calculating loss in OT')
    parser.add_argument('--row_num', type=int, default=None,
                        help='number of rows of tabmap')
    parser.add_argument('--col_num', type=int, default=None,
                        help='number of cols of tabmap')
    parser.add_argument('--num_iter', type=int, default=200,
                        help='number of iterations for learning coupling matrix')
    
    # Hypertuning paramters
    parser.add_argument('--use_default_hparams', action="store_true", default=True,
                    help='whether to use default hparams or tune the hparams')
    
    # Evaluation parameters
    parser.add_argument('--cv_folds', type=int, default=5,
                    help='number of data folds for cross-validation (default: 5)')

    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    main(args)