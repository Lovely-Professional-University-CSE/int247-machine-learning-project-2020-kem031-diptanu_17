# This is a abstract summary classifier module building project. Overherewe took the data set which contains some textual abstract content related to some passage and we have made a
#supervised module which can predict the category of the text it belonging to.
def main():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.preprocessing import LabelEncoder
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.metrics import accuracy_score

    data=pd.read_csv('D:/Study/ML/Data/bbc-text.csv')
    print("----------------------------------------------------------Text Classifier--------------------------------------------------------\n\n")
    print("****Data Being Used!---------\n")
    print(data.head())
    print("\n")
    l=LabelEncoder()
    data['Category_Code']=l.fit_transform(data['category'])
    data.describe()
    
    print("****-----------------------Data After Adding Code for the Categories-------------------------------\n")
    print(data.head())
    print("\n")
    
    Graph= data['Category_Code'].value_counts(sort=False).plot(kind='barh')
    Graph.set_xlabel("Number Of Samples")
    Graph.set_ylabel("Category")
    plt.show()
    sns.violinplot(x="category", y="Category_Code", data=data)
    plt.show()

    print("\t****Different Labels Given to the Categories\n")
    print(data['Category_Code'].values)

    X=data['text']
    Y=data['Category_Code']
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y, test_size=0.3, random_state=4)
    cv = CountVectorizer()
    x_traincv=cv.fit_transform(X_train)
    a=x_traincv.toarray()

    print("****After Transformation Array value---\n")
    print(a)

    print("****Following value we will get when we do inverse_transform of the above mentioned array--\n")
    print(cv.inverse_transform(a[0]))

    x_testcv=cv.transform(X_test)

    mnb = MultinomialNB()


    y_train=Y_train.astype('int')

    mnb.fit(x_traincv,y_train)
    predictions=mnb.predict(x_testcv)
    print("****Model Trained And Gives Following Pridiction---\n")
    predictions

    a=accuracy_score(Y_test,predictions)
    
    print("****Accuracy Of the Model= "+str(a))
    print("\n")

main()
