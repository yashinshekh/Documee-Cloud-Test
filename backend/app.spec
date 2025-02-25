# app.spec

# Import PyInstaller modules
# The main part is the Analysis, which is responsible for finding the files that need to be packaged
from PyInstaller.utils.hooks import collect_all

# Adjust the path to the location of your app.py script
a = Analysis(
    ['app.py'],
    pathex=['.'],  # Current directory
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher_module=None,
    noarchive=False
)

# Adding additional files if necessary, like templates, static files, etc.
# For example, if you have static files or templates in a folder, you should add them here.
# a.datas += collect_all('flask')

# The PYZ is the zipped Python bytecode module
pyz = PYZ(a.pure, a.zipped_data)

# The EXE step creates the executable
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='flask_app',  # Name of your executable
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # Optionally use UPX to compress the executable
    console=True,  # Since it's a console app (Flask server)
)

# If you're using any additional packaging configurations (e.g., setting up the app icon), you can modify this part
