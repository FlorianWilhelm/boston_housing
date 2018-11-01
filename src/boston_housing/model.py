import logging

import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.model_selection import KFold, GridSearchCV
from sklearn.tree import DecisionTreeRegressor


_logger = logging.getLogger(__name__)


def get_boston_df():
    boston = load_boston()
    df = pd.DataFrame(boston.data, columns=(c.lower() for c in boston.feature_names))
    df['price'] = boston.target
    return df


def fit_model(X, y, random_state=None):
    reg = DecisionTreeRegressor(random_state=random_state)
    c_grid = dict(max_depth=np.arange(10, 11))
    cv = KFold(n_splits=5, shuffle=True, random_state=random_state)
    clf = GridSearchCV(estimator=reg, param_grid=c_grid, cv=cv)
    clf.fit(X, y)
    _logger.info("Best score is {}".format(clf.best_score_))
    return clf.best_estimator_

