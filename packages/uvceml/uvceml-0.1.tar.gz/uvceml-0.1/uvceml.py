import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import warnings
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_selection import mutual_info_classif
from collections import Counter
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator as MLE
from pgmpy.inference import VariableElimination


# ANN function
def ANN():
    input_data = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
    target_output = np.array(([92], [86], [89]), dtype=float)
    input_data = input_data / np.amax(input_data, axis=0)
    target_output = target_output / 100

    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(x):
        return x * (1 - x)

    epochs = 1000
    learning_rate = 0.2
    num_input_neurons = 2
    num_hidden_neurons = 3
    num_output_neurons = 1

    weights_hidden = np.random.uniform(size=(num_input_neurons, num_hidden_neurons))
    bias_hidden = np.random.uniform(size=(1, num_hidden_neurons))

    weights_output = np.random.uniform(size=(num_hidden_neurons, num_output_neurons))
    bias_output = np.random.uniform(size=(1, num_output_neurons))

    for epoch in range(epochs):
        hidden_layer_input = np.dot(input_data, weights_hidden) + bias_hidden
        hidden_layer_activation = sigmoid(hidden_layer_input)
        output_layer_input = np.dot(hidden_layer_activation, weights_output) + bias_output
        predicted_output = sigmoid(output_layer_input)

        error_output_layer = target_output - predicted_output
        output_gradient = sigmoid_derivative(predicted_output)
        delta_output = error_output_layer * output_gradient

        error_hidden_layer = delta_output.dot(weights_output.T)
        hidden_layer_gradient = sigmoid_derivative(hidden_layer_activation)
        delta_hidden = error_hidden_layer * hidden_layer_gradient

        weights_output += hidden_layer_activation.T.dot(delta_output) * learning_rate
        bias_output += np.sum(delta_output, axis=0, keepdims=True) * learning_rate
        weights_hidden += input_data.T.dot(delta_hidden) * learning_rate
        bias_hidden += np.sum(delta_hidden, axis=0, keepdims=True) * learning_rate

    print("Normalized Input Data: \n" + str(input_data))
    print("Actual Output (Target): \n" + str(target_output))
    print("Predicted Output: \n", predicted_output)


# Bayesian Network function
def bayes_network(inputfile):
    warnings.filterwarnings('ignore')
    heart_disease = pd.read_csv(inputfile)

    model = BayesianModel([
        ('age', 'trestbps'),
        ('age', 'fbs'),
        ('sex', 'trestbps'),
        ('exang', 'trestbps'),
        ('trestbps', 'heartdisease'),
        ('fbs', 'heartdisease'),
        ('heartdisease', 'restecg'),
        ('heartdisease', 'thalach'),
        ('heartdisease', 'chol')
    ])
    model.fit(heart_disease, estimator=MLE)

    print(model.get_cpds('sex'))

    HeartDisease_infer = VariableElimination(model)
    q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'age': 29, 'sex': 0, 'fbs': 1})
    print(q)


# Candidate Elimination function
def candidate(inputfile):
    with open(inputfile) as f:
        csv_file = csv.reader(f)
        data = list(csv_file)

    specific = data[1][:-1]
    general = [['?' for _ in range(len(specific))] for _ in range(len(specific))]

    for i in range(1, len(data)):
        if data[i][-1] == "Yes":
            for j in range(len(specific)):
                if data[i][j] != specific[j]:
                    specific[j] = "?"
                    general[j][j] = "?"
        elif data[i][-1] == "No":
            for j in range(len(specific)):
                if data[i][j] != specific[j]:
                    general[j][j] = specific[j]
                else:
                    general[j][j] = '?'

        print("\nStep " + str(i) + " of Candidate Elimination Algorithm")
        print("Specific Hypothesis:", specific)
        print("General Hypothesis:", general)

    gh = [g for g in general if any(val != '?' for val in g)]

    print("\nFinal Specific Hypothesis:\n", specific)
    print("\nFinal General Hypothesis:\n", gh)


