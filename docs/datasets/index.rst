########
Datasets
########

.. toctree::
  :hidden:
  
  load_criteo_uplift_prediction
  download_criteo_uplift_prediction
  load_hillstrom_email_marketing
  download_hillstrom_email_marketing
  make_linear_regression

The pyuplift.datasets module includes utilities to load datasets, including methods to download and return popular datasets. It also features some artificial data generators.

*******
Loaders
*******
+-------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| `datasets.download_criteo_uplift_prediction([data_home, url]) <download_criteo_uplift_prediction.html>`_                            | Downloading the Criteo Uplift Prediction dataset.                  |
+-------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| `datasets.load_criteo_uplift_prediction([data_home, download_if_missing]) <load_criteo_uplift_prediction.html>`_                    | Loading the Criteo Uplift Prediction dataset from the local file.  |
+-------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| `datasets.download_hillstrom_email_marketing([data_home, url]) <download_hillstrom_email_marketing.html>`_                          | Downloading the Hillstrom Email Marketing dataset.                 |
+-------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| `datasets.load_hillstrom_email_marketing([data_home, load_raw_data, download_if_not_exist]) <load_hillstrom_email_marketing.html>`_ | Loading the Hillstrom Email Marketing dataset from the local file. |
+-------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+

**********
Generators
**********
+----------------------------------------------------------------------------------------------+--------------------------------------------+
| `datasets.make_linear_regression(size, [x1_params, x2_params, x3_params, t_params, e_params, | | Generate data by formula: Y' = X1+X2*T+E |
| eps, seed]) <make_linear_regression.html>`_                                                  | | Y = Y', if Y' - int(Y') > eps,           |
|                                                                                              | | Y = 0,  otherwise.                       |
+----------------------------------------------------------------------------------------------+--------------------------------------------+
