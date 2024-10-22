# %%
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # Set to the index of the GPU you want to use (e.g., 0, 1, 2, ...)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import torch

import sys
sys.path.append('/home/yan/pyTabMap/code/')
from dataloader.dataset import load_data
sys.path.insert(0,'/home/yan/pyTabMap/code/image_generators')
from tabmap_construction import TabMapGenerator

# %%
data_path='/home/yan/pyTabMap/data'
data_set='METABRIC'
results_path = '/home/yan/pyTabMap/results/BCTIL_revision/test'

# %%
data_dir = os.path.join(data_path, data_set)
os.makedirs(os.path.dirname(data_dir), exist_ok=True)

# Load the dataset into a pandas dataframe
features, labels, feature_names = load_data(data_dir, scaler_name='minmax', preprocessed=False)
if labels.ndim > 1:
    n_classes = labels.shape[1]
else:
    n_classes = len(np.unique(labels))

# def select_features_by_variation(data, variation_measure='var', threshold=None, num=None, draw_histogram=False,
#                                  bins=100, log=False):
#     '''
#     This function evaluates the variations of individual features and returns the indices of features with large
#     variations. Missing values are ignored in evaluating variation.

#     Parameters:
#     -----------
#     data: numpy array or pandas data frame of numeric values, with a shape of [n_samples, n_features].
#     variation_metric: string indicating the metric used for evaluating feature variation. 'var' indicates variance;
#         'std' indicates standard deviation; 'mad' indicates median absolute deviation. Default is 'var'.
#     threshold: float. Features with a variation larger than threshold will be selected. Default is None.
#     num: positive integer. It is the number of features to be selected based on variation.
#         The number of selected features will be the smaller of num and the total number of
#         features with non-missing variations. Default is None. threshold and portion can not take values
#         and be used simultaneously.
#     draw_histogram: boolean, whether to draw a histogram of feature variations. Default is False.
#     bins: positive integer, the number of bins in the histogram. Default is the smaller of 50 and the number of
#         features with non-missing variations.
#     log: boolean, indicating whether the histogram should be drawn on log scale.


#     Returns:
#     --------
#     indices: 1-D numpy array containing the indices of selected features. If both threshold and
#         portion are None, indices will be an empty array.
#     '''

#     if isinstance(data, pd.DataFrame):
#         data = data.values
#     elif not isinstance(data, np.ndarray):
#         print('Input data must be a numpy array or pandas data frame')
#         sys.exit(1)

#     if variation_measure == 'std':
#         v_all = np.nanstd(a=data, axis=0)
#     elif variation_measure == 'mad':
#         v_all = median_absolute_deviation(data=data, axis=0, ignore_nan=True)
#     else:
#         v_all = np.nanvar(a=data, axis=0)

#     indices = np.where(np.invert(np.isnan(v_all)))[0]
#     v = v_all[indices]

#     if draw_histogram:
#         if len(v) < 50:
#             print('There must be at least 50 features with variation measures to draw a histogram')
#         else:
#             bins = int(min(bins, len(v)))
#             _ = plt.hist(v, bins=bins, log=log)
#             plt.show()

#     if threshold is None and num is None:
#         return np.array([])
#     elif threshold is not None and num is not None:
#         print('threshold and portion can not be used simultaneously. Only one of them can take a real value')
#         sys.exit(1)

#     if threshold is not None:
#         indices = indices[np.where(v > threshold)[0]]
#     else:
#         n_f = int(min(num, len(v)))
#         indices = indices[np.argsort(-v)[:n_f]]

#     indices = np.sort(indices)

#     return indices

# def min_max_transform(data):
#     '''
#     This function does a linear transformation of each feature, so that the minimum and maximum values of a
#     feature are 0 and 1, respectively.

#     Input:
#     data: an input data array with a size of [n_sample, n_feature]
#     Return:
#     norm_data: the data array after transformation
#     '''

#     norm_data = np.empty(data.shape)
#     norm_data.fill(np.nan)
#     for i in range(data.shape[1]):
#         v = data[:, i].copy()
#         if np.max(v) == np.min(v):
#             norm_data[:, i] = 0
#         else:
#             v = (v - np.min(v)) / (np.max(v) - np.min(v))
#             norm_data[:, i] = v
#     return norm_data

# id = select_features_by_variation(features, variation_measure='var', num=900)
# features_full = features.copy()
# features = features[:, id]

# %%
# generator = TabMapGenerator(metric='correlation', loss_fun='kl_loss', epsilon=0.0, version=2, add_const=True, num_iter=200)
# # generator = TabMapGenerator(metric='correlation', loss_fun='kl_loss', version=1)
# generator.fit(features, truncate=False)
# images = generator.transform(features)

