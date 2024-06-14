# Apex Live Overlay

## Status

- [x] Team name display UI
- [x] Live-update Team name (test by `emulate*.py`)
- [ ] Test in Apex Legend (I need my friend to test it b/c I run Apex with Steam error on my PC)
- [ ] Show rank and score from DGS API
- [ ] Calculate rank and score (Unknown Implementability)
- [ ] Improve project structure

## Setup

The tutorial is modified by <https://apexliveapi.com/docs/quickstart/python/>

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

## OBS Setup

1. Add a Browser Source
2. Make sure "Local Files" is checked
3. [Browse] and Open `index.html` in this project. (not `templates/index.html`)
4. Press [OK]
5. Done!

## Special Thanks

- [Teko Font](https://fonts.google.com/specimen/Teko)
- [zeejayym/apex-liveapi-documentation](https://github.com/zeejayym/apex-liveapi-documentation)
- [ndekopon/liveapi_playgrounds](https://github.com/ndekopon/liveapi_playgrounds)

## Difficulty

### ~~About I chose File I/O~~

**_Solved since 0.2.0:_**: With sending data to another port, it's no longer to use file i/o  

> I have tried to use Flask and/or raw javascript, but they didn't return anything to html.  
As a last resort, I can only implement it with File I/O, so the project is not support Browser Source :persevere:

### ~~Why I hope users install font to local~~

**_Solved since 0.2.0:_**: With sending data to another port, it's no longer need to use web font while frequent refreshing by live.js.  

> Disable Cache can avoid refresh delay (~3-20s) during idling for 2 minutes. <sup>[[ref1]](https://forum.sambapos.com/t/2nd-screen-live-js-delayed-if-pos-screen-is-idle/12540)</sup>  
Local font can avoid font switching flashes.  
Maybe it can be solved by periodically adding junk comments to index.html :thinking:  

### Why I use PY file to save data instead of JSON

~~Just want to use int as key~~  
I don't want to spend too much code on File I/O.

### Relative Import

I have tried to use `sys.path` but it was not working again, why...
Maybe pyproject.toml is the only method I can improve the project structure...<sup>[[ref2]](https://stackoverflow.com/a/50194143)</sup>
