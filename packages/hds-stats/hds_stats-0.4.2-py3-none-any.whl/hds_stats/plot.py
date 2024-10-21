
# 집단별 상자 수염 그림을 그리는 함수
def box_group(data, x: str, y: str, pal: list = None) -> None:
    '''
    이 함수는 범주형 변수(x축)에 따라 연속형 변수(y축)의 상자 수염 그림을 그립니다.
    상자에 빨간 점은 해당 범주의 평균이며, 가로 직선은 전체 평균입니다.
    
    매개변수:
        data: 데이터프레임을 지정합니다.
        x: 범주형 변수명을 문자열로 지정합니다.
        y: 연속형 변수명을 문자열로 지정합니다.
        pal: 팔레트를 리스트로 지정합니다.
    
    반환값:
        그래프 외에 반환하는 객체는 없습니다.
    '''
    import numpy as np
    import pandas as pd
    from scipy import stats
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    avg = data.groupby(by = x)[y].mean()
    
    sns.boxplot(
        data = data, 
        x = x, 
        y = y, 
        hue = x, 
        order = avg.index, 
        palette = pal, 
        flierprops = {
            'marker': 'o', 
            'markersize': 3, 
            'markerfacecolor': 'pink',
            'markeredgecolor': 'red', 
            'markeredgewidth': 0.2
        }, 
        linecolor = '0.5',
        linewidth = 0.5
    )
    
    # sns.scatterplot(
    #     data = avg, 
    #     x = avg.index, 
    #     y = avg[y], 
    #     color = 'red', 
    #     s = 30, 
    #     edgecolor = 'black', 
    #     linewidth = 0.5
    # )
    
    plt.axhline(
        y = data[y].mean(), 
        color = 'red', 
        linewidth = 0.5, 
        linestyle = '--'
    )
    
    for i, v in enumerate(avg):
        plt.text(x = i, 
                 y = v, 
                 s = f'{v:,.2f}', 
                 ha = 'center', 
                 va = 'center',
                 fontsize = 6, 
                 fontweight = 'bold')
    
    plt.title(label = f'{x} 범주별 {y}의 평균 비교', 
              fontdict = {'fontweight': 'bold'});


# 두 연속형 변수로 산점도를 그리는 함수
def scatter(data, x: str, y: str, color: str = '0.3') -> None:
    '''
    이 함수는 두 연속형 변수의 산점도를 그립니다.
    
    매개변수:
        data: 데이터프레임을 지정합니다.
        x: 원인이 되는 연속형 변수명을 문자열로 지정합니다.
        y: 결과가 되는 연속형 변수명을 문자열로 지정합니다.
        color: 점의 채우기 색을 문자열로 지정합니다.(기본값: '0.3')
    
    반환값:
        그래프 외에 반환하는 객체는 없습니다.
    '''
    import numpy as np
    import pandas as pd
    from scipy import stats
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    sns.scatterplot(
        data = data, 
        x = x, 
        y = y, 
        color = color
    )
    
    plt.title(label = f'{x}와(과) {y}의 관계', 
              fontdict = {'fontweight': 'bold'});


# 두 연속형 변수로 산점도와 회귀직선을 그리는 함수
def regline(data, x: str, y: str, color: str = '0.3', size: int = 15) -> None:
    '''
    이 함수는 두 연속형 변수의 산점도에 회귀직선을 그립니다.
    
    매개변수:
        data: 데이터프레임을 지정합니다.
        x: 원인이 되는 연속형 변수명을 문자열로 지정합니다.
        y: 결과가 되는 연속형 변수명을 문자열로 지정합니다.
        color: 점의 채우기 색을 문자열로 지정합니다.(기본값: '0.3')
        size: 점의 크기를 정수로 지정합니다.(기본값: 15)
    
    반환값:
        그래프 외에 반환하는 객체는 없습니다.
    '''
    import numpy as np
    import pandas as pd
    from scipy import stats
    import seaborn as sns
    import matplotlib.pyplot as plt
        
    sns.regplot(
        data = data, 
        x = x, 
        y = y, 
        ci = None, 
        scatter_kws = {
            'facecolor': color, 
            'edgecolor': '1', 
            's': size, 
            'alpha': 0.2
        },
        line_kws = {
            'color': 'red', 
            'linewidth': 1.5
        }
    )
    
    # x_min = data[x].min()
    # x_max = data[x].max()
    # plt.xlim(x_min * 0.9, x_max * 1.1)
    
    plt.title(label = f'{x}와(과) {y}의 관계', 
              fontdict = {'fontweight': 'bold'});


