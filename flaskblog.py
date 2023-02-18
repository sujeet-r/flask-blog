from flask import Flask, render_template
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['Secret Key'] - 'ab673dde05fc9ec4dff3c84cfc540856'

posts = [
   {
      'Name' : 'Sujeet Singh',
      'Email': 'abc@xyz.com',
      'Phone': '9876543210',
      'Country': 'India'
   },
   {
      'Name' : 'John Doe',
      'Email': 'qwerty@xyz.com',
      'Phone': '1234567890',
      'Country': 'USA'
   }
]


@app.route('/')
@app.route('/home')
def home():
   return render_template('home.html', posts=posts)

@app.route('/about')
def about():
   return render_template('about.html')

if __name__ == '__main__':
   app.run(debug=True)
