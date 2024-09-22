import keras.backend as K
from keras.layers import Dense, GlobalAveragePooling1D, GlobalMaxPooling1D, Flatten

def fusion(layer_channel, input, unit):
    if   layer_channel==1: return K.mean(input,axis=-1) # CAP
    elif layer_channel==2: return GlobalAveragePooling1D()(input) # GAP
    elif layer_channel==3: return K.max(input,axis=-1) # CMP
    elif layer_channel==4: return GlobalMaxPooling1D()(input) # GMP
    else: return Dense(unit)(Flatten()(input)) #NM
