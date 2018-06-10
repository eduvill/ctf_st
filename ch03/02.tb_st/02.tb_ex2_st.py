# tensorboard ex2
import tensorflow as tf

sess = tf.InteractiveSession()

a = tf.constant(2, name='a')
b = tf.constant(3, name='b')
x = tf.add(a, b)

....................
sess.run(x)
writer.close()
sess.close()
