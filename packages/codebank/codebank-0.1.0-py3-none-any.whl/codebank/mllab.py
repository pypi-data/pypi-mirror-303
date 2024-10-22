def one():
    print('''import numpy as np
    import pandas as pd
    df=pd.read_csv('Iris1.csv')
    df.head()
    from sklearn import tree
    from sklearn.model_selection import train_test_split
    X=df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
    Y=df['Species']
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)
    model=tree.DecisionTreeClassifier()
    model.fit(X_train,Y_train)
    print("score",model.score(X_test,Y_test))
    tree.plot_tree(model)''')
    
