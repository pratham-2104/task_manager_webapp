import os

# Local SQLite (for testing)
SQLALCHEMY_DATABASE_URI = "sqlite:///tasks.db"

# For Azure (replace later with your Azure SQL connection string)
# Example:
# SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://username:password@servername/databasename?driver=ODBC+Driver+17+for+SQL+Server"

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "your_secret_key"
