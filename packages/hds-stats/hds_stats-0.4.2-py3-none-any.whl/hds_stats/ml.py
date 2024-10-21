
# 나무모형 시각화
def plot_tree(model, fileName = None, className = None):
    '''
    이 함수는 나무모형을 그립니다.
    
    매개변수:
        model: 사이킷런으로 적합한 나무모형을 지정합니다.
        fileName: 입력변수명을 지정합니다.(기본값: None)
        className: 분류모형은 목표변수의 범주를 지정합니다.(기본값: None)
    
    반환값:
        그래프 외에 반환하는 객체는 없습니다.
    '''
    
    import inspect
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.tree import export_graphviz
    import graphviz
    import os
    
    if fileName == None:
        global_objs = inspect.currentframe().f_back.f_globals.items()
        result = [name for name, value in global_objs if value is model]
        fileName = result[0]
    
    if type(model) == DecisionTreeRegressor:
        export_graphviz(
            decision_tree = model,
            out_file = f'{fileName}.dot',
            feature_names = model.feature_names_in_,
            filled = True,
            leaves_parallel = False,
            impurity = True
        )
    elif type(model) == DecisionTreeClassifier:
        if className == None:
            className = model.classes_
        export_graphviz(
            decision_tree = model,
            out_file = f'{fileName}.dot',
            class_names = className,
            feature_names = model.feature_names_in_,
            filled = True,
            leaves_parallel = False,
            impurity = True
        )
    
    with open(file = f'{fileName}.dot', mode = 'rt') as file:
        graph = file.read()
        graph = graphviz.Source(source = graph, format = 'png')
        graph.render(filename = fileName)
    
    os.remove(f'{fileName}')
    
    os.remove(f'{fileName}.dot')


# 입력변수별 중요도 시각화
def plot_feature_importance(model, pal = 'Spectral'):
    '''
    이 함수는 입력변수별 중요도로 막대 그래프를 그립니다.
    
    매개변수:
        model: 사이킷런으로 적합한 분류모형을 지정합니다.
        pal: 팔레트를 문자열로 지정합니다.(기본값: Spectral)
    
    반환값:
        그래프 외에 반환하는 객체는 없습니다.
    '''
    
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    if 'LGBM' in str(type(model)):
        fi = pd.DataFrame(
            data = model.feature_importances_, 
            index = model.feature_name_, 
            columns = ['importance']
        )
    else:
        fi = pd.DataFrame(
            data = model.feature_importances_, 
            index = model.feature_names_in_, 
            columns = ['importance']
        ) \
        .sort_values(by = 'importance', ascending = False) \
        .reset_index()
    
    sns.barplot(
        data = fi, 
        x = 'importance', 
        y = 'index', 
        hue = 'index', 
        palette = pal, 
        legend = True
    )
    
    for i, r in fi.iterrows():
        plt.text(
            x = r['importance'] + 0.01, 
            y = i, 
            s = f"{r['importance']:.3f}", 
            ha = 'left', 
            va = 'center', 
            fontsize = 8, 
            fontweight = 'bold'
        )
    
    plt.xlim(0, fi['importance'].max() * 1.2)
    
    plt.title(label = 'Feature Importances', 
              fontdict = {'fontweight': 'bold'})
    
    plt.xlabel(xlabel = 'Feature Importances')
    
    plt.ylabel(ylabel = 'Feature')
    
    plt.legend(loc = 'lower right',
               title = 'feat_imp', 
               fontsize = 8);


# 나무모형 가지치기 단계 그래프 시각화
def plot_step(data, x = 'alpha', y = 'impurity', color = 'blue', xangle = None):
    '''
    이 함수는 나무모형 가지치기 결과로 단계 그래프를 그립니다.
    
    매개변수:
        data: 나무모형의 가지치기 단계별 비용 복잡도 파라미터를 데이터프레임으로 지정합니다.
        x: x축에 지정할 변수명을 지정합니다.(기본값: alpha)
        y: y축에 지정할 변수명을 지정합니다.(기본값: impurity)
        color: 선과 점의 색을 문자열로 지정합니다.(기본값: blue)
        xangle: x축 회전 각도를 정수로 지정합니다.(기본값: None)
    
    반환값:
        그래프 외에 반환하는 객체는 없습니다.
    '''
    
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    sns.lineplot(
        data = data, 
        x = x, 
        y = y, 
        color = color, 
        drawstyle = 'steps-pre', 
        label = y
    )
    
    sns.scatterplot(
        data = data, 
        x = x, 
        y = y, 
        color = color, 
        s = 15
    )
    
    plt.xticks(rotation = xangle);


# 주성분 분석 스크리 도표 시각화
def plot_screeplot(x):
    '''
    이 함수는 주성분 점수 행렬로 스크리 도표를 그립니다.
    
    매개변수:
        x: 주성분 점수 행렬을 데이터프레임으로 지정합니다.
    
    반환값:
        그래프 외에 반환하는 객체는 없습니다.
    '''
    
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    x = x.var()
    n = len(x)
    xticks = range(1, n + 1)
    
    sns.lineplot(
        x = xticks, 
        y = x, 
        color = 'blue',
        linestyle = '-', 
        linewidth = 1, 
        marker = 'o'
    )
    
    plt.axhline(
        y = 1, 
        color = 'red', 
        linestyle = '--', 
        linewidth = 0.5
    )
    
    plt.xticks(ticks = xticks)
    
    plt.title(label = 'Scree Plot', 
              fontdict = {'fontweight': 'bold'})
    
    plt.xlabel(xlabel = 'Number of PC')
    
    plt.ylabel(ylabel = 'Variance');
    

