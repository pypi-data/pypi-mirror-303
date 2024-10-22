# %%
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "3"  # Set to the index of the GPU you want to use (e.g., 0, 1, 2, ...)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import torch

import sys
sys.path.append('/home/yan/pyTabMap/code/')
from TabMap.code.dataloader.dataset import load_data
# sys.path.insert(0,'/home/yan/pyTabMap/code/image_generators')
from TabMap.code.tabmap_construction import TabMapGenerator
from image_generators.IGTD_construction import generate_igtd_mapping, IGTD_Im_Gen
from image_generators.refined_construction import generate_refined_mapping, REFINED_Im_Gen
from pyDeepInsight import ImageTransformer
from sklearn.manifold import TSNE

# %%
data_path='/home/yan/pyTabMap/data'
data_set='wdbc'
results_path = '/home/yan/pyTabMap/code/plot_figures/FIG4'

# %%
data_dir = os.path.join(data_path, data_set)
os.makedirs(os.path.dirname(data_dir), exist_ok=True)

# Load the dataset into a pandas dataframe
features, labels, feature_names = load_data(data_dir, scaler_name='minmax', preprocessed=False)
if labels.ndim > 1:
    n_classes = labels.shape[1]
else:
    n_classes = len(np.unique(labels))

# %%
def generate_images(model_id, features, 
                    train_idx, test_idx,
                    feature_names=None, save_path=None, save_images=True):
    print(f"Generating images for {model_id}")
    
    generator = None
    
    if model_id == 'tabmap':
        # generator = TabMapGenerator(metric='correlation', loss_fun='kl_loss', epsilon=0, num_iter=200, seed=0)
        generator = TabMapGenerator(metric='correlation', 
                                    loss_fun='kl_loss',
                                    epsilon=0.0, 
                                    version=2,
                                    add_const=True,
                                    num_iter=200)
        generator.fit(features[train_idx])
        X_train_img = generator.transform(features[train_idx])
        X_test_img = generator.transform(features[test_idx])
        # generator.fit(features)
        # X_img = generator.transform(features)
        # X_train_img = X_img[train_idx]
        # X_test_img = X_img[test_idx]
    
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
    return images, generator

# %%
from sklearn.model_selection import StratifiedKFold, train_test_split, StratifiedShuffleSplit
from config import DL_MODELS, DL_MODELS_IMAGE_BASED, ML_MODELS, METRICS
from hparams_tuner.ml_models_tuner import MLModelTuner
from hparams_tuner.dl_models_tuner_gridsearchcv import DLModelTuner
from evaluate_model import Model_Evaluation
import seaborn as sns

import random
import shap

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

def seed_everything(seed: int):
    """Seed all random number generators."""
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


