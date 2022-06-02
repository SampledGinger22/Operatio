from flask import Flask, flash
app = Flask(__name__)
app.secret_key="construction"
DATABASE = 'projects_schema'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://amgbgmopfuipzx:180b1b2f359052371fd3a6584176f698e36b5590b2f72db702c2c49ee128c903@ec2-34-230-153-41.compute-1.amazonaws.com:5432/d9035k6v55o3ri'