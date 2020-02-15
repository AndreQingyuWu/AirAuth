
# coding: utf-8

# In[88]:


import keras
import csv
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization
from keras import optimizers
import numpy as np
from keras.layers.core import Lambda
from keras import backend as K
from keras.optimizers import SGD
from keras import regularizers
from keras.models import load_model
from keras.layers.convolutional import ZeroPadding2D,Convolution2D
from keras import applications
from keras.models import Model

# In[103]:


def VGG_16(weights_path=None):
    model = Sequential()
    model.add(Convolution2D(64, (3, 3),strides=(1,1),padding='same',input_shape=(256,48,3) ,activation='relu'))
    model.add(BatchNormalization())
    
    model.add(Convolution2D(64, (3, 3), activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D((2, 2), strides=(2, 2)))
    
    model.add(Convolution2D(128, (3, 3),strides=(1,1),padding='same', activation='relu'))
    model.add(BatchNormalization())

    model.add(Convolution2D(128, (3, 3), strides=(1,1),padding='same',activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D((2, 2), strides=(2, 2)))
    
    
    model.add(Convolution2D(256, (3, 3),strides=(1,1),padding='same', activation='relu'))
    model.add(BatchNormalization())
    
    model.add(Convolution2D(256, (3, 3), strides=(1,1),padding='same',activation='relu'))
    model.add(BatchNormalization())
    
    model.add(Convolution2D(256, (3, 3),strides=(1,1),padding='same', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D((2, 2), strides=(2, 2)))

    
    model.add(Convolution2D(512, (3, 3), strides=(1,1),padding='same',activation='relu'))
    model.add(BatchNormalization())
    
    model.add(Convolution2D(512, (3, 3),strides=(1,1),padding='same', activation='relu'))
    model.add(BatchNormalization())
    
    model.add(Convolution2D(512, (3, 3),strides=(1,1),padding='same', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D((2, 2), strides=(2, 2)))
    
    
    model.add(Convolution2D(512, (3, 3), strides=(1,1),padding='same',activation='relu'))
    model.add(BatchNormalization())
    
    model.add(Convolution2D(512, (3, 3),strides=(1,1),padding='same', activation='relu'))
    model.add(BatchNormalization())
    
    model.add(Convolution2D(512, (3, 3), strides=(1,1),padding='same',activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D((2, 2), strides=(2, 2)))

    model.add(Flatten())
    model.add(Dense(2000, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dense(500, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dense(5, activation='softmax'))
    model.add(Dropout(0.4))

    if weights_path:
        model.load_weights(weights_path,by_name=True)

    return model


# In[104]:


model=VGG_16()
model.summary()


# In[ ]:

'''
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd,metrics=['accuracy'])

model.fit(x_train,y_train,epochs=1000, batch_size=64,
             validation_split=0.1, verbose=1)

model.save('model.h5')
'''

# In[31]:


import numpy as np 


'''
for i in range(0,388):
    loadData = np.load('./train_data/mouse/'+str(i)+'.npy')
    if i==0:
        a=loadData
        
    else:
        a=np.vstack((a,loadData))
        
label=np.zeros(388)


# In[33]:


for i in range(0,430):
    loadData = np.load('./train_data/other/'+str(i)+'.npy')
        
    a=np.vstack((a,loadData))
a.shape
        


# In[78]:


label1=np.array([1]*430)


# In[37]:


for i in range(0,408):
    loadData = np.load('./train_data/pull/'+str(i)+'.npy')
        
    a=np.vstack((a,loadData))
a.shape


# In[77]:


label2=np.array([2]*408)


# In[39]:


for i in range(0,76):
    loadData = np.load('./train_data/ring_finger/'+str(i)+'.npy')
        
    a=np.vstack((a,loadData))
a.shape


# In[76]:


label3=np.array([3]*76)


# In[41]:


for i in range(0,375):
    loadData = np.load('./train_data/type/'+str(i)+'.npy')
        
    a=np.vstack((a,loadData))
a.shape


# In[84]:


label4=np.array([4]*375)


# In[57]:


label=label.astype(int)
label


# In[94]:


labelappend =np.append(label,label1)
labelappend = np.append(labelappend,label2)


labelappend = np.append(labelappend,label3)



labelappend = np.append(labelappend,label4)
labelappend.shape


# In[93]:


b=a.reshape(1677,256,48,3)


# In[95]:

from keras.utils import to_categorical
state = np.random.get_state()
np.random.shuffle(b)
np.random.set_state(state)
np.random.shuffle(labelappend)
one_hots = to_categorical(labelappend)
f=open('data.csv','w')
csv_writer=csv.writer(f)
for i in range(1677):
    csv_writer.writerow([one_hots[i],(b[i,:,:,:]).tolist()])
f.close()

# In[101]:
'''

import sys
from keras.utils import to_categorical
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd,metrics=['accuracy'])
csv.field_size_limit(1000 * 1024 * 1024)
for j in range(40):
    print('epoch--'+str(j)+'--')
    f = open('data.csv')
    # 2. 基于文件对象构建 csv写入对象
    csv_reader = csv.reader(f)
    cnt=0
    for row in csv_reader:
        #print(row[0])
        if cnt%2==1:
            print(str(cnt))
            cnt=cnt+1
            continue
        if cnt%128==0:
            print(str(cnt))
            train_data=eval(row[1])
            train_data=np.array(train_data)
            train_data=np.expand_dims(train_data,axis=0)
            #print(train_data.shape)
            string=row[0]
            string=string.split('[')[1]
            string=string.split('.]')[0]
            string=[int(s) for s in string.split('. ') if s.isdigit()]
            train_label=[string,]
        else:
            row[1]=eval(row[1])
            row[1]=np.array(row[1])
            row[1]=np.expand_dims(row[1],axis=0)
            print(str(cnt))
            print(np.array(train_data).shape)
            print(row[1].shape)
            train_data=np.vstack((train_data,row[1]))
            string=row[0]
            string=string.split('[')[1]
            string=string.split('.]')[0]
            string=[int(s) for s in string.split('. ') if s.isdigit()]
            train_label.append(string)
        if cnt%128==126:
            train_data=train_data.reshape(64,256,48,3)
            print('cnt='+str(cnt)+'train on batch')
            singleloss=model.train_on_batch(np.array(train_data),np.array(train_label))
            print(model.metrics_names,singleloss)
        cnt=cnt+1
    # 5. 关闭文件
    f.close()
model.save('model.h5')
print('Done-----------------------------')
# In[ ]:


'''
cnt=0
for i in range(1000):
    model.train_on_batch(b[cnt:cnt+32,:,:,:],one_hots[cnt:cnt+32])
    cnt=cnt+32
    if (cnt+32)>=1677:
        cnt=0
'''
#model.fit(b,one_hots,epochs=1000, batch_size=64,
#             validation_split=0.1, verbose=1)