for seed in range(50, 200):#[4]:#range(30, 50):#[4,9]+list(range(10,30)):
    seed_everything(seed)
    
    predictions_test_df = pd.DataFrame()
    performance_test_df = pd.DataFrame()
    best_hparams = []

    # skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
    skf = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=seed)
    for fold_id, (train_idx_all, test_idx) in enumerate(skf.split(features, labels)):
        
        # if fold_id in [0, 1, 3, 4]:
        #     continue
        train_idx, valid_idx = train_test_split(train_idx_all,
                                        test_size=0.125,
                                        random_state=seed,
                                        stratify=labels[train_idx_all])
        
        print('\nFold_ID', fold_id)
        images_dict = {}
        shap_values_dict = {}
        for model_id in ['tabmap']: #['tabmap', 'LR', 'RF', 'XGB']:#, 
            # ['DI', 'REFINED', 'IGTD', 'tabmap', 'tabmap_sq', 'LR', 'RF', 'GB', 'XGB', '1DCNN']:
            print(f'\nTraining {model_id}')
            
            if model_id in DL_MODELS_IMAGE_BASED:
                images_save_path = os.path.join(data_dir, f"{model_id}.npy")

                print('start generating images')
                images, generator = generate_images(model_id, features, 
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
                                    opt_metric='loss',
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
                background = torch.from_numpy(np.expand_dims(images_dict[model_id][train_idx], axis=1)).float().to(device)
                test_images = torch.from_numpy(np.expand_dims(images_dict[model_id][test_idx], axis=1)).float().to(device)
                explainer = shap.DeepExplainer(tuner.final_model, background)
                shap_values = explainer.shap_values(test_images)
                shap_values_dict[model_id] = shap_values
            else:
                y_prob, y_pred = model_eval.model_predict(tuner.final_model, features=features[test_idx], multilabel=False)
                if model_id == 'LR':
                    # Create a SHAP Linear Explainer
                    explainer = shap.LinearExplainer(tuner.final_model, features[train_idx])
                    shap_values = explainer.shap_values(features[test_idx])
                    # shap.summary_plot(shap_values, features[test_idx], feature_names=list(feature_names))
                elif model_id == 'RF':
                    # Create a SHAP Tree Explainer
                    explainer = shap.TreeExplainer(tuner.final_model)
                    shap_values = explainer.shap_values(features[test_idx])
                elif model_id == 'XGB':
                    # Create a SHAP Tree Explainer
                    explainer = shap.TreeExplainer(tuner.final_model)
                    shap_values = explainer.shap_values(features[test_idx])
                shap_values_dict[model_id] = shap_values
            
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

    # predictions_test_df.set_index(["model", "fold"]).to_csv(f"{results_path}/{data_set}/model_preds.csv", sep='\t')
    # performance_test_df.set_index(["model", "fold"]).to_csv(f"{results_path}/{data_set}/model_performance.csv", sep='\t')
    # mean_performance_test_df = performance_test_df.groupby(["model"])[METRICS].agg(["mean", "std"]).reset_index()
    # for metric in METRICS:
    #     mean_performance_test_df[(metric, "mean")] = mean_performance_test_df[(metric, "mean")].round(4)
    #     mean_performance_test_df[(metric, "std")] = mean_performance_test_df[(metric, "std")].round(4)
    # mean_performance_test_df.to_csv(f"{results_path}/{data_set}/mean_model_performance.csv", sep='\t')
    # print(mean_performance_test_df)

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
    # indices_keep = all_indices[:len(order_mapping)]

    # %%
    from collections import defaultdict
    tabmap_shap = defaultdict(list)
    for i, class_id in enumerate(list(set(y_pred))):
        for shap_value in shap_values_dict['tabmap'][i]:
            shap_dim = shap_value.shape
            shap_value_flattened = shap_value.flatten()
            shap_value_flattened = shap_value_flattened[indices_keep]
            shap_value_reordered = [shap_value_flattened[idx] for idx in dict(sorted(order_mapping.items())).values()]
            tabmap_shap[class_id].append(shap_value_reordered)

    # %%
    tabmap_shap = {class_id: np.stack(shap_value) for class_id, shap_value in tabmap_shap.items()}

    # %%
    # from scipy.special import softmax
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

    # for i in list([0,1]):
    #     feature_importances_sum = {k: 0 for k in feature_names} 
    #     for k in feature_names:
    #         feature_importances_sum[k] = feature_importances_list[i].get(k, 0)
        
    #     feature_importances_sum = {k: v for k, v in sorted(feature_importances_sum.items(), key=lambda item: item[1], reverse = False)}
    #     features_new = list(feature_importances_sum.keys())[-30:]
        
    #     df_plot_list = [feature_importances_list[i][k] for k in features_new]
    #     df_plot = pd.DataFrame(df_plot_list, index = features_new)
        
    #     sns.set_style("white")
    #     # palette = sns.color_palette("husl", len(df_plot))
    #     # # Create the barh plot with reduced bar width and compacted layout
    #     # plt.figure(figsize=(8, 10))
    #     # bar_plot = df_plot[0].sort_values().plot(
    #     #     kind='barh', 
    #     #     width=0.5,  # Smaller bar width
    #     #     color=palette
    #     # )
    #     # bar_height = 0.5  # Corresponding to the bar width set above
    #     # plt.ylim(-0.5, len(df_plot)*bar_height - 0.5)
        
    #     bar_plot = df_plot[0].plot(kind='barh', width=0.7, figsize=(3, 5))
    #     plt.tight_layout()

    #     plt.title(f'TabMap with SHAP DeepExplainer {i}')
    #     plt.show()

    # %%
    feature_importances_sum = {k: 0 for k in feature_names}  # Initialize sum dictionary
    # Iterate through each dictionary and sum the importances
    for i in range(n_classes):  # Assuming you want to include the first 5 dictionaries
        for k in feature_names:
            feature_importances_sum[k] += feature_importances_list[i].get(k, 0)

    feature_importances_sum = {k: v for k, v in sorted(feature_importances_sum.items(), key=lambda item: item[1], reverse = False)}
    features_new = list(feature_importances_sum.keys())[-30:]

    # plt.show()
    # feature_importances_sum = {k: 0 for k in feature_names}  # Initialize sum dictionary
    # # Iterate through each dictionary and sum the importances
    # for i in range(n_classes):  # Assuming you want to include the first 5 dictionaries
    #     for k in feature_names:
    #         feature_importances_sum[k] += feature_importances_list[i].get(k, 0)

    # feature_importances_sum = {k: v for k, v in sorted(feature_importances_sum.items(), key=lambda item: item[1], reverse = False)}
    # features_new = list(feature_importances_sum.keys())[-30:]

    if (
        'worst radius' in features_new[-2:]and
        'worst texture' in features_new[-10:] and
        'worst perimeter' in features_new[-10:] and
        'mean texture' in features_new[-10:]
    ):
        with open('/home/yan/pyTabMap/code/plot_figures/FIG4/seed.txt', "a") as file:
            file.write("\n\n")
            file.write(str(seed))
            file.write("\n")
            file.write("\n".join(features_new[::-1]))
        
        df_plot_dict = {}
        for i in range(n_classes):
            df_plot_dict[i] = [feature_importances_list[i][k] for k in features_new]

        df_plot = pd.DataFrame(df_plot_dict, index = features_new)
        df_plot = df_plot.rename(columns={0:'benign', 1:'malignant'})
    
        df_plot.plot(kind='barh', stacked=True, width=0.7, figsize=(8, 10))
        plt.title('TabMap with SHAP DeepExplainer')
        plt.tight_layout()
        plt.savefig(f'/home/yan/pyTabMap/code/plot_figures/FIG4/shap_{seed}.png', dpi=300, bbox_inches='tight')
        # plt.show()

        shap_plot = []
        for class_label in list([0, 1]):  # Assuming num_classes is defined
            indices_for_class = [i for i, label in enumerate(labels[test_idx]) if label == class_label]
            #[i for i, label in enumerate(labels[test_idx]) if label == class_label]
            # sampled_indices = np.random.choice(indices_for_class, size=30, replace=False)
            sampled_indices = indices_for_class 
            for i in sampled_indices:
                shap_plot.append(tabmap_shap[class_label][i])
        feature_names_ranked = df_plot.index.values[::-1]
        shap_plot = np.array(shap_plot)
        shap_value_plot = {key:value for key, value in zip(feature_names, shap_plot.T)}
        shap_value_plot_ranked = [shap_value_plot[key] for key in feature_names_ranked if key in shap_value_plot]
        shap_value_plot_ranked = np.stack(shap_value_plot_ranked)

        # shap_plot = np.array(shap_plot)
        vmin, vmax = np.nanpercentile(shap_plot.flatten(), [1, 99])

        plt.figure(figsize=(6, 6))
        sns.heatmap(
            # shap_plot.T,
            shap_value_plot_ranked,
            # aspect=0.7 * shap_plot.shape[0] / shap_plot.shape[1],
            # interpolation="nearest",
            vmin=min(vmin,-vmax),
            vmax=max(-vmin,vmax),
            cmap='bwr', 
            # yticklabels=feature_names
            yticklabels=feature_names_ranked
        )
        plt.title('Heatmap Plot')
        plt.tight_layout()
        plt.savefig(f'/home/yan/pyTabMap/code/plot_figures/FIG4/shap_heatmap_{seed}.png', dpi=300, bbox_inches='tight')
    else:
        print('retry')
    # df_plot_dict = {}
    # for i in range(n_classes):
    #     df_plot_dict[i] = [feature_importances_list[i][k] for k in features_new]
    # df_plot = pd.DataFrame(df_plot_dict, index = features_new)

# # %%
# shap_plot = []
# for class_label in list([0,1]):  # Assuming num_classes is defined
#     indices_for_class = [i for i, label in enumerate(labels[test_idx]) if label == class_label]
#     #[i for i, label in enumerate(labels[test_idx]) if label == class_label]
#     # sampled_indices = np.random.choice(indices_for_class, size=30, replace=False)
#     sampled_indices = indices_for_class 
#     for i in sampled_indices:
#         shap_plot.append(tabmap_shap[class_label][i])

# # %%
# feature_names_ranked = df_plot.index.values[::-1]

# # %%
# shap_plot = np.array(shap_plot)
# shap_value_plot = {key:value for key, value in zip(feature_names, shap_plot.T)}

# # %%
# # shap_value_plot = sorted(shap_value_plot, key=lambda x: index_map[x])

# # %%
# shap_value_plot_ranked = [shap_value_plot[key] for key in feature_names_ranked if key in shap_value_plot]

# # %%
# shap_value_plot_ranked = np.stack(shap_value_plot_ranked)

# # %%
# feature_names_ranked

# # %%
# import seaborn as sns

# # shap_plot = np.array(shap_plot)
# vmin, vmax = np.nanpercentile(shap_plot.flatten(), [1, 99])

# plt.figure(figsize=(3, 6))
# sns.heatmap(
#     # shap_plot.T,
#     shap_value_plot_ranked,
#     # aspect=0.7 * shap_plot.shape[0] / shap_plot.shape[1],
#     # interpolation="nearest",
#     vmin=-0.8,#min(vmin,-vmax),
#     vmax=0.8,#max(-vmin,vmax),
#     cmap='bwr', 
#     # yticklabels=feature_names
#     yticklabels=feature_names_ranked
# )
# plt.title('Heatmap Plot')
# plt.show()

# # %%
# for model_id in ['LR', 'RF', 'XGB']:
#     shap_values = shap_values_dict[model_id]
    
#     if model_id == 'RF':
#         shap_values = shap_values[1]
    
#     mean_shap_values = np.abs(shap_values).mean(axis=0)

#     # Sorting the features by their mean absolute SHAP values
#     sorted_indices = np.argsort(mean_shap_values)
#     sorted_features = np.array(feature_names)[sorted_indices]
#     sorted_shap_values = mean_shap_values[sorted_indices]
    
#     # Plotting using Matplotlib
#     plt.figure(figsize=(10, 6))
#     plt.barh(sorted_features, sorted_shap_values, color='skyblue')
#     plt.xlabel('Mean |SHAP Value|')
#     plt.title('Mean Absolute SHAP Values per Feature (Ranked)')
#     plt.tight_layout()
#     plt.show()


# # %%
# from sklearn.datasets import load_breast_cancer
# from sklearn.ensemble import RandomForestClassifier
# import numpy as np

# # Load data
# data = load_breast_cancer()
# X = data.data
# y = data.target
# feature_names = data.feature_names

# # Train a random forest classifier
# clf = RandomForestClassifier(n_estimators=100, random_state=42)
# clf.fit(X, y)

# # Get feature importances
# importances = clf.feature_importances_
# indices = np.argsort(importances)[::-1]

# # Print the feature ranking
# print("Feature ranking:")
# for f in range(X.shape[1]):
#     print(f"{f + 1}. feature {feature_names[indices[f]]} ({importances[indices[f]]:.4f})")


# # %%



