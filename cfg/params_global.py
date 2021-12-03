"""
Copyright 2021 Institute of Theoretical and Applied Informatics,
Polish Academy of Sciences (ITAI PAS) https://www.iitis.pl
Authors:
- Bartosz Grabowski (ITAI PAS, ORCID ID: 0000−0002−2364−6547)
- Przemysław Głomb (ITAI PAS, ORCID ID: 0000−0002−0215−4674),
- Kamil Książek (ITAI PAS, ORCID ID: 0000−0002−0201−6220),
- Krisztián Buza (Sapientia Hungarian University of Transylvania, ORCID ID: 0000-0002-7111-6452)
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
---
Autoencoders pretraining using clustering v.1.0
Related to the work:
Improving Autoencoders Performance for Hyperspectral Unmixing using Clustering
Source code for the review process of the 14th Asian Conference on Intelligent
Information and Database Systems (ACIIDS 2022)
"""

from ate.ate_loss import LossMSE


params_global = {
    'path_data': None,  # dataset dir
    'path_results': None,  # path of results
    'path_visualisations': None,  # path of visualisations
    'path_tune': None,  # path of tune
    'optim': 'adam',  # optimizer (Adam by default)
    'normalisation': 'max',  # a way of normalisation
    'loss_type': LossMSE(),  # loss function
    'weights_init': None,  # weights initialization
    'weights_modification': {
        'encoder_path': None,
        'decoder_path': None
    },
    'autoencoder_name': 'basic',
    'dataset_name': None,
    'seed': None,  # set deterministic results (or None)
    'cube_shape': None,  # full shape of the given image
}