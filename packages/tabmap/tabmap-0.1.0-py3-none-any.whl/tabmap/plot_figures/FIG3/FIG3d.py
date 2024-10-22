# %%
import os
import time

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit

import sys
sys.path.append('/home/yan/pyTabMap/code')
from config import DL_MODELS, DL_MODELS_IMAGE_BASED, ML_MODELS, METRICS
from TabMap.code.dataloader.dataset import load_data
from TabMap.code.tabmap_construction import TabMapGenerator
from image_generators.IGTD_construction import generate_igtd_mapping, IGTD_Im_Gen
from image_generators.refined_construction import generate_refined_mapping, REFINED_Im_Gen
from pyDeepInsight import ImageTransformer
from sklearn.manifold import TSNE

from hparams_tuner.ml_models_tuner import MLModelTuner
from hparams_tuner.dl_models_tuner_gridsearchcv import DLModelTuner
from evaluate_model import Model_Evaluation

# %%
seed = 0

def seed_everything(seed: int):
    """Seed all random number generators."""
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)

seed_everything(seed)

# %% [markdown]
# ### Data simulation

# %%
def generate_synthetic_data(n_samples, n_features, n_classes=2):
    random_seed = 0
    # Create synthetic classification datasets
    features, labels = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_informative=n_features,#int(0.8 * n_features),
        n_redundant=0,#n_features - int(0.8 * n_features),
        n_classes=n_classes,
        random_state=random_seed
    )
    return features, labels

# %%
# binary classification
n_samples_list = [200, 500, 1000, 2000, 5000]
n_features_list = [100, 200, 500, 1000, 2000]
for n_samples in n_samples_list:
    for n_features in n_features_list:
        features, labels = generate_synthetic_data(n_samples, n_features, n_classes=5)
        # Create df for simulated data
        data = np.concatenate([features, labels.reshape(-1, 1)], axis=1)
        feature_columns = [f'feature_{i}' for i in range(features.shape[1])]
        columns = feature_columns + ['label']
        df = pd.DataFrame(data, columns=columns)
        
        save_to_dir = f'/home/yan/pyTabMap/code/plot_figures/FIG3/3d/simulated_data_5_classes/ns_{n_samples}_nf_{n_features}/data_raw.csv'
        os.makedirs(os.path.dirname(save_to_dir), exist_ok=True)
        df.to_csv(save_to_dir, index=False) 

# %%
# %%
def generate_images(model_id, features, 
                    train_idx, test_idx,
                    feature_names=None, save_path=None, save_images=True):
    print(f"Generating images for {model_id}")
    if model_id == 'tabmap':
        generator = TabMapGenerator(metric='correlation', 
                                    loss_fun='kl_loss', 
                                    epsilon=0.0, 
                                    version=2,
                                    add_const=True,
                                    num_iter=200)
        generator.fit(features[train_idx])
        X_train_img = generator.transform(features[train_idx])
        X_test_img = generator.transform(features[test_idx])
    
    if model_id == 'tabmap_sq':
        generator = TabMapGenerator(metric ='correlation', 
                                    loss_fun='sqeuclidean', 
                                    epsilon=0.0, 
                                    version=2,
                                    add_const=True,
                                    num_iter=200)
        generator.fit(features[train_idx])
        X_train_img = generator.transform(features[train_idx])
        X_test_img = generator.transform(features[test_idx])
    
    if model_id == 'DI':
        reducer = TSNE(n_components=2, metric='cosine', perplexity=5, random_state=seed)
        it = ImageTransformer(feature_extractor=reducer, pixels=(50, 50))
        it.fit(features[train_idx])
        X_train_img = it.transform(features[train_idx], img_format='scalar')
        X_test_img = it.transform(features[test_idx], img_format='scalar')
    
    if model_id == 'REFINED':
        row_num, map_in_int, feature_names, coords = generate_refined_mapping(features[train_idx], feature_names)
        X_train_img = REFINED_Im_Gen(features[train_idx], row_num, map_in_int, feature_names, coords)
        X_test_img = REFINED_Im_Gen(features[test_idx], row_num, map_in_int, feature_names, coords)

    if model_id == 'IGTD':
        index, row_num, col_num, coordinate = generate_igtd_mapping(features[train_idx], 
                                    fea_dist_method='Pearson',
                                    image_dist_method='Euclidean',
                                    max_step=10000, val_step=300, 
                                    error='abs', seed=seed
                                    )
        X_train_img, _ = IGTD_Im_Gen(data=features[train_idx], 
                                     index=index, num_row=row_num, num_column=col_num,
                                     coord=coordinate)
        X_test_img, _ = IGTD_Im_Gen(data=features[test_idx], 
                                     index=index, num_row=row_num, num_column=col_num,
                                     coord=coordinate)
    
    images = np.empty((len(features), X_train_img.shape[1], X_train_img.shape[2]))  # Initialize tabmap array
    images[train_idx] = X_train_img
    images[test_idx] = X_test_img
    
    print(f'Shape of {model_id} images: ', images.shape)
    if save_images:
        np.save(save_path, images)
    return images

