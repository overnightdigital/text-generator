# 1. Install flask and python-dotenv and what it is good for / Explain imports how they work
# 2. Explain .env and .flaskenv and create them
# 3. Explain the init file how it works


import fire
import json
import os
import numpy as np
import tensorflow as tf
# import model, sample, encoder
# 17. Change imports in generator 
from text_generator import model
from text_generator import sample
from text_generator import encoder

class AI:
    def generate_text(self, input_text):
        model_name='117M_TRAINED'
        seed=None
        nsamples=1
        batch_size=1
        length=150
        temperature=1
        top_k=40
        top_p=0.0

        self.response = ""

        if batch_size is None:
            batch_size = 1
        assert nsamples % batch_size == 0

        enc = encoder.get_encoder(model_name)
        hparams = model.default_hparams()
        cur_path = os.path.dirname(__file__) + "/models" + "/" + model_name
        with open(cur_path + "/hparams.json") as f:
            hparams.override_from_dict(json.load(f))

        if length is None:
            length = hparams.n_ctx // 2
        elif length > hparams.n_ctx:
            raise ValueError("Can't get samples longer than window size: %s" % hparams.n_ctx)

        # What is a TensorFlow Session?
        # A graph defines the computation. It doesn’t compute anything, it doesn’t hold any values, it just defines 
        # the operations that you specified in your code.
        # A session allows to execute graphs or part of graphs. It allocates resources (on one or more machines) 
        # for that and holds the actual values of intermediate results and variables.
        with tf.Session(graph=tf.Graph()) as sess:
            context = tf.placeholder(tf.int32, [batch_size, None])
            np.random.seed(seed)
            tf.set_random_seed(seed)
            output = sample.sample_sequence(
                hparams=hparams, length=length,
                context=context,
                batch_size=batch_size,
                temperature=temperature, top_k=top_k, top_p=top_p
            )

            saver = tf.train.Saver()
            ckpt = tf.train.latest_checkpoint(cur_path)
            saver.restore(sess, ckpt)

            context_tokens = enc.encode(input_text)
            print("Title: " + input_text)
            generated = 0
            for _ in range(nsamples // batch_size):
                out = sess.run(output, feed_dict={
                    context: [context_tokens for _ in range(batch_size)]
                })[:, len(context_tokens):]
                for i in range(batch_size):
                    generated += 1
                    text = enc.decode(out[i])
                    self.response = text

        return self.response

ai = AI()
#text = ai.generate_text("The Jedi")
#print(text)
# Table of Contents
# 1. - X.
