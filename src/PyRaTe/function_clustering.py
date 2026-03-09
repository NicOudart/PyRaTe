###############################################################################
#HEADER

#This function 

###############################################################################

#Libraries importation:--------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score,silhouette_samples

#Function definition:----------------------------------------------------------

def clustering(band_list,nb_clusters,seed=0):
    
    #K-means clustering:-------------------------------------------------------
    
    img_input = np.stack(band_list,axis=-1)
    
    dim_x,dim_y,dim_bands = img_input.shape
    
    features = img_input.reshape(-1,dim_bands)
    
    scaler = StandardScaler()
    features = scaler.fit_transform(features)
    
    kmeans = KMeans(n_clusters=nb_clusters,random_state=seed,n_init=10)
    kmeans.fit(features)
    
    labels = kmeans.labels_
    
    img_label = labels.reshape(dim_x,dim_y)
    
    cmap = plt.get_cmap("tab10",nb_clusters)
    norm = BoundaryNorm(np.arange(-0.5,nb_clusters+0.5,1),nb_clusters)
    
    fig_label,ax_label = plt.subplots()
    img_display = ax_label.imshow(img_label,origin='upper',cmap=cmap,norm=norm)
    
    colorbar = plt.colorbar(img_display,ticks=np.arange(nb_clusters))
    colorbar.ax.set_yticklabels(np.arange(nb_clusters))
    
    #Silhouette score:---------------------------------------------------------
    
    sample_idx = []
    for cluster in np.unique(labels):
        cluster_idx = np.where(labels == cluster)[0]
        nb_samples = min(1000,len(cluster_idx))
        cluster_sample = list(np.random.choice(cluster_idx,size=nb_samples,replace=False))
        sample_idx += cluster_sample
        
    sample_features = features[sample_idx]
    sample_labels = labels[sample_idx]
    
    average_score = silhouette_score(sample_features,sample_labels)
    sample_scores = silhouette_samples(sample_features,sample_labels)

    fig,ax = plt.subplots()

    y_lower = 10
    for idx in range(nb_clusters):
        sample_scores_idx = sample_scores[sample_labels==idx]
        sample_scores_idx.sort()

        size_cluster_idx = sample_scores_idx.shape[0]
        y_upper = y_lower + size_cluster_idx

        color = cmap(idx)
        ax.fill_betweenx(
            np.arange(y_lower, y_upper),
            0,
            sample_scores_idx,
            facecolor=color,
            edgecolor=color,
            alpha=0.7
        )

        ax.text(-0.05, y_lower + 0.5 * size_cluster_idx, str(idx))
        y_lower = y_upper + 10
        
    ax.axvline(x=average_score,color="red",linestyle="--")

    ax.set_yticks([])
    ax.set_xlim([-1, 1])
    ax.set_xlabel("Coefficient de silhouette",fontsize=12)
    ax.set_ylabel("Classes",fontsize=12)
    ax.set_title("Average silhouette score = "+str(round(average_score,3)),fontsize=12)
    
    plt.show()
    
    return img_label
    
    
        