# %%
# run models for classification
# n_samples_list = [200]
# n_features_list = [1000, 2000]
# n_samples_list = [200, 500, 1000, 2000, 5000]
# n_features_list = [100, 200, 500, 1000, 2000]

for n_samples in n_samples_list:
    for n_features in n_features_list:
        
        data_path='/home/yan/pyTabMap/code/plot_figures/FIG3/3d/simulated_data_5_classes'
        data_set=f'ns_{n_samples}_nf_{n_features}'
        results_path = '/home/yan/pyTabMap/code/plot_figures/FIG3/3d/simulated_data_5_classes'

        data_dir = os.path.join(data_path, data_set)
        os.makedirs(os.path.dirname(data_dir), exist_ok=True)

        # df = pd.read_csv(f'/home/yan/pyTabMap/code/plot_figures/FIG3/3d/simulated_data/ns_{n_samples}_nf_{n_features}.csv')
        features, labels, feature_names = load_data(data_dir, scaler_name='minmax', preprocessed=False)
        if labels.ndim > 1:
            n_classes = labels.shape[1]
        else:
            n_classes = len(np.unique(labels))
        
        predictions_test_df = pd.DataFrame()
        performance_test_df = pd.DataFrame()
        best_hparams = []
        seed = 0

        skf = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=seed)
        for fold_id, (train_idx_all, test_idx) in enumerate(skf.split(features, labels)):
            
            # Stratified Sampling for train and val
            train_idx, valid_idx = train_test_split(train_idx_all,
                                            test_size=0.125,
                                            random_state=seed,
                                            stratify=labels[train_idx_all])

            print('\nFold_ID', fold_id)
            
            images_dict = {}
            runtime_dict = {}
            for model_id in ['tabmap', 'LR', 'RF', 'GB', 'XGB']:
                print(f'\nTraining {model_id}')
                
                if model_id in DL_MODELS_IMAGE_BASED:
                    images_save_path = os.path.join(data_dir, f"{model_id}.npy")
                    
                    print('start generating images')
                    images = generate_images(model_id, features, 
                                                    train_idx_all, test_idx,
                                                    feature_names, save_path=images_save_path)
                    images_dict[model_id] = images
                    print('finished generating images')

                data_config = {
                    "data_set": data_set,
                    "data_dir": data_dir,
                    "n_classes": n_classes,
                    "input_size": images_dict[model_id].shape[1:] \
                        if model_id in DL_MODELS_IMAGE_BASED else features.shape[1],
                    "fold_id": fold_id,
                }
                
                if model_id in DL_MODELS:
                    tuner = DLModelTuner(data_config, train_idx, valid_idx, model_id, 
                                        results_path,
                                        use_default_hparams=True,
                                        random_seed=seed)
                elif model_id in ML_MODELS:
                    tuner = MLModelTuner(data_config, train_idx, valid_idx, model_id, 
                                        results_path,
                                        use_default_hparams=True,
                                        random_seed=seed)
                
                best_params_dict = tuner.params_dict
                best_params_dict['fold'] = fold_id
                best_hparams.append(best_params_dict)
                        
                # Model evaluation on the best trained model
                model_eval = Model_Evaluation(model_id)
                # Save the predictions
                if model_id in DL_MODELS_IMAGE_BASED:
                    y_prob, y_pred = model_eval.model_predict(tuner.final_model, features=images_dict[model_id][test_idx], multilabel=False)
                else:
                    y_prob, y_pred = model_eval.model_predict(tuner.final_model, features=features[test_idx], multilabel=False)

                predictions_test = pd.DataFrame({"model": model_id, "fold": fold_id, "true": labels[test_idx].ravel(), "pred": y_pred.ravel()})
                for i in range(n_classes):
                    predictions_test[f'prob_class_{i}'] = y_prob[:, i]
                predictions_test_df = pd.concat([predictions_test_df, predictions_test], ignore_index=True)
                
                # save the performance
                print('Saving the prediction results...')
                performance_test = model_eval.prediction_performance(labels[test_idx].ravel(), y_pred.ravel())
                performance_test = pd.DataFrame([performance_test])
                performance_test["fold"] = fold_id
                performance_test_df = pd.concat([performance_test_df, performance_test])
    
        predictions_test_df.set_index(["model", "fold"]).to_csv(f"{results_path}/{data_set}/model_preds.csv", sep='\t')
        performance_test_df.set_index(["model", "fold"]).to_csv(f"{results_path}/{data_set}/model_performance.csv", sep='\t')
        mean_performance_test_df = performance_test_df.groupby(["model"])[METRICS].agg(["mean", "std"]).reset_index()
        for metric in METRICS:
            mean_performance_test_df[(metric, "mean")] = mean_performance_test_df[(metric, "mean")].round(4)
            mean_performance_test_df[(metric, "std")] = mean_performance_test_df[(metric, "std")].round(4)
        mean_performance_test_df.to_csv(f"{results_path}/{data_set}/mean_model_performance.csv", sep='\t')
        print(mean_performance_test_df)
        


