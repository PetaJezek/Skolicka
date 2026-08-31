import keras
from keras.datasets import reuters
from keras import models
from keras import layers
from keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt

def create_testing_data():
    """
    Data = a newswire represented as a sequence of integers (representing words) 
    Labels = one of 46 categories the newswire talks about
    Consider only the 10000 most often used words, vectorization produces a vector of length 10000, index i = 1 if word i is in the newswire
    One hot labels is a vector of length 46 with 1 at the position of the correct category
    """
    (train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=10000)

    train = vectorize_sequences(train_data)
    test = vectorize_sequences(test_data)
    one_hot_train_labels = to_categorical(train_labels)
    one_hot_test_labels = to_categorical(test_labels)

    # For fun, we can decode the input data to see what a newswire looks like
    #decode_input_data(train_data)

    return (train, one_hot_train_labels, test, one_hot_test_labels)

def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension), dtype=np.float32)
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results

def decode_input_data(train_data):
    word_index = reuters.get_word_index()
    reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
    # Note that our indices were offset by 3
    # because 0, 1 and 2 are reserved indices for "padding", "start of sequence", and "unknown".
    decoded_newswire = ' '.join([reverse_word_index.get(i - 3, '?') for i in train_data[0]])
    print(decoded_newswire)



def create_and_train_network(input):
    """
    Create a network with the input of size 10000, two hidden layers, and one output layer of size 46
    The output of the network is a vector of probabilities the newswire falls into the specific category
    Set aside 1000 samples for validation, use the rest for training
    """
    (train,train_labels,_,_) = input

    # specify the shape of the network
    model = models.Sequential()
    model.add(layers.Dense(500, activation='relu', input_shape=(10000,)))
    model.add(layers.Dense(500, activation='relu'))
    model.add(layers.Dense(46, activation='softmax'))

    model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

    # split input data into training set and validation set
    val_data = train[:1000]
    train_data = train[1000:]

    val_labels = train_labels[:1000]
    train_labels = train_labels[1000:]

    # train the network
    history = model.fit(train_data,
                        train_labels,
                        epochs=20,
                        batch_size=512,
                        validation_data=(val_data, val_labels))
    
    return (history,model)
 #========================================================================================================#

    #TASK 2. What happens if you use significantly fewer neurons than the output size? 

    # If we use significatnly fewer neruons (I tried 5), the training and validation simutaneously drop down. 
    # It is because the network has only five dimensions to represent all the 46 different labels, which is impossible. 

    # I also tried setting the number of hidden neurons to 1000, and the training accuracy increased.
    #  However, the validation accuracy stayed stagnant after like 7 epochs.
    # It is because the network has too much capacity and it overfits the training data (with its noise), which is not good for generalization e. g. validation/testing results plummet.
    #========================================================================================================#




def categorize_testing_set(model, input):
    """
    Use the trained model to categorize the testing set and compare the results with the expected categories
    """
    (_,_,test,test_labels) = input

    results = model.predict(test)

    # results is a vector of probabilities, we need to find the index of the highest probability to get the category
    predicted_labels = np.argmax(results, axis=1)
    expected_labels = np.argmax(test_labels, axis=1)


    wrong = 0

    for i in range(len(predicted_labels)):
        if predicted_labels[i] != expected_labels[i]:
            wrong += 1
    
    print("Number of wrong predictions: " + str(wrong) + " out of " + str(len(predicted_labels)) + " predictions")
    
    #========================================================================================================#

    #TASK 1. Are the results on the testing set more comparable to the training set or the validation set?

    # The testing set results are way more comparable to the validation set results. 
    # I think it's because the model has seen the training set but has not seen the testing/validation sets. 
  
    #========================================================================================================#

def print_graphs(history):
    """
    History contains data about the training process. It contains an entry for each metric used for both training and validation.
    Specifically, we plot loss = difference between the expected outcome and the produced outcome
    and accuracy = fraction of predictions the model got right
    """
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(1, len(loss) + 1)

    plt.plot(epochs, loss, 'bo', label='Training loss')
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

    plt.show()

    plt.clf()   # clear figure

    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

    plt.show()



if __name__ == "__main__":
    input = create_testing_data()
    (history, model) = create_and_train_network(input)

    (_, _, test, test_labels) = input
    test_loss, test_acc = model.evaluate(test, test_labels)

    print(f"Final training accuracy:   {history.history['accuracy'][-1]:.4f}")
    print(f"Final validation accuracy: {history.history['val_accuracy'][-1]:.4f}")
    print(f"Test accuracy:             {test_acc:.4f}")

    print(f"Final training loss:   {history.history['loss'][-1]:.4f}")
    print(f"Final validation loss: {history.history['val_loss'][-1]:.4f}")
    print(f"Test loss:             {test_loss:.4f}")

    print_graphs(history)
    categorize_testing_set(model, input)