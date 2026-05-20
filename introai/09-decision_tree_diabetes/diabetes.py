import pandas
from pathlib import Path
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
column_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'truth']
feature_columns = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']
df = pandas.read_csv("diabetes.csv")
df.columns = column_names

X = df[feature_columns]
y = df.truth

split_sizes = [num/16 for num in range(1, 16)]
print(split_sizes)
results = []
for test_size in split_sizes:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, #random_state=42
    )
    dec_tree = DecisionTreeClassifier(
        criterion='entropy',
        #random_state=42,
        max_leaf_nodes=30,
        max_depth=5,
        min_samples_split=7,
        min_samples_leaf=7,
    )
    dec_tree = dec_tree.fit(X_train, y_train)
    y_pred = dec_tree.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred, zero_division=0)
    recall = metrics.recall_score(y_test, y_pred)
    results.append({
        'test_size': test_size,
        'train_size': 1.0 - test_size,
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'model': dec_tree,
    })
    print(
        f"test_size={test_size:.3f} train_size={1 - test_size:.3f} "
        f"accuracy={accuracy:.3f} precision={precision:.3f} recall={recall:.3f}"
    )

best = max(results, key=lambda result: (result['accuracy']))
print("\nBest result:")
print(
    f" test_size={best['test_size']:.4f} train_size={best['train_size']:.4f} "
    f"accuracy={best['accuracy']:.4f} precision={best['precision']:.4f} recall={best['recall']:.4f}"
)
print("Hyperparameters:", best['model'].get_params())


plt.figure(figsize=(20, 12))
train_proportions = [result['train_size'] for result in results]
accuracies = [result['accuracy'] for result in results]
precisions = [result['precision'] for result in results]

plt.plot(train_proportions, accuracies, marker='o', markersize=8, linewidth=2, label='Accuracy', color='#1f77b4')
plt.plot(train_proportions, precisions, marker='s', markersize=8, linewidth=2, label='Precision', color='#ff7f0e')

best_idx = accuracies.index(max(accuracies))
best_train_size = train_proportions[best_idx]
best_acc = accuracies[best_idx]

plt.scatter([best_train_size], [best_acc], color='gold', s=250, edgecolor='red', zorder=5, label='Nejlepší Accuracy')

plt.annotate(f"{best_acc:.3f}", 
             (best_train_size, best_acc), 
             textcoords="offset points", 
             xytext=(0, 15), 
             ha='center', 
             fontsize=14, 
             fontweight='bold', 
             color='red')


plt.xlabel('Podíl trénovací sady (Train Size)', fontsize=12)
plt.ylabel('Skóre', fontsize=12)
plt.title('Závislost Accuracy a Precision na velikosti trénovací sady', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

graph_path = 'accuracy_precision_vs_train_size1.png'
plt.savefig(graph_path, bbox_inches='tight', dpi=600)
print(f"Saved accuracy/precision graph to: {graph_path}")

fig = plt.figure(figsize=(40, 16))
tree.plot_tree(
    best['model'],
    feature_names=feature_columns,
    class_names=['No Diabetes', 'Diabetes'],
    filled=True,
    rounded=True,
)

tree_path = 'decision_tree_best1.png'
fig.savefig(tree_path, bbox_inches='tight')
print(f"Saved best decision tree image to: {tree_path}")