# 범주형 변수의 도수로 막대 그래프를 그리는 함수
def bar_freq(data, x: str, color: str = None, pal: list = None) -> None:
    '''
    이 함수는 범주형 변수의 도수를 내림차순 정렬한 막대 그래프를 그립니다.
    
    매개변수:
        data: 데이터프레임을 지정합니다.
        x: 범주형 변수명을 문자열로 지정합니다.
        color: 점의 채우기 색을 문자열로 지정합니다.
        pal: 팔레트를 리스트로 지정합니다.
    
    반환값:
        그래프 외에 반환하는 객체는 없습니다.
    '''
    import numpy as np
    import pandas as pd
    from scipy import stats
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    grp = data[x].value_counts()
    
    v_max = grp.values.max()
    
    space = np.ceil(v_max * 0.01)
    
    sns.countplot(
        data = data, 
        x = x, 
        hue = x, 
        order = grp.index, 
        color = color, 
        palette = pal
    )
    
    for i, v in enumerate(grp):
        plt.text(
            x = i, 
            y = v + space, 
            s = v, 
            ha = 'center', 
            va = 'bottom', 
            c = 'black', 
            fontsize = 8, 
            fontweight = 'bold'
        )
    
    plt.ylim(0, v_max * 1.2)
    
    plt.title(label = '목표변수의 범주별 도수 비교', 
              fontdict = {'fontweight': 'bold'});


# 범주형 변수를 소그룹으로 나누고 도수로 펼친 막대 그래프를 그리는 함수
def bar_dodge_freq(data, x: str, g: str, pal: list = None) -> None:
    '''
    이 함수는 범주형 변수를 소그룹으로 나누고 도수로 펼친 막대 그래프를 그립니다.
    
    매개변수:
        data: 데이터프레임을 지정합니다.
        x: 범주형 변수명을 문자열로 지정합니다.
        g: x를 소그룹으로 나눌 범주형 변수명을 문자열로 지정합니다.
        pal: 팔레트를 리스트로 지정합니다.
    
    반환값:
        그래프 외에 반환하는 객체는 없습니다.
    '''
    import numpy as np
    import pandas as pd
    from scipy import stats
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    grp = data.groupby(by = [x, g]).count().iloc[:, 0]
    
    v_max = grp.values.max()
    
    space = np.ceil(v_max * 0.01)
    
    sns.countplot(
        data = data, 
        x = x, 
        hue = g, 
        order = grp.index.levels[0], 
        hue_order = grp.index.levels[1], 
        palette = pal
    )
    
    for i, v in enumerate(grp):
        if i % 2 == 0:
            i = i/2 - 0.2
        else:
            i = (i-1)/2 + 0.2
        plt.text(
            x = i, 
            y = v + space, 
            s = v, 
            ha = 'center', 
            va = 'bottom', 
            fontsize = 8, 
            fontweight = 'bold'
        )
    
    plt.ylim(0, v_max * 1.2)
    
    plt.title(label = f'{x}의 범주별 {g}의 도수 비교', 
              fontdict = {'fontweight': 'bold'})
    
    plt.legend(loc = 'center left', 
               bbox_to_anchor = (1, 0.5), 
               fontsize = 8);


