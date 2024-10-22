import os
import time
import json
# from image_generators.refined_construction import generate_refined
from dataloader.dataset import load_data
from TabMap.code.tabmap_construction import TabMapGenerator
# from image_generators.IGTD_construction import table_to_image
from pyDeepInsight import ImageTransformer
import pandas as pd
from sklearn.manifold import TSNE
from sklearn.datasets import make_classification

def compute_runtime(features, feature_names):
    runtime_records = {}
    for model_id in ['tabmap', 'IGTD', 'REFINED']: #, 
        print(model_id)
        start = time.time()
        if model_id == 'tabmap':
            generator = TabMapGenerator(metric='correlation',
                                        loss_fun='kl_loss', 
                                        epsilon=0.0, 
                                        add_const=True)
            generator.fit(features, nd=False, truncate=False)
            images = generator.transform(features)
        
        if model_id == 'REFINED':
            images = generate_refined(features, feature_names=feature_names)

        if model_id == 'DI':
            reducer = TSNE(n_components=2, metric='cosine', perplexity=5, random_state=42)
            it = ImageTransformer(feature_extractor=reducer, pixels=(50, 50))
            images = it.fit_transform(features, img_format='scalar')
        
        if model_id == 'IGTD':
            images, _ = table_to_image(features, 
                                       fea_dist_method='Pearson',
                                       image_dist_method='Euclidean',
                                       max_step=10000, val_step=300, 
                                       error='abs', seed=42)
        
        elapsed_time = time.time() - start
        # hours = int(elapsed_time // 3600)
        # minutes = int((elapsed_time % 3600) // 60)
        # seconds = int(elapsed_time % 60) {hours}h:{minutes}m:
        runtime_records[model_id] = f'{elapsed_time}s'
    
    return runtime_records

def generate_synthetic_data(n_samples, n_features):
    random_seed = 42
    # Create synthetic classification datasets
    features, labels = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        random_state=random_seed
    )
    return features, labels

############# Compare Runtime for synthetic data #############
# runtime_dict = {}
# for n_samples in [100, 500, 1000, 2000, 5000, 10000, 20000]:
#     for n_features in [50000, 100000]: #  
#         print(n_features, n_samples)
#         try:
#             features, labels = generate_synthetic_data(n_samples, n_features)
#             runtime_dict[f'ns{n_samples}_nf{n_features}'] = compute_runtime(features)
#             with open("/home/yan/pyTabMap/results/ablation_study/runtime/runtime_new2.json", "w") as json_file:
#                 json.dump(runtime_dict, json_file, indent=4)
#         except Exception as e:
#             print(f"An error occurred: {e}")

# # ############# Compare Runtime for each dataset #############
data_path = '/home/yan/pyTabMap/data'
data_set_list = ['isolet']
# data_set_list = [ 'parkinson', 'qsar_biodeg', 'har', 'micromass', 'isolet', 'wdbc', 'lung', 'tox171', 'arcene', 'p53', 'METABRIC', ]
for data_set in data_set_list:
    runtime_dict = {}
    data_dir = os.path.join(data_path, data_set)
    features, labels, feature_names = load_data(data_dir, preprocessed=False)
    runtime_dict[data_set] = compute_runtime(features, feature_names)
    with open(f"/home/yan/pyTabMap/data/runtime_final_2/runtime_{data_set}.json", "w") as json_file:
        json.dump(runtime_dict, json_file, indent=4)

# data_path = '/home/yan/pyTabMap/data'
# runtime_dict = {}
# data_set = 'onconpc'
# data_dir = os.path.join(data_path, data_set)

# # Load the dataset into a pandas dataframe
# features = pd.read_csv(f'{data_dir}/onconpc_processed_features.csv', index_col='RANDID')
# labels = pd.read_csv(f'{data_dir}/onconpc_processed_labels.csv', index_col='RANDID')
# # Find train test splits used in the paper
# all_samples = pd.read_csv(f'{data_dir}/onconpc_processed_labels.csv')['RANDID'].values.tolist()
# test_samples = pd.read_csv(f'{data_dir}/onconpc_predictions_on_held_outs.csv')['RANDID'].values.tolist()
# train_samples = [item for item in all_samples if item not in test_samples]

# features = pd.concat([features.loc[train_samples], features.loc[test_samples]])
# labels = pd.concat([labels.loc[train_samples], labels.loc[test_samples]])
# # labels = labels['cancer_label'].values
# # print(train_features.shape, test_features.shape)
# print(features.shape, labels.shape)
# # if args.scaler_name == 'quantile': 
# #    scaler = QuantileTransformer(output_distribution='normal', random_state=args.seed)
# # if args.scaler_name == 'minmax':
# #     scaler = MinMaxScaler()
# # features_normalized = scaler.fit_transform(features)
# df_features = pd.DataFrame(features, index=features.index, columns=features.columns)
# # le = LabelEncoder()
# # labels = le.fit_transform(labels)
# df_labels = labels['cancer_label']
# labels = df_labels.values
    
# # save train features and labels
# df_features.to_csv(f'{data_dir}/features.csv')
# df_labels.to_csv(f'{data_dir}/labels.csv')
# n_classes = len(set(labels))
# features = df_features.values
# feature_names = df_features.columns.to_list()

# runtime_dict[data_set] = compute_runtime(features, feature_names)
# with open(f"/home/yan/pyTabMap/data/runtime_final/runtime_{data_set}.json", "w") as json_file:
#     json.dump(runtime_dict, json_file, indent=4)