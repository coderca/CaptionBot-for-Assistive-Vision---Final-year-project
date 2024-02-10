from flask import Flask,render_template,request,send_from_directory
app = Flask(__name__)
import os
import keras
import numpy as np
from keras.preprocessing import image
from gtts import gTTS
 

path1 = "D:/final-year project/Flask/static/model1/"
path2 = "D:/final-year project/Flask/static/model2/"
path3 = "D:/final-year project/Flask/static/model3/"
path4 = "D:/final-year project/Flask/static/model4/"


@app.route("/")
def hello():
	return render_template('index.html')


@app.route("/Model1",methods=['GET','POST'])
def model1():
	if request.method == 'POST':
		f=request.files['file']
		f.save(os.path.join(path1,f.filename))
		p=os.path.join(path1,f.filename)
		cnn = keras.models.load_model('model4-traffic.h5')
		import numpy as np
		from keras.preprocessing import image
		test_image = image.load_img('D:/final-year project/Flask/static/model1/traffic.jpg', target_size = (64, 64))
		test_image = image.img_to_array(test_image)
		test_image = np.expand_dims(test_image, axis = 0)
		result = cnn.predict(test_image)
		if result[0][0] == 1:
			prediction = 'red'
			tts = gTTS("Traffic Signal is red,Cross the road as soon as possible")
			tts.save('D:/final-year project/Flask/static/music/1.wav')
		else:
			prediction = 'Green'
			tts = gTTS("Traffic Signal is Green, Please do not move.")
			tts.save('D:/final-year project/Flask/static/music/1.wav')
		return render_template('audio1.html')
		
	return render_template('Model1.html')

@app.route("/Model2",methods=['GET','POST'])
def model2():
	if request.method == 'POST':
		f=request.files['file']
		f.save(os.path.join(path2,f.filename))
		p=os.path.join(path2,f.filename)
		cnn = keras.models.load_model('model1-bus.h5')
		import numpy as np
		from keras.preprocessing import image
		test_image = image.load_img('D:/final-year project/Flask/static/model2/bus.jpeg', target_size = (64, 64))
		test_image = image.img_to_array(test_image)
		test_image = np.expand_dims(test_image, axis = 0)
		result = cnn.predict(test_image)
		if result[0][0] == 1:
			prediction = 'No-Rush'
			tts = gTTS("Bus is empty You can get into Bus")
			tts.save('D:/final-year project/Flask/static/music/2.wav')
		else:
			prediction = 'Rush'
			tts = gTTS("Bus is Rush Please do not get into bus")
			tts.save('D:/final-year project/Flask/static/music/2.wav')
		return render_template('audio2.html')
	return render_template('Model2.html')

@app.route("/Model3",methods=['GET','POST'])
def model3():
	if request.method == 'POST':
		f=request.files['file']
		f.save(os.path.join(path3,f.filename))
		p=os.path.join(path3,f.filename)
		cnn = keras.models.load_model('model3-person.h5')
		import numpy as np
		from keras.preprocessing import image
		test_image = image.load_img('D:/final-year project/Flask/static/model3/person.jpeg', target_size = (64, 64))
		test_image = image.img_to_array(test_image)
		test_image = np.expand_dims(test_image, axis = 0)
		result = cnn.predict(test_image)
		if result[0][0] == 1:
			prediction = 'person'
			tts = gTTS("There is  person in-front of you")
			tts.save('D:/final-year project/Flask/static/music/3.wav')
		else:
			prediction = 'No-person'
			tts = gTTS("There is No-person in-front of you")
			tts.save('D:/final-year project/Flask/static/music/5.wav')
			return render_template('audio5.html')
		return render_template('audio3.html')
	return render_template('Model3.html')

@app.route("/Model4",methods=['GET','POST'])
def model4():
	if request.method == 'POST':
		f=request.files['file']
		f.save(os.path.join(path4,f.filename))
		p=os.path.join(path4,f.filename)
		cnn = keras.models.load_model('model2-dog.h5')
		import numpy as np
		from keras.preprocessing import image
		test_image = image.load_img('D:/final-year project/Flask/static/model4/dog.jpeg', target_size = (64, 64))
		test_image = image.img_to_array(test_image)
		test_image = np.expand_dims(test_image, axis = 0)
		result = cnn.predict(test_image)
		if result[0][0] == 1:
			prediction = 'No-dog'
			tts = gTTS("There is No dog in-front of you")
			tts.save('D:/final-year project/Flask/static/music/4.wav')
		else:
			prediction = 'dog'
			tts = gTTS("There is  dog in-front of you")
			tts.save('D:/final-year project/Flask/static/music/4.wav')
		return render_template('audio4.html')
	return render_template('Model4.html')



if __name__ == '__main__':
	app.run(debug=True)
