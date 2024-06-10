# Apex Live Overlay

## Setup

Please follow the instructions at <https://apexliveapi.com/docs/quickstart/python/>.
You don't need to re-run `protoc`.

## Status
- [x] Live-update (test by `emulate.py` for short term and `emulate-once.py` for long term)
- [ ] Test in Apex Legend (I need my friend to test it b/c I run Apex with Steam error on my PC)
- [ ] Show rank and score from DGS API
- [ ] Calculate rank and score (Unknown Implementability)
- [ ] Improve project structure

## Run

1. Install the [Teko Font](https://fonts.google.com/specimen/Teko) (at `font/Teko-VariableFont_wght.ttf`).
2. Open a terminal and run:
    ```bash
    python main.py
    ```
3. Open another terminal and run:
    ```bash
    python -m http.server 8000
    ```
4. Open your browser and navigate to `127.0.0.1:8000`.
5. Open Developer Tools with `Ctrl-Shift-I` or `F12`.
6. Switch to the "Network" tab. You may need to access it by clicking the `>>` button.
7. Check "Disable Cache".

> "Disable Cache" can avoid refresh delay (~3-20s).  
> Users also need to install the font to the system to avoid font switching flashing.  
> (Need to consider) Maybe it can be solved by periodically adding junk comments to index.html.  

## OBS Setup

1. Keep your browser window open and not minimized.
2. Add a **Window Capture** source (this program doesn't work with a Browser source).
3. Choose the browser displaying the overlay in the "Window" field.
4. Adjust the crop parameters so that only the overlay remains (the green background is OK).
5. Disable "Capture Cursor".
6. Right-click on the source and open "Filters".
7. Add a "Color Key" with "Green" as the Key Color Type.
8. Adjust the similarity to make the green background disappear.
9. Adjust the position and size of the overlay.
10. Done!

## ScreenShot
![screenshot]()
