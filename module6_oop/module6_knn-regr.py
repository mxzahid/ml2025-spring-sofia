from module6_mod import KnnRegresser

def main():
    knnr = KnnRegresser()
    n = int(input("Enter N (number of points): "))
    if n <= 0:
        print("N must be a positive integer.")
        return
    
    k = int(input("Enter k (number of neighbors): "))
    if k <= 0:
        print("k must be a positive integer.")
        return
    
    x_values = []
    y_values = []
    
    for i in range(n):
        x = float(input(f"Enter x coordinate for point {i+1}: "))
        y = float(input(f"Enter y coordinate for point {i+1}: "))
        x_values.append(x)
        y_values.append(y)
    
    knnr.add_points(x_values, y_values)
    
    x_query = float(input("Enter X value to predict: "))
    result = knnr.predict(x_query, k)
    print(f"Predicted Y value: {result}")
            

if __name__ == "__main__":
    main()