# 주성분 분석 행렬도 시각화
def plot_biplot(score, coefs, x = 1, y = 2, zoom = 1):
    '''
    이 함수는 주성분 분석 결과를 받아 스크리 도표를 그립니다.
    
    매개변수:
        score: 주성분 점수 행렬을 데이터프레임으로 지정합니다.
        coefs: 고유벡터 행렬을 데이터프레임으로 지정합니다.
        x: x축에 지정할 주성분의 인덱스를 지정합니다.(기본값: 1)
        y: y축에 지정할 주성분의 인덱스를 지정합니다.(기본값: 2)
        zoom: 변수의 벡터 크기를 조절하는 값을 지정합니다. (기본값: 1)
    
    반환값:
        그래프 외에 반환하는 객체는 없습니다.
    '''
    
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    xs = score.iloc[:, x-1]
    
    ys = score.iloc[:, y-1]
    
    sns.scatterplot(
        x = xs, 
        y = ys, 
        fc = 'silver',
        ec = 'black',
        s = 15, 
        alpha = 0.2
    )
    
    plt.axvline(
        x = 0, 
        color = '0.5', 
        linestyle = '--', 
        linewidth = 0.5
    )
    
    plt.axhline(
        y = 0, 
        color = '0.5', 
        linestyle = '--', 
        linewidth = 0.5
    )
    
    n = score.shape[1]
    
    for i in range(n):
        plt.arrow(
            x = 0, 
            y = 0, 
            dx = coefs.iloc[i, x-1] * zoom, 
            dy = coefs.iloc[i, y-1] * zoom, 
            color = 'red',
            linewidth = 0.5,
            alpha = 0.5
        )
        
        plt.text(
            x = coefs.iloc[i, x-1] * (zoom + 0.5), 
            y = coefs.iloc[i, y-1] * (zoom + 0.5), 
            s = coefs.index[i], 
            color = 'darkred', 
            ha = 'center', 
            va = 'center', 
            fontsize = 8, 
            fontweight = 'bold'
        )
    
    # plt.xlim(-1, 1)
    # plt.ylim(-1, 1)
    # plt.grid()
    
    plt.title(label = 'Biplot with PC1 and PC2', 
              fontdict = {'fontweight': 'bold'})
    
    plt.xlabel(xlabel = 'PC{}'.format(x))
    
    plt.ylabel(ylabel = 'PC{}'.format(y));


# k-평균 군집분석 WSS 단계 그래프 시각화
def plot_wcss(X, k = 3):
    '''
    이 함수는 군집별 편차 제곱합으로 선 그래프를 그립니다.
    
    매개변수:
        X: 표준화된 데이터셋을 데이터프레임으로 지정합니다.
        k: 군집 개수를 지정합니다.(기본값: 3)
    
    반환값:
        그래프 외에 반환하는 객체는 없습니다.
    '''
    
    from sklearn.cluster import KMeans
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    ks = range(1, k + 1)
    
    result = []
    
    for k in ks:
        model = KMeans(n_clusters = k, random_state = 0)
        model.fit(X = X)
        wcss = model.inertia_
        result.append(wcss)
    
    sns.lineplot(x = ks, 
                 y = result, 
                 marker = 'o', 
                 linestyle = '-', 
                 linewidth = 1)
    
    plt.xticks(ticks = ks)
    
    plt.title(label = 'Elbow Method', 
              fontdict = {'fontweight': 'bold'})
    
    plt.xlabel(xlabel = 'Number of clusters')
    
    plt.ylabel(ylabel = 'Within Cluster Sum of Squares');


# k-평균 군집분석 실루엣 지수 시각화
def plot_silhouette(X, k = 3):
    '''
    이 함수는 군집별 실루엣 지수로 선 그래프를 그립니다.
    
    매개변수:
        X: 표준화된 데이터셋을 데이터프레임으로 지정합니다.
        k: 군집 개수를 지정합니다.(기본값: 3)
    
    반환값:
        그래프 외에 반환하는 객체는 없습니다.
    '''
    
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    ks = range(1, k + 1)
    
    result = [0]
    
    for k in ks:
        if k == 1: continue
        model = KMeans(n_clusters = k, random_state = 0)
        model.fit(X = X)
        cluster = model.predict(X = X)
        silwidth = silhouette_score(X = X, labels = cluster)
        result.append(silwidth)
    
    sns.lineplot(x = ks, 
                 y = result, 
                 marker = 'o', 
                 linestyle = '-', 
                 linewidth = 1)
    
    plt.xticks(ticks = ks)
    
    plt.title(label = 'Silhouette Width', 
              fontdict = {'fontweight': 'bold'})
    
    plt.xlabel(xlabel = 'Number of clusters')
    
    plt.ylabel(ylabel = 'Silhouette Width Average');


## End of Document
