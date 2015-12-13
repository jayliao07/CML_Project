from sklearn.linear_model import SGDClassifier
from training import batch_training_display

working_dir = "/Users/Kun/Desktop/Project_CML/sample/"
annotation_path = working_dir + "Annotations/"
img_parent_path = working_dir + "JPEGImages/"
target = "sheep"
input_parent_path = working_dir + "output/" + target + "/"
X_path = input_parent_path + "global_X.txt"
y_path = input_parent_path + "global_y.txt"
clf = SGDClassifier(class_weight={1:10})
threshold = 0.5

batch_training_display(input_parent_path, X_path, y_path,
        annotation_path, img_parent_path, target, clf, threshold)
