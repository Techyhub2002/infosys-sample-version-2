from flask import Flask,render_template
app=Flask(__name__)
JOBS=[
  {
    'id':1,
    'title':'Data Scientist',
    'location':'Chennai,India',
    'salary':'Rs.7,50,000'
  },
  {
    'id':2,
    'title':'Full Stack Developer',
    'location':'Pune,India',
    'salary':'Rs.4,00,000'
  },
  {
    'id':3,
    'title':'Data Analyst',
    'location':'Mumbai,India',
    'salary':'Rs.3,50,000'
  },
  {
    'id':4,
    'title':'Data Engineer',
    'location':'Delhi,India',
    'salary':'Rs.10,00,000'
  },
  {
    'id':5,
    'title':'Software Engineer',
    'location':'Munich,Germany',
    'salary':'€35000'
  },
]
@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name='Infosys')
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
print(__name__)
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)
