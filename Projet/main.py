import tensorflow as tf
from tensorflow.contrib import rnn
import numpy as np
# import ffmpeg


from util.util import print_progress
from util.create_dataset import create_dataset, get_batch
from util.midi_manipulation import noteStateMatrixToMidi

min_song_length  = 128
encoded_songs    = create_dataset(min_song_length)

NUM_SONGS = len(encoded_songs)
print(str(NUM_SONGS) + " total songs to learn from")
print(encoded_songs[0].shape)

input_size       = encoded_songs[0].shape[1]   # The number of possible MIDI Notes
output_size      = input_size                  # Same as input size
hidden_size      = 256                     # Number of neurons in hidden layer

learning_rate    = 0.001 # Learning rate of the model
training_steps   = 2000 # Number of batches during training
batch_size           = 128 # Number of songs per batch
time_steps          = 30    # Length of song snippet -- this is what is fed into the model

assert time_steps < min_song_length

input_placeholder_shape = [None, time_steps, input_size]
output_placeholder_shape = [None, output_size]

input_vec  = tf.placeholder("float", input_placeholder_shape)
output_vec = tf.placeholder("float", output_placeholder_shape)

weights = tf.Variable(tf.random_normal([hidden_size, output_size]))

biases = tf.Variable(tf.random_normal([output_size]))


def recurrent_neurons_network(input_vec_param, weights_param, biases_param):
    """
    @param input_vec_param: (tf.placeholder) The input vector's placeholder
    @param weights_param: (tf.Variable) The weights variable
    @param biases_param: (tf.Variable) The bias variable
    @return: The RNN graph that will take in a tensor list of shape (batch_size, time_steps, input_size)
    and output tensors of shape (batch_size, output_size)
    """
    input_vec_param = tf.unstack(input_vec_param, time_steps, 1)

    lstm_cell = tf.nn.rnn_cell.LSTMCell(hidden_size)

    outputs, states =tf.nn.static_rnn(lstm_cell, input_vec_param, dtype=tf.float32)
    recurrent_net = (tf.matmul(outputs[-1], weights_param) + biases_param)

    prediction_note = tf.nn.softmax(recurrent_net)

    return recurrent_net, prediction_note

logits, prediction = recurrent_neurons_network(input_vec, weights, biases)

loss_op = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits, labels=output_vec))

optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
train_op = optimizer.minimize(loss_op)

true_note = tf.argmax(output_vec,1)
pred_note = tf.argmax(prediction,1)
correct_pred = tf.equal(pred_note, true_note)

accuracy_op = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

init = tf.global_variables_initializer()

sess = tf.InteractiveSession()

sess.run(init)

display_step = 100
for step in range(training_steps):
    batch_x,batch_y  = get_batch(encoded_songs, batch_size, time_steps, input_size, output_size)

    feed_dict = {
        input_vec: batch_x,
        output_vec: batch_y
    }
    sess.run(train_op, feed_dict=feed_dict)

    if step % display_step == 0 or step == 1:
        loss, acc = sess.run([loss_op, accuracy_op], feed_dict=feed_dict)
        suffix = "\nStep " + str(step) + ", Minibatch Loss= " + \
                 "{:.4f}".format(loss) + ", Training Accuracy= " + \
                 "{:.3f}".format(acc)

        print_progress(step, training_steps, barLength=50, suffix=suffix)

GEN_SEED_RANDOMLY = True
if GEN_SEED_RANDOMLY:
    ind = np.random.randint(NUM_SONGS)
else:
    ind = 41
gen_song = encoded_songs[ind][:time_steps].tolist()

for i in range(500):
    seed = np.array([gen_song[-time_steps:]])
    predict_probs = sess.run(prediction, feed_dict={input_vec:seed})

    played_notes = np.zeros(output_size)
    sampled_note = np.random.choice(range(output_size), p=predict_probs[0])
    played_notes[sampled_note] = 1
    gen_song.append(played_notes)

noteStateMatrixToMidi(gen_song, name= "E:\WPy3670\Projet\generated\gen_song_0")
# noteStateMatrixToMidi(encoded_songs[ind], name="E:\WPy3670\Projet\generated\base_song_0")
print("\nSaved generated song! seed ind: {}".format(ind))

# ffmpeg.input("E:\WPy3670\Projet\generated\gen_song_0.mid").output("E:\WPy3670\Projet\generated\output.mp3").run()

# ..\Projet\ffmpeg -i "E:\WPy3670\Projet\generated\gen_song_0.mid" -vn -ar 44100 -ac 2 -ab 192k -f mp3 "E:\WPy3670\Projet\generated\output.mp3"