#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

__all__ = ["Regressor"]


class Regressor:
    def __init__(
        self,
    ):
        self.model = DecisionTreeRegressor()

    def fit(self, data, y=None, yidx=-1):
        """모델을 학습시킨다

        Args:
            data (list): X, y를 모두 포함하는 경우는 yidex를 설정해야 한다.
            y (list, optional): 정답값이 포함된 파이썬 리스트. Defaults to None.
            yidx (int, optional): data에 X, y값이 모두 포함되어있을 경우, y값으로 사용될 컬럼의 인덱스를 지정한다. Defaults to -1.

        Returns:
            _type_: _description_
        """
        if y is None:
            df = pd.DataFrame(data)
            X = df.drop(df.columns[yidx], axis=1).values
            y = df.iloc[:, yidx].values
            self.model.fit(X, y)
        else:
            self.model.fit(data, y)
        return self

    def predict(self, data):
        return self.model.predict(data)

    def score(self, X, y):
        return self.model.score(X, y)
