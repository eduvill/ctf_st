# tensorboard  ex4
import tensorflow as tf

a = tf.constant(3.0, name='a')
b = tf.constant(4.0, name='b')
c = a*b

c_summary = tf.summary._____('point', c)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
	writer = tf.summary.FileWriter('/share/tb/tb4', sess.graph)  
	rst = sess.run(......)	
	...........
	writer.close()
	sess.close()
    