# Find-S function
def find_s(inputfile):
    attributes = [['Sunny', 'Rainy'], ['Warm', 'Cold'], ['Normal', 'High'], ['Strong', 'Weak'], ['Warm', 'Cool'], ['Same', 'Change']]
    num_attributes = len(attributes)

    print("\nThe most general hypothesis: ['?', '?', '?', '?', '?', '?']\n")
    print("The most specific hypothesis: ['0', '0', '0', '0', '0', '0']\n")

    a = []
    with open(inputfile, 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            a.append(row)
            print(row)

    hypothesis = ['0'] * num_attributes
    for j in range(num_attributes):
        hypothesis[j] = a[0][j]

    for i in range(len(a)):
        if a[i][num_attributes] == 'Yes':
            for j in range(num_attributes):
                if a[i][j] != hypothesis[j]:
                    hypothesis[j] = '?'

        print("For Training Example No :{0}, the hypothesis is: ".format(i), hypothesis)

    print("\nThe Maximally Specific Hypothesis for the given Training Examples:\n")
    print(hypothesis)


# ID3 Decision Tree function
def ID3(inputfile):
    def ID3_decision_tree(data_frame, target_attribute, attributes, default_class=None):
        class_counts = Counter(x for x in data_frame[target_attribute])
        if len(class_counts) == 1:
            return next(iter(class_counts))
        elif data_frame.empty or (not attributes):
            return default_class
        else:
            gains = mutual_info_classif(data_frame[attributes], data_frame[target_attribute], discrete_features=True)
            index_of_max_gain = gains.tolist().index(max(gains))
            best_attribute = attributes[index_of_max_gain]
            decision_tree = {best_attribute: {}}
            remaining_attributes = [i for i in attributes if i != best_attribute]

            for attribute_value, subset_data in data_frame.groupby(best_attribute):
                sub_tree = ID3_decision_tree(subset_data, target_attribute, remaining_attributes, default_class)
                decision_tree[best_attribute][attribute_value] = sub_tree

            return decision_tree

    data_frame = pd.read_csv(inputfile)
    attributes = data_frame.columns.tolist()
    attributes.remove("Target")

    for col_name in data_frame.select_dtypes("object"):
        data_frame[col_name], _ = data_frame[col_name].factorize()

    print(data_frame)
    tree = ID3_decision_tree(data_frame, "Target", attributes)
    pprint(tree)


# Naive Bayes function
def NaiveBayes(inputfile):
    data = pd.read_csv(inputfile)
    features = data.iloc[:, :-1]
    target = data.iloc[:, -1]

    label_encoder_outlook = LabelEncoder()
    label_encoder_temperature = LabelEncoder()
    label_encoder_humidity = LabelEncoder()
    label_encoder_wind = LabelEncoder()

    features['Outlook'] = label_encoder_outlook.fit_transform(features['Outlook'])
    features['Temperature'] = label_encoder_temperature.fit_transform(features['Temperature'])
    features['Humidity'] = label_encoder_humidity.fit_transform(features['Humidity'])
    features['Wind'] = label_encoder_wind.fit_transform(features['Wind'])

    label_encoder_play_tennis = LabelEncoder()
    target = label_encoder_play_tennis.fit_transform(target)

    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.20)
    naive_bayes_classifier = GaussianNB()
    naive_bayes_classifier.fit(X_train, y_train)

    predictions = naive_bayes_classifier.predict(X_test)
    accuracy = accuracy_score(predictions, y_test)

    print("Model Accuracy:", accuracy)


# Local Weighted Regression function
def regression(inputfile):
    def calculate_weights(point, features_matrix, bandwidth):
        num_samples, num_features = np.shape(features_matrix)
        weights = np.asmatrix(np.eye(num_samples))
        for j in range(num_samples):
            difference = point - features_matrix[j]
            weights[j, j] = np.exp(difference * difference.T / (-2.0 * bandwidth ** 2))
        return weights

    data = pd.read_csv(inputfile)
    m = np.array(data.X)
    y = np.array(data.Y)
    n = len(m)
    mean_x = np.mean(m)
    mean_y = np.mean(y)
    ss_xy = np.sum(m * y) - n * mean_x * mean_y
    ss_xx = np.sum(m * m) - n * mean_x * mean_x
    b_1 = ss_xy / ss_xx
    b_0 = mean_y - b_1 * mean_x
    print(b_1, b_0)

    plt.scatter(m, y, color='blue')
    plt.plot(m, b_0 + b_1 * m, color='red')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


# K-Means function
def k_means():
    iris = datasets.load_iris()
    X = iris.data[:, :4]
    y = iris.target

    estimator = KMeans(n_clusters=3)
    estimator.fit(X)

    y_kmeans = estimator.predict(X)
    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

    centers = estimator.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75)
    plt.show()


# KNN function
def knn():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    knn_classifier = KNeighborsClassifier(n_neighbors=3)
    knn_classifier.fit(X_train, y_train)

    y_pred = knn_classifier.predict(X_test)
    accuracy = np.mean(y_pred == y_test)

    print(f"KNN Accuracy: {accuracy}")
