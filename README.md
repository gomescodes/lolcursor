<div align="center">
  <h1>𝙡𝙤𝙡𝙘𝙪𝙧𝙨𝙤𝙧</h1>
  <img src="https://raw.githubusercontent.com/gomescodes/lolcursor/main/favicon.ico" alt="drawing" width="200" />
  <br/>
  <h4>
    Change your League of Legends cursor size above the in-game limit.
  </h4>
</div>

## Authors

- [@gomescodes](https://www.github.com/gomescodes)
- [@aratakamikaze](https://www.github.com/aratakamikaze)

## v2.0.0 Roadmap

- [x] Get the `PersistentSettings.json` value at app start.

- [ ] System tray icon.

- [ ] Keep running option.

## Test Locally

Clone the project

```bash
  git clone https://github.com/gomescodes/lolcursor
```

Go to the project directory

```bash
  cd lolcursor
```

Install dependency

```bash
  pip install PySide6
```

Start the app

```bash
  python lolcursor.py
```

## Building Executable

Install dependency

```bash
  pip install pyinstaller
```

Run pyinstaller

```bash
  pyinstaller .\lolcursor.py -F -w --icon=favicon.ico --add-data="favicon.ico;."
```

## License

[GNU GLPv3](https://choosealicense.com/licenses/gpl-3.0/)
