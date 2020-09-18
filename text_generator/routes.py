from flask import Blueprint, render_template, request, redirect
from .generator import ai

generator = Blueprint('generator', __name__)

@generator.route('/')
def index():
    # 18. Now add route index 
    return render_template('index.html')

@generator.route('/analyze', methods=['POST'])
def analyze():
    # 7. Explain the render template and import and also how it finds the index
    # 8. Also explain how we need to create a template now
    title = request.form['title']
    text = ai.generate_text(title)

    return render_template('index.html', text=text)

# 11. Now lets go and train our model for text generation / Download and Extract the GPT2 Finetuning repo
# Link(https://github.com/nshepperd/gpt-2)    

# STEPS FOR TRAINING THE MODEL
# -> MOVE encode.py /train.py / train-horovod.py to the src folder
# -> pip install -r requirements.txt
# -> python download_model.py 117M
# -> MOVE models folder to src 
# -> ADD training.txt file to src Link(https://www.looper.com/162409/the-entire-star-wars-story-finally-explained/)
# -> python encode.py training.txt training.npz (encoded model which the training script will use)
# -> python train.py --dataset training.npz
# -> CREATE a new model in the models folder which is just a copy of our 117M
# -> COPY from src/checkpoints/run1 to the new copy thats 117M and overwrite the files
# -> ALSO adapt all the imports so that the right model is used(in interactive_conditional_samples)
# -> RUN with python src/interactive_conditional_samples.py --top_k 40 --model_name <our model name> --length 25 
# -> IMPORTANT NOTE THIS WILL ONLY WORK WITH TENSORFLOW !!! 1.8 !!! and not with 2.2
# -> IMPORTANT NOTE ALSO ADAPT THE train.py TO SAVE AND HAVE A MAX NUMBER OF ITERATIONS
# 12. Now that this is finished we need to think of a way to use our model in our route and return the result 
# to the index.html

# 13. Now lets use the code from the interactive code sample in our generator.py
# 14. Alos move model, smaple and encoder to the same directory