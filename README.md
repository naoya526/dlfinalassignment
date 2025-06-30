## deeplearning final assignment
this is the instruction of how to use ALE environment and gymnasium.
please follow the procedure below.

### Gameplay Preview

![Breakout gameplay](movie/blockgame.gif)

### environment

- python 3.10
- wsl

---
### 1. Install gymnasium and ALE dependencies

```bash
pip install "gymnasium[atari]"
```

```bash
pip install ale-py
```
see the link of ale:
https://ale.farama.org/getting-started/


### 2.Install AutoROM to download Atari ROMs
next, you need to install AutoROM

```bash
pip install autorom
```


in my case, I needed to clarify the path:
```bash
mkdir ~/.local/share/gymnasium/roms
python3 -m autorom --accept-license --install-dir ~/.local/share/gymnasium/roms
```

or simply (if default path is fine)
```bash
AutoROM --accept-license
```

### 3. run the game

```bash
python play_human.py
```

- ←: Move left
- →: Move right
- Space: Fire (start the game)
- Close window to exit


## 📄 Licenses of Dependencies

This project uses the following open-source libraries:

| Library       | License         | Link                                 |
|---------------|------------------|--------------------------------------|
| gymnasium     | MIT              |  |
| ale-py        | BSD-2-Clause     |  |
| pygame        | LGPL             |  |
| numpy         | BSD              |  |

Please refer to the linked license files for more details.
