import numpy as np

class IntegerStore:
    def __init__(self):
        self.nums = []

    def add_num(self, num):
        self.nums.append(num)

    def find_num(self, target):
        if target in self.nums:
            return self.nums.index(target) + 1 #1 indexed
  
        return -1

class KnnRegresser:
    def __init__(self):
        self.feats = None
        self.labels = None
    
    def add_points(self, x_values, y_values):
        self.features = np.array(x_values).reshape(-1, 1)
        self.labels = np.array(y_values)
    
    def predict(self, x_query, k):
        if self.features is None or self.labels is None:
            print("No training data available")
            return None
            
        if k > len(self.features):
            print("k > len(self.features)")
            return None
            
        x_query = np.array([x_query]).reshape(-1, 1)
        
        distances = np.sqrt(np.sum((self.features - x_query) ** 2, axis=1))
        
        nearest_indices = np.argsort(distances)[:k]
        
        return np.mean(self.labels[nearest_indices])
