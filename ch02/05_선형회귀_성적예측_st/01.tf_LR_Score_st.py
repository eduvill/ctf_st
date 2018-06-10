import tensorflow as tf
tf.set_random_seed(666)

t_x = [2, 4, 6, 8]
t_y = [81, 93, 91, 97]

W = tf.Variable(tf.random_uniform([1], 0, 10, dtype=tf.float64, seed=0))
b = tf.Variable(tf.random_uniform([1], 0, 100, dtype=tf.float64, seed=0))

# Our hypothesis XW+b
hypo = t_x * W + b

# cost/loss function
cost = tf.reduce_mean(tf.square(hypo - t_y))

# Minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

# Launch the graph in a session.
sess = tf.Session()
# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())

# Fit the line
for step in range(2001):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(cost), sess.run(W), sess.run(b))

print('Predict Score => ')
#..................


