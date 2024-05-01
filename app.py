from flask import Flask, render_template, redirect, request, make_response
from pose_estimation import estimate_step_1, estimate_step_2, estimate_step_3
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = ['.jpg', '.jpeg', '.png', '.gif']

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/step1_estimation', methods=['GET', 'POST'])
def step1_estimation():
    if request.method == 'POST':
        # Check if the file was uploaded
        if 'step1_img' not in request.files:
            return render_template('step1.html', feedback="No image uploaded.")

        # Get the uploaded file
        step1_img = request.files['step1_img']

        # Check if the file is allowed
        allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif']
        if not any(step1_img.filename.lower().endswith(ext) for ext in allowed_extensions):
            return render_template('step1.html', feedback="Invalid file format.")

        # Save the uploaded file
        filename = secure_filename(step1_img.filename)
        step1_img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        step1_img.save(step1_img_path)


        # Call the estimate_step_1 function and get the feedback
        from pose_estimation import estimate_step_1  # Import the function from your pose_estimation module
        encoded_image,feedback1, feedback2 = estimate_step_1(step1_img_path)
        print(f"Image path: {step1_img_path}")

        # Render the step1.html template with the feedback
        return render_template('step1.html', feedback1=feedback1, feedback2=feedback2,processed_image=encoded_image)
        # html = render_template('step1.html', feedback1=feedback1, feedback2=feedback2, processed_image=encoded_image)
        #
        # # Create a response with the appropriate headers
        # response = make_response(html)
        # response.headers['Content-Disposition'] = 'inline'
        # response.headers['Content-Type'] = 'text/html'
        #
        # return response

        # For GET requests, render the step1.html template without feedback
    return render_template('step1.html')

    # For GET requests, render the step1.html template without feedback
    return render_template('step1.html', feedback= "no response")



@app.route('/step2_estimation', methods=['GET', 'POST'])
def step2_estimation():
    if request.method == 'POST':
        # Check if the file was uploaded
        if 'step2_img' not in request.files:
            return render_template('step2.html', feedback="No image uploaded.")

        # Get the uploaded file
        step2_img = request.files['step2_img']

        # Check if the file is allowed
        allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif']
        if not any(step2_img.filename.lower().endswith(ext) for ext in allowed_extensions):
            return render_template('step2.html', feedback="Invalid file format.")

        # Save the uploaded file
        filename = secure_filename(step2_img.filename)
        step2_img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        step2_img.save(step2_img_path)

        # Call the estimate_step_1 function and get the feedback
        from pose_estimation import estimate_step_2  # Import the function from your pose_estimation module
        encoded_image,feedback1, feedback2,feedback3 = estimate_step_2(step2_img_path)
        print(f"Image path: {step2_img_path}")

        # Render the step1.html template with the feedback
        return render_template('step2.html', feedback1= feedback1, feedback2= feedback2,feedback3=feedback3, processed_image=encoded_image)

    # For GET requests, render the step1.html template without feedback
    return render_template('step2.html', feedback1="no response")



@app.route('/step3_estimation', methods=['GET', 'POST'])
def step3_estimation():
    if request.method == 'POST':
        # Check if the file was uploaded
        if 'step3_img' not in request.files:
            return render_template('step3.html', feedback="No image uploaded.")

        # Get the uploaded file
        step3_img = request.files['step3_img']

        # Check if the file is allowed
        allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif']
        if not any(step3_img.filename.lower().endswith(ext) for ext in allowed_extensions):
            return render_template('step3.html', feedback="Invalid file format.")

        # Save the uploaded file
        filename = secure_filename(step3_img.filename)
        step3_img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        step3_img.save(step3_img_path)

        # Call the estimate_step_1 function and get the feedback
        from pose_estimation import estimate_step_3  # Import the function from your pose_estimation module
        # feedback1, feedback2,feedback3 = estimate_step_3(step3_img_path)
        encoded_image,feedback1,feedback2,feedback3 = estimate_step_3(step3_img_path)
        print(f"Image path: {step3_img_path}")

        # Render the step1.html template with the feedback
        return render_template('step3.html', feedback1= feedback1,feedback2= feedback2,feedback3=feedback3,processed_image=encoded_image)

    # For GET requests, render the step1.html template without feedback
    return render_template('step3.html', feedback="no response")

if __name__ == '__main__':
    app.run(debug=True)
