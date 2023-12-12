print("SJC22MCA-2027-Georgekutty Biju\nS3MCA")
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn import metrics
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
gnb = GaussianNB()
bnb = BernoulliNB()
mnb = MultinomialNB()
gnb.fit(X_train, y_train)
bnb.fit(X_train, y_train)
mnb.fit(X_train, y_train)
y_pred_gnb = gnb.predict(X_test)
y_pred_bnb = bnb.predict(X_test)
y_pred_mnb = mnb.predict(X_test)
accuracy_gnb = metrics.accuracy_score(y_test, y_pred_gnb)
accuracy_bnb = metrics.accuracy_score(y_test, y_pred_bnb)
accuracy_mnb = metrics.accuracy_score(y_test, y_pred_mnb)
print("Gaussian Naive Bayes Accuracy:", accuracy_gnb)
print("Bernoulli Naive Bayes Accuracy (Not suitable for this dataset):", accuracy_bnb)
print("Multinomial Naive Bayes Accuracy:", accuracy_mnb)
mislabel_count_gnb = (y_test != y_pred_gnb).sum()
mislabel_count_bnb = (y_test != y_pred_bnb).sum()
mislabel_count_mnb = (y_test != y_pred_mnb).sum()
print("Number of Mislabeled Classifications((Gaussian NB):",mislabel_count_gnb)
print("Number of Mislabeled Classifications((Bernoulli NB):",mislabel_count_bnb)
print("Number of Mislabeled Classifications((Multinominal NB):",mislabel_count_mnb)
mismatch_labels_gnb=y_test[y_test != y_pred_gnb]
mismatch_labels_bnb=y_test[y_test != y_pred_bnb]
mismatch_labels_mnb=y_test[y_test != y_pred_mnb]
print("Mismatching class labels(Gaussian NB):",mismatch_labels_gnb.tolist())
print("Mismatching class labels(Bernoulli NB):",mismatch_labels_bnb.tolist())
print("Mismatching class labels(MultinominalNB):",mismatch_labels_mnb.tolist())