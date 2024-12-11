from keras.layers import Dense
from keras.models import Sequential

def fit_compile_0(capas, x, y):
 
    model=Sequential()
    model.add(Dense(capas[0], activation='relu',input_dim=2))
    for i in range(1,len(capas)-2):
        model.add(Dense(capas[i], activation='relu'))

    model.add(Dense(capas[-1], activation='sigmoid'))
    model.compile(loss='mean_squared_error')
    
    model.fit(x, y,epochs=40) 

    return model



def fit_compile_1(capas, x, y, temporadas=40):
 
    model=Sequential()
    model.add(Dense(capas[0], activation='relu',input_dim=2))
    for i in range(1,len(capas)-2):
        model.add(Dense(capas[i], activation='relu'))

    model.add(Dense(capas[-1], activation='sigmoid'))
    model.compile(loss='mean_squared_error')
    
    model.fit(x, y,epochs=temporadas) 

    return model

