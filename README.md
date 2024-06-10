# Apex Live Overlay

## Status
- [x] UI
- [x] Live-update Team name (test by `emulate*.py`)
- [ ] Test in Apex Legend (I need my friend to test it b/c I run Apex with Steam error on my PC)
- [ ] Show rank and score from DGS API
- [ ] Calculate rank and score (Unknown Implementability)
- [ ] Improve project structure

## Setup

The tutorial is modified by https://apexliveapi.com/docs/quickstart/python/

1. Install [Python 3.9 or higher](https://www.python.org/downloads/windows) and Enable **Add Python to PATH** in installer
2. Click [<> Code] and [Download ZIP] and Extract it or `git clone https://github.com/YuevUwU/apex-live-overlay.git` if you have downloaded [git](https://www.git-scm.com/downloads/win)
3. Modify `team_data` to what you want to display
4. Run Terminal by tapping [Win-R] and entering `cmd`
5. Navigate to Project with `cd /path/to/apex-live-overlay`
6. Run these command:
    ```sh
    # Upgrade pip (a package-management system in Python) (Do it only once)
    python -m ensurepip --upgrade
    
    # Create Virtual Environment (Do it only once)
    python -m venv .venv
    
    # Active Virtual Enviroment
    .venv\Scripts\activate.bat
    
    # Install requirements (Do it only once)
    pip install -r requirements.txt
    ```
7. Check [Set Launch Options written in apex-liveapi-documentation](https://apexliveapi.com/docs/quickstart/python/#set-launch-options)
8. (Optional) You can update `events_pb2.py` with that tutorial or not
9. Run:
    ```sh
    python main.py
    ```
10. Create another Terminal just like Step 3
11. Run:
    ```
    # You don't need to navigate
    python -m http.server 8000
    ```

## Run

1. Install the [Teko Font](https://fonts.google.com/specimen/Teko) (at `font/Teko-VariableFont_wght.ttf`)
2. Open a terminal and run:
    ```bash
    python main.py
    ```
3. Open another terminal and run:
    ```bash
    python -m http.server 8000
    ```
4. Open your browser and navigate to `http://127.0.0.1:8000`
5. Open Developer Tools with `Ctrl-Shift-I` or `F12`
6. Switch to the "Network" tab. You may need to access it by clicking the `>>` button
7. Check "Disable Cache"

## OBS Setup

1. Keep your browser window open and not minimized
2. Add a **Window Capture** source (this program doesn't work with a Browser source)
3. Choose the browser displaying the overlay in the "Window" field
4. Adjust the crop parameters so that only the overlay remains (the green background is OK)
5. Disable "Capture Cursor"
6. Right-click on the source and open "Filters"
7. Add a "Color Key" with "Green" as the Key Color Type
8. Adjust the similarity to make the green background disappear
9. Adjust the position and size of the overlay
10. Done!

## ScreenShot

![screenshot-2024-06-10-08-09](https://github.com/YuevUwU/apex-live-overlay/assets/96368079/e697dccf-1d3e-4522-a2a7-da5bfe57d327)
> Used Image: https://tw.steelseries.com/blog/vantage-apex-legends-guide-tips-tricks-826

## Special Thanks

- [Teko Font](https://fonts.google.com/specimen/Teko)
- [zeejayym/apex-liveapi-documentation](https://github.com/zeejayym/apex-liveapi-documentation)
- [ndekopon/liveapi_playgrounds](https://github.com/ndekopon/liveapi_playgrounds)

## Difficulty

### About I chose File I/O
I have tried to use Flask and/or raw javascript, but they didn't return anything to html.  
As a last resort, I can only implement it with File I/O, so the project is not support Browser Source :persevere:

### Why I hope users install font to local
Disable Cache can avoid refresh delay (~3-20s) during idling for 2 minutes. <sup>[[ref1]](https://forum.sambapos.com/t/2nd-screen-live-js-delayed-if-pos-screen-is-idle/12540)</sup>  
Local font can avoid font switching flashes.  
Maybe it can be solved by periodically adding junk comments to index.html :thinking:  

### Why I use PY file to save data instead of JSON
~~Just want to use int as key~~  
I don't want to spend too much code on File I/O.

### Relative Import
I have tried to use `sys.path` but it was not working again, why...
Maybe pyproject.toml is the only method I can improve the project structure...<sup>[[ref2]](https://stackoverflow.com/a/50194143)</sup>