# # %%
# np.save('bctil_image.npy', images)

# # %%
# for i in set(labels):
#     fig, axes = plt.subplots(1, 5)
#     for j in range(5):
#         axes[j].imshow(images[labels==i][j], cmap='viridis')
#     plt.show()

# %%
from sklearn.model_selection import StratifiedKFold, train_test_split, StratifiedShuffleSplit
from config import DL_MODELS, DL_MODELS_IMAGE_BASED, ML_MODELS, METRICS
from hparams_tuner.ml_models_tuner import MLModelTuner
from hparams_tuner.dl_models_tuner_gridsearchcv import DLModelTuner
from evaluate_model import Model_Evaluation
import random

predictions_test_df = pd.DataFrame()
performance_test_df = pd.DataFrame()
best_hparams = []
seed = 0

def seed_everything(seed: int):
    """Seed all random number generators."""
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

seed_everything(seed)


skf = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=seed)
for fold_id, (train_idx_all, test_idx) in enumerate(skf.split(features, labels)):
    
    # Stratified Sampling for train and val
    train_idx, valid_idx = train_test_split(train_idx_all,
                                    test_size=0.125,
                                    random_state=seed,
                                    stratify=labels[train_idx_all])

    print('\nFold_ID', fold_id)
    
    for model_id in ['tabmap']:
        print(f'\nTraining {model_id}')
        
        if model_id in DL_MODELS_IMAGE_BASED:
            images_save_path = os.path.join(data_dir, f"{model_id}.npy")
            # if not os.path.exists(images_save_path):
            generator = TabMapGenerator(metric='correlation', 
                            loss_fun='kl_loss', 
                            version=2,
                            add_const=True)
            generator.fit(features[train_idx])
            
            X_train_img = generator.transform(features[train_idx])
            X_test_img = generator.transform(features[test_idx])
            images = np.empty((len(features), X_train_img.shape[1], X_train_img.shape[2]))  # Initialize tabmap array
            images[train_idx] = X_train_img
            images[test_idx] = X_test_img
            np.save(images_save_path, images)

        data_config = {
            "data_set": data_set,
            "data_dir": data_dir,
            "n_classes": n_classes,
            "input_size": images.shape[1:] \
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
            y_pred = model_eval.model_predict(tuner.final_model, features=images[test_idx], multilabel=False)
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

# %% [markdown]
# ### SHAP value

# %%
##SHAP
import torch
import sys
import shap

sys.path.append('/home/yan/genomap/classification/ours/')

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

train_data = [(images[i], labels[i]) for i in train_idx]
test_data = [(images[i], labels[i]) for i in test_idx]

dataloader_train = torch.utils.data.DataLoader(
        train_data,
        batch_size=len(train_idx),
        shuffle=False,
        drop_last=False
    )

dataloader_test = torch.utils.data.DataLoader(
        test_data,
        batch_size=len(test_idx),
        shuffle=False,
        drop_last=False
    )

train_images, _ = next(iter(dataloader_train))
test_images, _ = next(iter(dataloader_test))
train_images = torch.unsqueeze(train_images, axis=1).float()
test_images = torch.unsqueeze(test_images, axis=1).float()
background = train_images[:1000].to(device)
test_images = test_images.to(device)

# %%
# background.shape

# %%
e = shap.DeepExplainer(tuner.final_model, background)

# %%
shap_values = e.shap_values(test_images)

# %%
np.save('bctil_shap.npy', np.array(shap_values))

# %% [markdown]
# ### Feature importance analysis

# %%
# Load projection matrix
projMap = generator.project_matrix
print(projMap.shape)

order_mapping = {} #key: feature index in original data, value: pixel index in genomap flatten vector
for i, col_id in enumerate(range(projMap.shape[1])):
    org_idx = int(np.nonzero(projMap[:, col_id])[0][0])
    order_mapping[org_idx] = i

# %%
all_indices = list(range(images[0].flatten().shape[0]))
zero_padding_indices = np.where(~images.reshape(images.shape[0], -1).any(axis=0))[0].astype(int).tolist()
indices_keep = list(set(all_indices) - set(zero_padding_indices))

# %%
from collections import defaultdict
tabmap_shap = defaultdict(list)
for i, class_id in enumerate(list(set(y_pred))):
    for shap_value in shap_values[i]:
        shap_dim = shap_value.shape
        shap_value_flattened = shap_value.flatten()
        shap_value_flattened = shap_value_flattened[indices_keep]
        shap_value_reordered = [shap_value_flattened[idx] for idx in dict(sorted(order_mapping.items())).values()]
        tabmap_shap[class_id].append(shap_value_reordered)

# %%
tabmap_shap = {class_id:np.stack(shap_value) for class_id, shap_value in tabmap_shap.items()}

# %%
from scipy.special import softmax

feature_importances_list = []
feature_importances_norm_list = []
for i, class_id in enumerate(list(set(y_pred))):
    # if class_id == 1:
    importances = []
    for k in range(tabmap_shap[class_id].shape[1]):
        importances.append(np.mean(np.abs(tabmap_shap[class_id][:,k])))
    # Organize the importances and columns in a dictionary
    feature_importances = {fea: imp for imp, fea in zip(importances, feature_names)}
    # Sorts the dictionary
    feature_importances = {k: v for k, v in sorted(feature_importances.items(), key=lambda item: item[1], reverse = True)}
    feature_importances_list.append(feature_importances)

# Prints the feature importances
for i, class_id in enumerate(list(set(y_pred))):
    for k, v in feature_importances.items():
        print(f"{k} -> {v:.4f}")

# %%
# CL_0000576 -> 0 monocyte, mono
# CL_0000624 -> 1 CD4-positive, alpha-beta T cell, rgcc+?
# CL_0000798 -> 2 gamma-delta T cell, gamma-delta
# CL_0000815 -> 3 regulatory T cell, FOXP3+
# CL_0000897 -> 4 CD4-positive, alpha-beta memory T cell
# CL_0000909 -> 5 CD8-positive, alpha-beta memory T cell

# CL_0000576 -> 0
# CL_0000624 -> 1
# CL_0000798 -> 2
# CL_0000815 -> 3
# CL_0000897 -> 4
# CL_0000909 -> 5

label_mapping = {0: 'monocyte', 1: 'CD4-positive, alpha-beta T cell', 2: 'gamma-delta T cell',
                 3: 'regulatory T cell', 4: 'CD4-positive, alpha-beta memory T cell', 5:'CD8-positive, alpha-beta memory T cell'}

# %%
for i in range(6):
    feature_importances_sum = {k: 0 for k in feature_names} 
    for k in feature_names:
        feature_importances_sum[k] = feature_importances_list[i].get(k, 0)
    
    feature_importances_sum = {k: v for k, v in sorted(feature_importances_sum.items(), key=lambda item: item[1], reverse = False)}
    features_new = list(feature_importances_sum.keys())[-20:]
    
    df_plot_list = [feature_importances_list[i][k] for k in features_new]
    df_plot = pd.DataFrame(df_plot_list, index = features_new)
    df_plot.plot(kind='barh', stacked=True, width=0.7, figsize=(8, 10))
    plt.title(f'TabMap with SHAP DeepExplainer {label_mapping[i]}')
    plt.show()
    
    #https://storage.googleapis.com/fc-76726bc2-9a90-4881-8ef4-c1e9dff68d87/cluster.txt?GoogleAccessId=116798894341-compute%40developer.gserviceaccount.com&Expires=1709870841&Signature=ays9n7V3OsIbsFXeSamQMPtk2SsTobDmRT0BJjv3cmu%2BApbZ79BxqBJXCbAmgTohEzlZ%2B%2FfEGaRlJzyVMMTQQLuZHNhxMj4IdXBrUPOLehJacOkVxei7XYSG1dP%2BYaZEgSgUoDR%2BQdT0DKbo4zAFNfBdjP%2FAPLdrVXnGqOBH2%2Bk4sed7O%2BNJkWdkFhd2iBtMQBHA3yWK4v5415kPAYOCrDScSCoVhp7V5rm2j1LmPszGvhMSKyNASqZn%2FrFy9ldhRSCr8WQOLEnD%2B55A0P2dcvxgF4Tuq5uOS8rrUCqJ6HtDJnaJKx6ZXuvzYBB83TGN%2FDLG%2BK0OgaKB0sMq9c0XeQ%3D%3D

# %%
feature_importances_sum = {k: 0 for k in feature_names}  # Initialize sum dictionary
# Iterate through each dictionary and sum the importances
for i in range(6):  # Assuming you want to include the first 5 dictionaries
    for k in feature_names:
        feature_importances_sum[k] += feature_importances_list[i].get(k, 0)

df_plot_dict = {}
for i in range(6):
    df_plot_dict[i] = [feature_importances_list[i][k] for k in features_new]

df_plot = pd.DataFrame(df_plot_dict, index = features_new)

df_plot.plot(kind='barh', stacked=True, width=0.7, figsize=(8, 10))
plt.title('TabMap with SHAP DeepExplainer ')

plt.show()