# 범주형 변수를 소그룹으로 나누고 도수로 쌓은 막대 그래프를 그리는 함수
def bar_stack_freq(data, x: str, g: str, kind: str = 'bar', pal: list = None) -> None:
    '''
    이 함수는 범주형 변수를 소그룹으로 나누고 도수로 쌓은 막대 그래프를 그립니다.
    
    매개변수:
        data: 데이터프레임을 지정합니다.
        x: 범주형 변수명을 문자열로 지정합니다.
        g: x를 소그룹으로 나눌 범주형 변수명을 문자열로 지정합니다.
        kind: 막대 그래프의 종류를 'bar' 또는 'barh'로 지정합니다.(기본값: 'bar')
        pal: 팔레트를 리스트로 지정합니다.
    
    반환값:
        그래프 외에 반환하는 객체는 없습니다.
    '''
    import numpy as np
    import pandas as pd
    from scipy import stats
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    p = data[g].unique().size
    
    pv = pd.pivot_table(
        data = data, 
        index = x, 
        columns = g, 
        aggfunc = 'count'
    )
    
    pv = pv.iloc[:, 0:p].sort_index()
    
    pv.columns = pv.columns.droplevel(level = 0)
    
    pv.columns.name = None
    
    pv = pv.reset_index()
    
    cols = pv.columns[1:]
    
    cumsum = pv[cols].cumsum(axis = 1)
    
    if type(pal) == list:
        pal = sns.set_palette(sns.color_palette(pal))
    
    pv.plot(
        x = x, 
        kind = kind, 
        stacked = True, 
        rot = 0, 
        legend = 'reverse', 
        colormap = pal
    )
    
    if kind == 'bar':
        for col in cols:
            for i, (v1, v2) in enumerate(zip(cumsum[col], pv[col])):
                plt.text(
                    x = i, 
                    y = v1 - v2/2, 
                    s = v2, 
                    ha = 'center', 
                    va = 'center', 
                    c = 'black', 
                    fontsize = 8, 
                    fontweight = 'bold'
                );
    elif kind == 'barh':
        for col in cols:
            for i, (v1, v2) in enumerate(zip(cumsum[col], pv[col])):
                plt.text(
                    x = v1 - v2/2, 
                    y = i, 
                    s = v2, 
                    ha = 'center', 
                    va = 'center', 
                    c = 'black', 
                    fontsize = 8, 
                    fontweight = 'bold'
                )

    plt.title(label = f'{x}의 범주별 {g}의 도수 비교', 
              fontweight = 'bold')
    
    plt.legend(loc = 'center left', 
               bbox_to_anchor = (1, 0.5), 
               fontsize = 8);


# 범주형 변수를 소그룹으로 나누고 상대도수로 쌓은 막대 그래프를 그리는 함수
def bar_stack_prop(data, x: str, g: str, kind: str = 'bar', pal: list = None) -> None:
    '''
    이 함수는 범주형 변수를 소그룹으로 나누고 상대도수로 쌓은 막대 그래프를 그립니다.
    
    매개변수:
        data: 데이터프레임을 지정합니다.
        x: 범주형 변수명을 문자열로 지정합니다.
        g: x를 소그룹으로 나눌 범주형 변수명을 문자열로 지정합니다.
        kind: 막대 그래프의 종류를 'bar' 또는 'barh'로 지정합니다.(기본값: 'bar')
        pal: 팔레트를 리스트로 지정합니다.
    
    반환값:
        그래프 외에 반환하는 객체는 없습니다.
    '''
    import numpy as np
    import pandas as pd
    from scipy import stats
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    p = data[g].unique().size
    
    pv = pd.pivot_table(
        data = data, 
        index = x, 
        columns = g, 
        aggfunc = 'count'
    )
    
    pv = pv.iloc[:, 0:p].sort_index()
    
    pv.columns = pv.columns.droplevel(level = 0)
    
    pv.columns.name = None
    
    pv = pv.reset_index()
    
    cols = pv.columns[1:]
    
    rowsum = pv[cols].apply(func = sum, axis = 1)
    
    pv[cols] = pv[cols].div(rowsum, 0) * 100
    
    cumsum = pv[cols].cumsum(axis = 1)
    
    if type(pal) == list:
        pal = sns.set_palette(sns.color_palette(pal))
        
    pv.plot(
        x = x, 
        kind = kind, 
        stacked = True, 
        rot = 0, 
        legend = 'reverse', 
        colormap = pal, 
        mark_right = True
    )
    
    if kind == 'bar':
        for col in cols:
            for i, (v1, v2) in enumerate(zip(cumsum[col], pv[col])):
                v3 = f'{np.round(v2, 1)}%'
                plt.text(
                    x = i, 
                    y = v1 - v2/2, 
                    s = v3, 
                    ha = 'center', 
                    va = 'center', 
                    c = 'black', 
                    fontsize = 8, 
                    fontweight = 'bold'
                );
    elif kind == 'barh':
        for col in cols:
            for i, (v1, v2) in enumerate(zip(cumsum[col], pv[col])):
                v3 = f'{np.round(v2, 1)}%'
                plt.text(
                    x = v1 - v2/2, 
                    y = i, 
                    s = v3, 
                    ha = 'center', 
                    va = 'center', 
                    c = 'black', 
                    fontsize = 8, 
                    fontweight = 'bold'
                )
    plt.title(label = f'{x}의 범주별 {g}의 상대도수 비교', 
              fontweight = 'bold')
    
    plt.legend(loc = 'center left', 
               bbox_to_anchor = (1, 0.5), 
               fontsize = 8);


## End of Document
