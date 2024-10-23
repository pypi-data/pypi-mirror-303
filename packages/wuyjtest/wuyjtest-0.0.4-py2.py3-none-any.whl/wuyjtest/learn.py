# -*- coding: utf8 -*-
def hello(name: str = "world"):
    """
    ################# 随机森林回归代码   baseline
    import numpy as np
    import pandas as pd
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import MinMaxScaler

    # 读取数据
    data = pd.read_csv('house_price_dataset.csv')

    # 分离特征和目标
    X = data.drop(['SalePrice'], axis=1)
    y = data['SalePrice']

    # 数据集划分
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 特征缩放
    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 初始化随机森林模型
    rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

    # 训练模型
    rf_regressor.fit(X_train_scaled, y_train)

    # 进行预测
    y_pred = rf_regressor.predict(X_test_scaled)

    # 反缩放，得到原始单位的房价预测值
    y_pred_scaled = scaler.inverse_transform(y_pred.reshape(-1, 1))

    # 输出RMSE
    from sklearn.metrics import mean_squared_error
    rmse = np.sqrt(mean_squared_error(y_test, y_pred_scaled.ravel()))
    print(f"RMSE: {rmse}")

    # 保存模型
    import joblib
    joblib.dump(rf_regressor, 'random_forest_regressor.pkl')"""
    