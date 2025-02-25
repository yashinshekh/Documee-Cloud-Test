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
    
    ## for frontend
        1. npm run build
        2. npm install -g serve
        3. serve -s dist


# couchdb installation
    
    snap install couchdb