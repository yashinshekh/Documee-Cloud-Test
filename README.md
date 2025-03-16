# running locally

    ## for backend ( python installation required )
        1. cd backend
        2. pip install -r requirements.txt
        3. python app.py
    
    ## for frontend ( node installation required v18/v20 )
    
        1. cd frontend
        2. npm install
        3. npm run dev


# building for production

    ## for backend
        1. pyinstaller app.spec
    
    ## for frontend ( npm install )
        1. npm run build
        2. npm install -g pm2
        3. pm2 start npm --name "next-app" -- start


# couchdb installation
    
    snap install couchdb
    curl -X PUT http://127.0.0.1:5984/_config/admins/admin -d '"admin"'
    sudo snap set couchdb admin=admin (alternative way to set admin credentials)

