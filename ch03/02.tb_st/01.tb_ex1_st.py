# tensorboard ex1
import tensorflow as tf

sess = tf.InteractiveSession()

a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a, b)

.................

sess.run(x)
.................
sess.close()
