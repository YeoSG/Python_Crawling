# anaconda prompt administrator 모드에서 실행해야 동작함 

import tensorflow as tf
    
a = tf.constant(1234)
b = tf.constant(5000)

add_op = a + b

sess = tf.Session()
res = sess.run(add_op)
print(res)