import pickle

some_variable = ...

# pickle.dump
# pickle.load

with open('file.pkl', 'wb') as f:  
    pickle.dump(some_variable, f)

with open('file.pkl','rb') as f:  
    some_variable = pickle.load(f)