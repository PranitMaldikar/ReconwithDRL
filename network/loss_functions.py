# Author: Aqeel Anwar(ICSRL)
# Created: 2/22/2019, 4:57 PM
# Email: aqeel.anwar@gatech.edu
import numpy as np
import tensorflow as tf


def huber_loss(X, Y):
    err = X - Y
    loss = tf.where(tf.abs(err) < 1.0, 0.5 * tf.square(err), tf.abs(err) - 0.5)
    loss = tf.reduce_sum(loss)

    return loss


def mse_loss(X, Y):
    err = X - Y
    return tf.reduce_sum(tf.square(err))

def kl_loss(y_true,y_pred):
    y_true = tf.clip_by_value(y_true, 0, 1)
    y_pred = tf.clip_by_value(y_pred, 0, 1)
    return tf.reduce_sum(y_true * tf.log(y_true / y_pred))



